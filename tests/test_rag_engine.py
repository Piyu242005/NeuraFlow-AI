from services.rag_engine import RAGManager


def test_chunking_preserves_overlap_and_content():
    rag = object.__new__(RAGManager)
    chunks = rag._chunk_text("abcdefghij", chunk_size=6, overlap=2)
    assert chunks[0] == "abcdef"
    assert chunks[1].startswith("ef")
    assert "j" in chunks[-1]


def test_invalid_chunk_parameters_fail_fast():
    rag = object.__new__(RAGManager)
    try:
        rag._chunk_text("text", chunk_size=10, overlap=10)
    except ValueError:
        return
    raise AssertionError("Expected ValueError")
