# researcher.py — Free Testing Version

from typing import Any

class BaseAgent:
    def __init__(self, name="base", **kwargs):
        pass

class ResearcherAgentError(Exception):
    pass

class ResearchAgent(BaseAgent):
    def __init__(self, name: str = "researcher", **kwargs: Any):
        super().__init__(name=name, **kwargs)

    def run(self, goal: str) -> list[str]:
        if not goal or not goal.strip():
            raise ResearcherAgentError("Goal cannot be empty")
        
        goal = goal.strip()

        # MOCK research steps
        mock_steps = [
            f"Gather information about {goal}",
            f"Look up best practices and tips for {goal}",
            f"Analyze resources and constraints for {goal}",
        ]
        return mock_steps