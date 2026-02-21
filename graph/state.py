"""
State definitions for the LangGraph workflow.

Placeholder module for graph state TypedDicts and state update logic.
"""

from typing import Any, TypedDict


class PlanningState(TypedDict, total=False):
    """
    Placeholder state schema for the multi-agent planning graph.

    Will define all state keys passed between graph nodes.
    """

    messages: list[Any]
    tasks: list[Any]
    metadata: dict[str, Any]
