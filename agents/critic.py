from typing import Any, List

class CriticAgent:
    def __init__(self, name: str = "critic", **kwargs: Any) -> None:
        self.name = name

    def run(self, plan_steps: List[str]) -> List[str]:
        suggestions = []
        for step in plan_steps:
            suggestions.append(f"Review feasibility of: {step}")
        return suggestions