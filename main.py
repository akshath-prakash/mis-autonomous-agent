import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

# Load environment variables (reads ANTHROPIC_API_KEY from .env)
load_dotenv()

# Configure Claude as the LLM for CrewAI
claude_llm = LLM(
    model="anthropic/claude-sonnet-5-5",
    
)

# Define the 3 Agents using the Claude LLM
researcher = Agent(
    role="Lead Infrastructure Researcher",
    goal="Gather data on Northern California data center energy constraints and PG&E grid capacity upgrades.",
    backstory="You are an expert infrastructure analyst specialized in Silicon Valley utilities and energy grids.",
    verbose=True,
    allow_delegation=False,
    llm=claude_llm
)

writer = Agent(
    role="Executive Communications Director",
    goal="Synthesize raw tech infrastructure data into a concise, highly impactful executive brief.",
    backstory="You are a corporate communications veteran translating tech metrics into strategy reports.",
    verbose=True,
    allow_delegation=False,
    llm=claude_llm
)

auditor = Agent(
    role="Compliance and Quality Evaluation Engine",
    goal="Enforce strict corporate reporting compliance metrics. Act as the evaluation gatekeeper.",
    backstory="You are a ruthless corporate auditor verifying formatting, tone, and data integrity.",
    verbose=True,
    allow_delegation=True,
    llm=claude_llm
)

# Tasks
research_task = Task(
    description=(
        "Research Northern California data center energy constraints and PG&E "
        "grid capacity upgrades. Cover current constraints, planned upgrades, "
        "timelines, and risks. Flag anything you are unsure of rather than guessing figures."
    ),
    expected_output="A bulleted research summary with key facts, timelines, and clearly labeled uncertainties.",
    agent=researcher
)

writing_task = Task(
    description=(
        "Using the research, write a one-page executive brief for senior leadership: "
        "headline takeaway, key findings, risks, and recommended actions."
    ),
    expected_output="A concise executive brief in markdown, under 500 words.",
    agent=writer,
    context=[research_task]
)

audit_task = Task(
    description=(
        "Review the brief for formatting, tone, and data integrity. Remove or flag "
        "any claim not supported by the research. Return the final corrected brief."
    ),
    expected_output="The final, compliance-checked executive brief in markdown.",
    agent=auditor,
    context=[research_task, writing_task],
    output_file="executive_brief.md"
)

# Crew
crew = Crew(
    agents=[researcher, writer, auditor],
    tasks=[research_task, writing_task, audit_task],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    result = crew.kickoff()
    print(result)