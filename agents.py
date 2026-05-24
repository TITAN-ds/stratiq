from crewai import Agent
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

search_tool = SerperDevTool()

# Agent 1 - The Spy
spy_agent = Agent(
    role="Competitor Research Specialist",
    goal="Find ALL competitors for the startup idea: {startup_idea} with their pricing and weaknesses",
    backstory="You are an expert market researcher who finds accurate business information from the web.",
    tools=[search_tool],
    llm="openrouter/meta-llama/llama-3.3-70b-instruct",
    verbose=True
)

# Agent 2 - The Analyst
analyst_agent = Agent(
    role="Market Gap Analyst",
    goal="Find the market gap and underserved customers for: {startup_idea}",
    backstory="You are a senior business consultant who specializes in finding market opportunities.",
    llm="openrouter/meta-llama/llama-3.3-70b-instruct",
    verbose=True
)

# Agent 3 - The Advisor
advisor_agent = Agent(
    role="Startup Strategy Advisor",
    goal="Create a clear positioning strategy for: {startup_idea}",
    backstory="You are a startup mentor who gives practical, actionable advice.",
    llm="openrouter/meta-llama/llama-3.3-70b-instruct",
    verbose=True
)