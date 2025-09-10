class GoalBasedVacuumAgent:
    def __init__(self):
        self.location = "A"
        self.goal = {"A": "Clean", "B": "Clean"}

    def perceive(self, environment):
        return self.location, environment[self.location]

    def act(self, environment):
        if environment[self.location] == "Dirty":
            print(f"Cleaning {self.location}...")
            environment[self.location] = "Clean"
        elif environment != self.goal:
            print(f"{self.location} is clean. Moving...")
            self.location = "B" if self.location == "A" else "A"
        else:
            print("Goal achieved! Both rooms are clean.")

environment = {"A": "Dirty", "B": "Dirty"}

agent = GoalBasedVacuumAgent()
while environment != agent.goal:
    percept = agent.perceive(environment)
    agent.act(environment)
    print(environment)
