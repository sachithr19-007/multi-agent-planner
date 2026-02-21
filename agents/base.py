"""
Base agent abstractions for the Multi-Agent Task Planning System.

Placeholder module prepared for LangGraph agent definitions.
Agent logic will be implemented here.
"""

from typing import Any


class BaseAgent:
    """
    Placeholder base class for agent implementations.

    Will define the common interface and lifecycle for all agents
    in the planning system.
    """

    def __init__(self, name: str, **kwargs: Any) -> None:
        """Initialize the agent with a name and optional configuration."""
        self.name = name

    def __repr__(self) -> str:
        """Return string representation of the agent."""
        return f"{self.__class__.__name__}(name={self.name!r})"
