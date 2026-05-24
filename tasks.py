from crewai import Task
from agents import spy_agent, analyst_agent, advisor_agent

# Task 1 - Find Competitors
research_task = Task(
    description="""
        Research this startup idea: {startup_idea}
        
        Find and list:
        1. Top 5 direct competitors
        2. For each competitor write:
           - Their name
           - What they charge
           - What customers complain about
           - Who they target
    """,
    expected_output="A detailed list of 5 competitors with name, pricing, weaknesses for each",
    agent=spy_agent
)

# Task 2 - Find The Gap
analysis_task = Task(
    description="""
        Using the competitor research, find the GAP for: {startup_idea}
        
        Answer:
        1. What do ALL competitors do badly?
        2. Which customer is nobody serving well?
        3. What price point is missing?
        4. What feature does everyone want but nobody provides?
    """,
    expected_output="A clear market gap analysis with 3-4 specific opportunities",
    agent=analyst_agent,
    context=[research_task]
)

# Task 3 - Build Strategy
strategy_task = Task(
    description="""
        Create a positioning strategy for: {startup_idea}
        
        Include:
        1. Unique Value Proposition
        2. Target Customer
        3. Pricing Strategy
        4. Top 3 features to build first
        5. Marketing angle
    """,
    expected_output="A complete startup positioning strategy that a founder can act on immediately",
    agent=advisor_agent,
    context=[research_task, analysis_task]
)