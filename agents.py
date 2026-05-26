from crewai import Agent
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    model_name="meta-llama/llama-3.3-70b-instruct",
    temperature=0.7
)

search_tool = SerperDevTool()

spy_agent = Agent(
    role="Competitor Research Specialist",
    goal="Find ALL competitors for the startup idea: {startup_idea} with their pricing and weaknesses",
    backstory="You are an expert market researcher who finds accurate business information from the web.",
    tools=[search_tool],
    llm=llm,
    verbose=True
)

analyst_agent = Agent(
    role="Market Gap Analyst",
    goal="Find the market gap and underserved customers for: {startup_idea}",
    backstory="You are a senior business consultant who specializes in finding market opportunities.",
    llm=llm,
    verbose=True
)

advisor_agent = Agent(
    role="Startup Strategy Advisor",
    goal="Create a clear positioning strategy for: {startup_idea}",
    backstory="You are a startup mentor who gives practical, actionable advice.",
    llm=llm,
    verbose=True
)