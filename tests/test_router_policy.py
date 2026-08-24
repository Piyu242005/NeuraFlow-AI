from services.router_policy import estimate_cost, select_provider


def test_router_selects_from_available_providers():
    selected, reason, score = select_provider(
        "reasoning", "OpenRouter", {"Gemini": object(), "Groq": object(), "OpenRouter": object()}
    )
    assert selected in {"Gemini", "Groq", "OpenRouter"}
    assert "selected by" in reason
    assert 0 <= score <= 1


def test_cost_estimate_is_non_negative():
    assert estimate_cost("Gemini", 1000, 1000) >= 0
