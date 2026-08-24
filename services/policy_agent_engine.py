"""Policy-aware AgentEngine wrapper."""

from services.agent_engine import AgentEngine
from services.router_policy import select_provider
from services.task_classifier import classify_task


class PolicyAgentEngine(AgentEngine):
    """AgentEngine with deterministic cost/quality/speed/reliability routing."""

    def _decision_target(self, prompt: str):
        if self.mode != "auto":
            return "manual", self.mode, "Manually selected by user", 1.0
        task_type, classifier_provider, _ = classify_task(prompt)
        selected, reason, score = select_provider(
            task_type, classifier_provider, self.providers
        )
        return task_type, selected, reason, score

    def run(self, prompt: str):
        task_type, preferred, reason, score = self._decision_target(prompt)
        response, fallback_log = self._fallback_manager.execute_with_fallback(
            prompt=prompt, preferred_provider=preferred
        )
        from services.agent_engine import AgentDecision
        return AgentDecision(
            task_type=task_type,
            selected_provider=preferred,
            actual_provider=response.provider,
            reason=reason,
            response=response,
            fallback_log=fallback_log,
            fallback_used=response.fallback_used,
            routing_score=score,
        )

    def run_stream(self, prompt: str, status_callback=None):
        task_type, preferred, reason, score = self._decision_target(prompt)
        generator, fallback_log = self._fallback_manager.execute_stream_with_fallback(
            prompt=prompt,
            preferred_provider=preferred,
            status_callback=status_callback,
        )
        from services.agent_engine import StreamWrapper
        wrapper = StreamWrapper(
            generator, task_type, preferred, reason, fallback_log
        )
        wrapper.routing_score = score
        return wrapper
