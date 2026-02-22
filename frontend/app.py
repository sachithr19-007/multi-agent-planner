import os
import sys
import streamlit as st

# -----------------------------
# Add project root to Python path
# -----------------------------
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
sys.path.append(PROJECT_ROOT)

# -----------------------------
# Import Agents
# -----------------------------
from agents.planner import PlannerAgent
from agents.researcher import ResearchAgent
from agents.critic import CriticAgent

# -----------------------------
# App Configuration
# -----------------------------
st.set_page_config(page_title="Multi-Agent Task Planner", page_icon="📝")
st.title("📝 Multi-Agent Task Planner")
st.markdown(
    "Enter a goal and let multiple agents collaborate to generate a structured plan."
)
st.divider()

# -----------------------------
# Initialize Agents
# -----------------------------
planner = PlannerAgent()
researcher = ResearchAgent()
critic = CriticAgent()

# -----------------------------
# User Input
# -----------------------------
goal = st.text_input("🎯 Enter your goal:", "")

# -----------------------------
# Generate Plan Button
# -----------------------------
if st.button("Generate Plan", use_container_width=True):
    if not goal.strip():
        st.warning("⚠️ Please enter a goal first.")
    else:
        with st.spinner("Agents are thinking..."):
            try:
                # ---- Planner ----
                planner_output = planner.plan(goal)

                # ---- Researcher ----
                research_steps = researcher.run(goal)

                # ---- Critic ----
                critic_feedback = critic.run(planner_output["tasks"])

                st.success("✅ Plan generated successfully!")
                st.divider()

                # -----------------------------
                # Planner Output
                # -----------------------------
                with st.expander("📋 Planner Output", expanded=True):
                    for task in planner_output["tasks"]:
                        st.write(f"**Step {task['step']}** — {task['task']}")

                # -----------------------------
                # Research Output
                # -----------------------------
                with st.expander("🔎 Research Output"):
                    for step in research_steps:
                        st.write(f"- {step}")

                # -----------------------------
                # Critic Feedback
                # -----------------------------
                with st.expander("🧐 Critic Feedback"):
                    for feedback in critic_feedback:
                        st.write(f"- {feedback}")

            except Exception as e:
                st.error(f"Execution failed: {e}")

st.markdown("---")
st.caption("Built with Streamlit • Multi-Agent Mock • Day 3 Complete 🚀")