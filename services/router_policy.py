"""Cost/quality/latency-aware provider selection policy.

The policy is deliberately deterministic and configurable through environment
variables so portfolio demos remain reproducible and production deployments can
replace the defaults with current provider pricing/SLAs.
"""

from dataclasses import dataclass
import os
from typing import Dict, Tuple


@dataclass(frozen=True)
class ProviderProfile:
    quality: float
    speed: float
    cost: float
    reliability: float
    input_cost_per_1k: float
    output_cost_per_1k: float


DEFAULT_PROFILES: Dict[str, ProviderProfile] = {
    "Gemini": ProviderProfile(0.90, 0.82, 0.88, 0.92, 0.0, 0.0),
    "Groq": ProviderProfile(0.84, 0.98, 0.86, 0.90, 0.0, 0.0),
    "OpenRouter": ProviderProfile(0.94, 0.78, 0.72, 0.88, 0.0, 0.0),
    "Hugging Face": ProviderProfile(0.78, 0.68, 0.90, 0.82, 0.0, 0.0),
}


def _env_float(name: str, default: float) -> float:
    try:
        return float(os.getenv(name, default))
    except (TypeError, ValueError):
        return default


def estimate_cost(provider: str, input_tokens: int = 0, output_tokens: int = 0) -> float:
    """Estimate USD cost from optional environment-configured rates."""
    profile = DEFAULT_PROFILES.get(provider)
    if not profile:
        return 0.0
    input_rate = _env_float(f"{provider.upper().replace(' ', '_')}_INPUT_USD_PER_1K", profile.input_cost_per_1k)
    output_rate = _env_float(f"{provider.upper().replace(' ', '_')}_OUTPUT_USD_PER_1K", profile.output_cost_per_1k)
    return (input_tokens / 1000.0) * input_rate + (output_tokens / 1000.0) * output_rate


def select_provider(task_type: str, preferred: str, available: Dict[str, object]) -> Tuple[str, str, float]:
    """Return (provider, explanation, score) using task-aware weighted scoring."""
    if preferred in available:
        candidates = list(available)
    else:
        candidates = list(available)
    if not candidates:
        return preferred, "No configured provider; execution will fail clearly.", 0.0

    weights = {
        "coding": (0.35, 0.30, 0.15, 0.20),
        "reasoning": (0.45, 0.10, 0.15, 0.30),
        "experimentation": (0.35, 0.15, 0.25, 0.25),
        "general": (0.35, 0.20, 0.25, 0.20),
        "manual": (0.40, 0.20, 0.20, 0.20),
    }.get(task_type, (0.35, 0.20, 0.25, 0.20))

    scores = {}
    for name in candidates:
        p = DEFAULT_PROFILES.get(name, ProviderProfile(0.7, 0.7, 0.7, 0.7, 0.0, 0.0))
        score = (
            weights[0] * p.quality
            + weights[1] * p.speed
            + weights[2] * p.cost
            + weights[3] * p.reliability
        )
        scores[name] = score

    selected = max(scores, key=scores.get)
    score = scores[selected]
    reason = (
        f"{selected} selected by quality/speed/cost/reliability policy "
        f"for {task_type} (score {score:.2f})."
    )
    if preferred in available and preferred != selected:
        reason += f" Classifier preference was {preferred}; policy overrode it using configured profiles."
    return selected, reason, score
