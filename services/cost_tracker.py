"""Centralized estimated LLM cost calculation."""

from services.router_policy import estimate_cost


def response_cost(provider: str, token_usage: dict | None) -> float:
    """Estimate cost from a normalized token usage dictionary."""
    usage = token_usage or {}
    input_tokens = int(usage.get("input_tokens", usage.get("prompt_tokens", 0)) or 0)
    output_tokens = int(usage.get("output_tokens", usage.get("completion_tokens", 0)) or 0)
    return round(estimate_cost(provider, input_tokens, output_tokens), 8)
