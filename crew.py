from crewai import Crew, Process
from agents import spy_agent, analyst_agent, advisor_agent
from tasks import research_task, analysis_task, strategy_task
from dotenv import load_dotenv

load_dotenv()

def analyze_startup(startup_idea):

    crew = Crew(
        agents=[spy_agent, analyst_agent, advisor_agent],
        tasks=[research_task, analysis_task, strategy_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff(inputs={"startup_idea": startup_idea})

    return result