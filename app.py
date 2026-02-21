"""
Application entry point for the Multi-Agent Task Planning System.

Provides CLI entry points for running the FastAPI backend,
Streamlit frontend, or other services.
"""

import argparse
import sys
from pathlib import Path
from typing import NoReturn

# Ensure package is importable when run as python app.py from project root
_root = Path(__file__).resolve().parent
_parent = _root.parent
if str(_parent) not in sys.path:
    sys.path.insert(0, str(_parent))

from multi_agent_planner.config import get_settings
from multi_agent_planner.utils.logging import setup_logging


def run_api() -> None:
    """Start the FastAPI backend server."""
    setup_logging()
    settings = get_settings()

    import uvicorn
    from multi_agent_planner.api.main import app

    uvicorn.run(
        app,
        host=settings.api_host,
        port=settings.api_port,
        log_level=settings.log_level.lower(),
    )


def run_frontend() -> None:
    """Start the Streamlit frontend application."""
    setup_logging()

    import streamlit.web.cli as stcli

    frontend_app = Path(__file__).parent / "frontend" / "app.py"
    sys.argv = [
        "streamlit",
        "run",
        str(frontend_app),
        "--server.port=8501",
        "--server.address=0.0.0.0",
    ]
    sys.exit(stcli.main())


def main() -> NoReturn:
    """Parse CLI arguments and dispatch to the appropriate runner."""
    parser = argparse.ArgumentParser(
        description="Multi-Agent Task Planning System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python app.py api       Start FastAPI backend
  python app.py frontend  Start Streamlit UI
        """,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("api", help="Run the FastAPI backend server")
    subparsers.add_parser("frontend", help="Run the Streamlit frontend")

    args = parser.parse_args()

    if args.command == "api":
        run_api()
    elif args.command == "frontend":
        run_frontend()

    sys.exit(0)


if __name__ == "__main__":
    main()
