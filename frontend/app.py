import streamlit as st

from multi_agent_planner.orchestrator import MultiAgentOrchestrator
from multi_agent_planner.agents.planner import PlannerAgent
from multi_agent_planner.agents.researcher import ResearcherAgent
from multi_agent_planner.agents.critic import CriticAgent


st.title("Multi-Agent Planner")

goal = st.text_area("Enter your goal:")

if st.button("Generate Plan"):
    if not goal.strip():
        st.warning("Please enter a goal.")
    else:
        # Initialize agents
        planner = PlannerAgent()
        researcher = ResearcherAgent()
        critic = CriticAgent()

        orchestrator = MultiAgentOrchestrator(
            planner,
            researcher,
            critic
        )

        with st.spinner("Running multi-agent system..."):
            result = orchestrator.run(goal)

        st.subheader("Final Tasks")
        st.write(result["tasks"])

        st.subheader("Research Insights")
        st.write(result["research"])

        st.subheader("Critic Feedback")
        st.write(result["feedback"])