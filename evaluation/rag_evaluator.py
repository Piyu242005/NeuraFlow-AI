"""Offline RAG evaluation utilities.

The evaluator intentionally avoids paid model calls. It measures retrieval
coverage and answer overlap against a small labelled dataset, making it useful
for regression tests in CI.
"""

from dataclasses import dataclass
import re
from typing import Iterable


@dataclass(frozen=True)
class EvalCase:
    question: str
    expected_terms: tuple[str, ...]


def _terms(text: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z0-9]{3,}", (text or "").lower()))


def retrieval_recall(retrieved_text: str, expected_terms: Iterable[str]) -> float:
    expected = {str(x).lower() for x in expected_terms if str(x).strip()}
    if not expected:
        return 1.0
    found = _terms(retrieved_text)
    return len(expected & found) / len(expected)


def answer_term_precision(answer: str, expected_terms: Iterable[str]) -> float:
    expected = {str(x).lower() for x in expected_terms if str(x).strip()}
    if not expected:
        return 1.0
    found = _terms(answer)
    return len(found & expected) / max(len(found), 1)


def evaluate_case(case: EvalCase, retrieved_text: str, answer: str) -> dict:
    recall = retrieval_recall(retrieved_text, case.expected_terms)
    precision = answer_term_precision(answer, case.expected_terms)
    return {
        "question": case.question,
        "retrieval_recall": round(recall, 4),
        "answer_term_precision": round(precision, 4),
        "score": round((recall + precision) / 2, 4),
    }


def evaluate_dataset(cases: list[EvalCase], retrieved_answers: list[tuple[str, str]]) -> dict:
    """Evaluate labelled cases; retrieved_answers contains (context, answer)."""
    if len(cases) != len(retrieved_answers):
        raise ValueError("cases and retrieved_answers must have equal length")
    results = [
        evaluate_case(case, context, answer)
        for case, (context, answer) in zip(cases, retrieved_answers)
    ]
    if not results:
        return {"cases": 0, "retrieval_recall": 0.0, "answer_precision": 0.0, "score": 0.0}
    return {
        "cases": len(results),
        "retrieval_recall": round(sum(r["retrieval_recall"] for r in results) / len(results), 4),
        "answer_precision": round(sum(r["answer_term_precision"] for r in results) / len(results), 4),
        "score": round(sum(r["score"] for r in results) / len(results), 4),
        "results": results,
    }
