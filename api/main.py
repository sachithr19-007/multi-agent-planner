from fastapi import FastAPI
from pydantic import BaseModel

from multi_agent_planner.orchestrator import MultiAgentOrchestrator
from multi_agent_planner.agents.planner import PlannerAgent
from multi_agent_planner.agents.researcher import ResearcherAgent
from multi_agent_planner.agents.critic import CriticAgent

app = FastAPI()


class GoalRequest(BaseModel):
    goal: str


@app.post("/plan")
def generate_plan(request: GoalRequest):
    planner = PlannerAgent()
    researcher = ResearcherAgent()
    critic = CriticAgent()

    orchestrator = MultiAgentOrchestrator(
        planner,
        researcher,
        critic
    )

    result = orchestrator.run(request.goal)

    return result