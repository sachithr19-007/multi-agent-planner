# planner.py — Free Testing Version

from typing import Any
from pydantic import BaseModel, Field

# -------------------------------
# Temporary BaseAgent for free testing
# -------------------------------
class BaseAgent:
    def __init__(self, name="base", **kwargs):
        pass

# -------------------------------
# Dummy logger to prevent errors
# -------------------------------
class DummyLogger:
    def debug(self, *args, **kwargs): pass
    def info(self, *args, **kwargs): pass
    def exception(self, *args, **kwargs): pass

logger = DummyLogger()

# -------------------------------
# Subtask and PlanResult Models
# -------------------------------
class Subtask(BaseModel):
    step: int = Field(..., description="Ordered step number")
    task: str = Field(..., description="Task description")

class PlanResult(BaseModel):
    goal: str = Field(..., description="The original user goal")
    tasks: list[Subtask] = Field(default_factory=list, description="Ordered list of subtasks")

    def to_dict(self) -> dict[str, Any]:
        return {
            "goal": self.goal,
            "tasks": [{"step": t.step, "task": t.task} for t in sorted(self.tasks, key=lambda x: x.step)],
        }

# -------------------------------
# PlannerAgentError
# -------------------------------
class PlannerAgentError(Exception):
    pass

# -------------------------------
# PlannerAgent
# -------------------------------
class PlannerAgent(BaseAgent):
    """
    Agent that breaks down user goals into ordered subtasks.
    Uses a MOCK for free testing if no LLM API keys are set.
    """

    def __init__(self, name: str = "planner", **kwargs: Any) -> None:
        super().__init__(name=name, **kwargs)
        logger.debug("PlannerAgent initialized", extra={"name": name})

    def plan(self, goal: str) -> dict[str, Any]:
        if not goal or not goal.strip():
            raise PlannerAgentError("Goal cannot be empty")

        goal = goal.strip()
        logger.info("Planning started", extra={"goal": goal[:80]})

        mock_tasks = [
            {"step": 1, "task": "Research budget options for the goal"},
            {"step": 2, "task": "Book necessary resources"},
            {"step": 3, "task": "Plan detailed steps"},
            {"step": 4, "task": "Finalize and review"},
        ]

        result = PlanResult(
            goal=goal,
            tasks=[Subtask(**t) for t in mock_tasks]
        )

        return result.to_dict()

    # ✅ NEW: refinement method for multi-agent loop
    def refine(self, tasks: list[dict[str, Any]], feedback: list[str]) -> list[dict[str, Any]]:
        """
        Refines tasks based on critic feedback.
        For now, we simulate improvement.
        """

        refined_tasks = []

        for task in tasks:
            updated_task = task.copy()

            if feedback:
                updated_task["task"] += " (Improved after critique)"

            refined_tasks.append(updated_task)

        return refined_tasks