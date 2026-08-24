"""Lightweight provider health and reliability tracking."""

from collections import defaultdict
from dataclasses import dataclass
from time import time


@dataclass
class HealthSnapshot:
    requests: int = 0
    successes: int = 0
    failures: int = 0
    total_latency: float = 0.0
    last_error: str = ""
    last_seen: float = 0.0

    @property
    def success_rate(self) -> float:
        return self.successes / self.requests if self.requests else 1.0

    @property
    def avg_latency(self) -> float:
        return self.total_latency / self.requests if self.requests else 0.0


class ProviderHealthTracker:
    """In-process health tracker suitable for dashboards and routing signals."""

    def __init__(self):
        self._data = defaultdict(HealthSnapshot)

    def record(self, provider: str, success: bool, latency: float, error: str = ""):
        item = self._data[provider]
        item.requests += 1
        item.total_latency += max(0.0, float(latency))
        item.last_seen = time()
        if success:
            item.successes += 1
        else:
            item.failures += 1
            item.last_error = error[:300]

    def snapshot(self) -> dict[str, dict]:
        return {
            name: {
                "requests": item.requests,
                "success_rate": round(item.success_rate * 100, 2),
                "avg_latency": round(item.avg_latency, 4),
                "last_error": item.last_error,
                "last_seen": item.last_seen,
            }
            for name, item in self._data.items()
        }
