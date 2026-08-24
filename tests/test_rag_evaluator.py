from evaluation.rag_evaluator import EvalCase, evaluate_case, evaluate_dataset


def test_evaluate_case():
    case = EvalCase("What is the purpose?", ("purpose", "document"))
    result = evaluate_case(case, "The purpose of this document is clear.", "The document purpose is clear.")
    assert result["retrieval_recall"] == 1.0
    assert result["score"] > 0


def test_dataset_rejects_mismatched_lengths():
    try:
        evaluate_dataset([EvalCase("q", ("answer",))], [])
    except ValueError:
        return
    raise AssertionError("Expected ValueError")
