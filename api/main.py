"""
FastAPI application entry point.

Placeholder module for API server setup and route registration.
"""

from fastapi import FastAPI

from multi_agent_planner.config import get_settings


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.

    Returns:
        Configured FastAPI application instance.
    """
    get_settings()
    app = FastAPI(
        title="Multi-Agent Task Planning API",
        version="0.1.0",
        description="API for the Autonomous Multi-Agent AI Task Planning System",
    )
    # Route registration will be added here
    return app


app = create_app()


@app.get("/health")
def health_check() -> dict[str, str]:
    """Health check endpoint for load balancers and monitoring."""
    return {"status": "healthy"}
