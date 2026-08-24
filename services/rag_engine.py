"""RAG engine with deterministic chunking, metadata and lightweight reranking."""

import re
import time
from typing import Callable, Optional

import chromadb


class RAGManager:
    """Document indexing and retrieval using persistent ChromaDB."""

    def __init__(self, db_path="./chroma_db", collection_name="document_context"):
        self.client = chromadb.PersistentClient(path=db_path)
        self.default_collection_name = collection_name
        self.collection_name = collection_name
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name
        )

    def _chunk_text(self, text: str, chunk_size: int = 1500, overlap: int = 180) -> list:
        if chunk_size <= 0 or overlap < 0 or overlap >= chunk_size:
            raise ValueError("chunk_size must be > overlap >= 0")
        text = (text or "").strip()
        chunks = []
        start = 0
        while start < len(text):
            end = min(start + chunk_size, len(text))
            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)
            if end == len(text):
                break
            start = end - overlap
        return chunks

    @staticmethod
    def _tokens(text: str) -> set[str]:
        return set(re.findall(r"[a-zA-Z0-9]{3,}", (text or "").lower()))

    def _rerank(self, query: str, documents: list, distances: list, metadatas: list) -> list:
        """Blend semantic distance with lexical overlap for stable retrieval."""
        q = self._tokens(query)
        ranked = []
        for idx, doc in enumerate(documents):
            d = distances[idx] if idx < len(distances) else 1.0
            semantic = 1.0 / (1.0 + max(d, 0.0))
            overlap = len(q & self._tokens(doc)) / max(len(q), 1)
            score = 0.75 * semantic + 0.25 * overlap
            ranked.append((score, idx, doc, metadatas[idx] if idx < len(metadatas) else {}))
        ranked.sort(key=lambda x: x[0], reverse=True)
        return ranked

    def set_collection(self, collection_name: str):
        self.collection_name = collection_name
        self.collection = self.client.get_or_create_collection(name=collection_name)

    def is_indexed(self, doc_hash: str) -> bool:
        try:
            coll = self.client.get_collection(name=f"doc_{doc_hash}")
            return coll.count() > 0
        except Exception:
            return False

    def index_document(
        self,
        document_text: str,
        doc_hash: Optional[str] = None,
        metadata: Optional[dict] = None,
        progress_callback: Optional[Callable[[str, int], None]] = None,
    ) -> dict:
        start_time = time.time()
        if doc_hash:
            self.collection_name = f"doc_{doc_hash}"
        else:
            self.collection_name = self.default_collection_name
            try:
                self.client.delete_collection(self.collection_name)
            except Exception:
                pass
        self.collection = self.client.get_or_create_collection(name=self.collection_name)

        if progress_callback:
            progress_callback("📖 Extracting Text...", 20)
        chunks = self._chunk_text(document_text)
        if not chunks:
            return {"chunks": 0, "embeddings": 0, "time": 0.0, "cache_hit": False}
        if progress_callback:
            progress_callback("✂️ Creating chunks...", 40)
            progress_callback("🧠 Generating embeddings...", 70)

        ids = [f"chunk_{i}" for i in range(len(chunks))]
        metadatas = []
        base = dict(metadata or {})
        for i in range(len(chunks)):
            item = dict(base)
            item["chunk_index"] = i
            item["chunk_count"] = len(chunks)
            metadatas.append(item)

        if progress_callback:
            progress_callback("💾 Building vector index...", 90)
        self.collection.add(documents=chunks, ids=ids, metadatas=metadatas)
        elapsed = time.time() - start_time
        if progress_callback:
            progress_callback("✅ Ready for search", 100)
        return {
            "chunks": len(chunks),
            "embeddings": len(chunks),
            "time": elapsed,
            "cache_hit": False,
        }

    def retrieve_context(self, query: str, k: int = 5):
        start_time = time.time()
        if not query or not query.strip() or self.collection.count() == 0:
            return "", 0.0, time.time() - start_time, 0
        k = max(1, min(int(k), self.collection.count()))
        results = self.collection.query(
            query_texts=[query],
            n_results=k,
            include=["documents", "distances", "metadatas"],
        )
        retrieval_time = time.time() - start_time
        documents = results.get("documents", [[]])[0]
        if not documents:
            return "", 0.0, retrieval_time, 0
        distances = results.get("distances", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        ranked = self._rerank(query, documents, distances, metadatas)
        selected = ranked[:k]
        context_str = "\n\n---\n\n".join(item[2] for item in selected)
        similarity_score = sum(item[0] for item in selected) / len(selected)
        return context_str, similarity_score, retrieval_time, len(selected)

    def retrieve_with_sources(self, query: str, k: int = 5) -> dict:
        """Return ranked chunks and metadata for citation-aware UIs."""
        if not query or self.collection.count() == 0:
            return {"items": [], "retrieval_time": 0.0}
        start = time.time()
        k = max(1, min(int(k), self.collection.count()))
        results = self.collection.query(
            query_texts=[query], n_results=k, include=["documents", "distances", "metadatas"]
        )
        docs = results.get("documents", [[]])[0]
        distances = results.get("distances", [[]])[0]
        metas = results.get("metadatas", [[]])[0]
        ranked = self._rerank(query, docs, distances, metas)
        return {
            "items": [
                {"text": item[2], "score": round(item[0], 4), "metadata": item[3]}
                for item in ranked[:k]
            ],
            "retrieval_time": time.time() - start,
        }
