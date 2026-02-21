# planner_test.py
# Free testing version of PlannerAgent

# Minimal BaseAgent so it works without imports
class BaseAgent:
    def __init__(self, name="base", **kwargs):
        pass

from typing import Any
from pydantic import BaseModel, Field

# Subtask and PlanResult models
class Subtask(BaseModel):
    step: int = Field(..., description="Ordered step number")
    task: str = Field(..., description="Task description")

class PlanResult(BaseModel):
    goal: str = Field(..., description="The original user goal")
    tasks: list[Subtask] = Field(default_factory=list, description="Ordered list of subtasks")

    def to_dict(self) -> dict[str, Any]:
        return {
            "goal": self.goal,
            "tasks": [{"step": t.step, "task": t.task} for t in self.tasks]
        }

# PlannerAgent with MOCK
class PlannerAgent(BaseAgent):
    def __init__(self, name: str = "planner", **kwargs: Any) -> None:
        super().__init__(name=name, **kwargs)

    def plan(self, goal: str) -> dict[str, Any]:
        if not goal.strip():
            raise ValueError("Goal cannot be empty")
        # MOCK tasks
        mock_tasks = [
            {"step": 1, "task": "Research budget options for the goal"},
            {"step": 2, "task": "Book necessary resources"},
            {"step": 3, "task": "Plan detailed steps"},
            {"step": 4, "task": "Finalize and review"},
        ]
        return PlanResult(goal=goal, tasks=[Subtask(**t) for t in mock_tasks]).to_dict()

# Test run
if __name__ == "__main__":
    agent = PlannerAgent()
    result = agent.plan("Plan a 3-day Goa trip under 20000 INR")
    print(result)