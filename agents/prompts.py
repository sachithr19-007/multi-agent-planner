"""
Reusable prompt templates for the Multi-Agent Task Planning System.
"""

PLANNER_TASK_BREAKDOWN_TEMPLATE = """You are an expert task planner. Break down the following user goal into clear, ordered subtasks.

User goal: {goal}

Requirements:
- Each subtask should be specific, actionable, and achievable
- Order tasks logically (prerequisites first)
- Use clear, concise language
- Return exactly the JSON structure below, with no additional text

Output format (strict JSON):
{{
  "goal": "the original user goal",
  "tasks": [
    {{"step": 1, "task": "first subtask description"}},
    {{"step": 2, "task": "second subtask description"}}
  ]
}}
"""
