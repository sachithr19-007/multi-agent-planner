class MultiAgentOrchestrator:
    def __init__(self, planner, researcher, critic):
        self.planner = planner
        self.researcher = researcher
        self.critic = critic

    def run(self, goal):
        # Shared memory
        shared_state = {
            "goal": goal,
            "tasks": [],
            "research": [],
            "feedback": []
        }

        # -------------------
        # 1️⃣ Planner
        # -------------------
        planner_output = self.planner.plan(goal)
        shared_state["tasks"] = planner_output["tasks"]

        # -------------------
        # 2️⃣ Researcher
        # -------------------
        research_output = self.researcher.run(goal)
        shared_state["research"] = research_output

        # -------------------
        # 3️⃣ Critic
        # -------------------
        critic_output = self.critic.run(shared_state["tasks"])
        shared_state["feedback"] = critic_output

        # -------------------
        # 4️⃣ Refinement Loop
        # -------------------
        if critic_output:
            refined_plan = self.planner.refine(
                shared_state["tasks"],
                critic_output
            )
            shared_state["tasks"] = refined_plan

        return shared_state