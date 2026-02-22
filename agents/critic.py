# critic.py — Free Testing Version

from typing import Any

class BaseAgent:
    def __init__(self, name="base", **kwargs):
        pass

class CriticAgentError(Exception):
    pass

class CriticAgent(BaseAgent):
    def __init__(self, name: str = "critic", **kwargs: Any):
        super().__init__(name=name, **kwargs)

    def run(self, planner_steps: list) -> list[str]:
        if not planner_steps:
            raise CriticAgentError("No planner steps provided")
        
        # MOCK feedback
        feedback = [f"Check: {step}" for step in planner_steps]
        return feedback