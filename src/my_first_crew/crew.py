from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import DirectoryReadTool, FileReadTool
from typing import List

REPO_DIR = r"C:\Users\wsqsy\Documents\cpp\tigr_test"


@CrewBase
class MyFirstCrew:
    """MyFirstCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def code_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config["code_reviewer"],
            tools=[
                DirectoryReadTool(
                    directory=REPO_DIR
                ), 
                FileReadTool(),
            ],
            verbose=True,
        )

    @agent
    def json_generator(self) -> Agent:
        return Agent(
            config=self.agents_config["json_generator"],
            tools=[],
            verbose=True,
        )

    @task
    def code_review_task(self) -> Task:
        return Task(
            config=self.tasks_config["code_review_task"],
            output_file="code_review.md",
        )
    
    @task
    def review_json_task(self) -> Task:
        return Task(
            config=self.tasks_config["review_json_task"],
            output_file="issues.json",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MyFirstCrew crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
