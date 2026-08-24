# NeuraFlow AI — Production Readiness

## Architecture

```text
Streamlit UI
    │
    ├── Document ingestion → validation → chunking → ChromaDB
    │
    └── Query → task classifier → policy router → fallback manager
                                      │
                         ┌────────────┼────────────┐
                         ▼            ▼            ▼
                      Gemini        Groq      OpenRouter/HF
                                      │
                                      ▼
                           Observability + DB
                                      │
                           metrics / cost / health
```

## Routing policy

Auto mode combines four dimensions:

- quality
- speed
- estimated cost
- reliability

Provider profiles are intentionally configurable. If current provider prices are known, set environment variables such as:

```env
GEMINI_INPUT_USD_PER_1K=0
GEMINI_OUTPUT_USD_PER_1K=0
GROQ_INPUT_USD_PER_1K=0
GROQ_OUTPUT_USD_PER_1K=0
OPENROUTER_INPUT_USD_PER_1K=0
OPENROUTER_OUTPUT_USD_PER_1K=0
```

Do not treat the bundled zero-cost defaults as current vendor pricing.

## RAG quality

The RAG engine now provides:

- validated chunk parameters
- larger overlap for context continuity
- chunk-level metadata
- semantic distance + lexical-overlap reranking
- source-aware retrieval through `retrieve_with_sources()`
- deterministic offline evaluation utilities

## Evaluation

Use `evaluation/rag_evaluator.py` to measure retrieval recall and answer-term precision without requiring another paid LLM call.

The intended production evaluation loop is:

1. Create a labelled question set.
2. Run retrieval and generation.
3. Store retrieval/answer metrics.
4. Compare against the previous baseline.
5. Block regressions in CI when thresholds are missed.

For higher-quality evaluation, extend the dataset with human-labelled relevance, faithfulness and correctness scores.

## Security

Use `services/security.py` before processing uploads or tool-enabled prompts:

- validate PDF extension, size and magic bytes
- sanitize filenames
- detect common prompt-injection patterns
- keep provider credentials server-side
- enforce upload limits and rate limits at the deployment layer

Prompt-injection detection is a signal, not a complete security boundary. Tool permissions must still be enforced independently.

## Deployment checklist

- [ ] Use a managed secret store in production.
- [ ] Set CPU/memory requests and limits in Kubernetes.
- [ ] Configure liveness/readiness probes.
- [ ] Restrict ingress and enable TLS.
- [ ] Set provider quotas and timeouts.
- [ ] Persist ChromaDB or replace it with a managed vector database.
- [ ] Persist analytics in PostgreSQL for multi-instance deployments.
- [ ] Add rate limiting and authentication before public exposure.
- [ ] Run tests, linting and security scans in CI.
- [ ] Monitor latency, error rate, fallback rate, token usage and estimated cost.
