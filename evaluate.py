"""Batch runner: runs the 3-agent pipeline on many topics and saves every stage.

For each topic it saves:
  results/<topic>/research.md  (researcher output)
  results/<topic>/draft.md     (writer output = the "without auditor" version)
  results/<topic>/final.md     (auditor output = the "with auditor" version)
and appends time + token usage to results/run_log.csv.
Re-running skips topics that are already finished, so you can stop and resume.
"""
import csv
import re
import time
from pathlib import Path

from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

load_dotenv()
llm = LLM(model="anthropic/claude-sonnet-5-5")

# Start with 2-3 to test, then use all of them.
TOPICS = [
    "Northern California data center energy constraints and PG&E grid capacity upgrades",
    "Ransomware trends affecting hospitals in the United States",
    "Adoption of multi-factor authentication in small businesses",
    "Cloud cost optimization (FinOps) for mid-sized companies",
    "Zero trust architecture adoption in enterprises",
    "Generative AI governance policies in large corporations",
    "Supply chain visibility technology in retail",
    "Data privacy compliance for California businesses (CCPA/CPRA)",
    "Phishing attack trends and employee security training",
    "ERP system migration risks for mid-sized manufacturers",
    "Edge computing in logistics and warehousing",
    "Cyber insurance market conditions for small and mid-sized businesses",
]

RESULTS = Path("results")


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60]


def build_crew(topic):
    researcher = Agent(
        role="Lead Researcher",
        goal=f"Gather data on: {topic}.",
        backstory="You are an expert analyst who clearly labels anything you are unsure of.",
        verbose=False, allow_delegation=False, llm=llm,
    )
    writer = Agent(
        role="Executive Communications Director",
        goal="Synthesize raw research into a concise, highly impactful executive brief.",
        backstory="You are a corporate communications veteran translating metrics into strategy reports.",
        verbose=False, allow_delegation=False, llm=llm,
    )
    auditor = Agent(
        role="Compliance and Quality Evaluation Engine",
        goal="Enforce strict corporate reporting compliance metrics. Act as the evaluation gatekeeper.",
        backstory="You are a ruthless corporate auditor verifying formatting, tone, and data integrity.",
        verbose=False, allow_delegation=True, llm=llm,
    )
    research_task = Task(
        description=(f"Research: {topic}. Cover current constraints, planned developments, "
                     "timelines, and risks. Flag anything you are unsure of rather than guessing figures."),
        expected_output="A bulleted research summary with key facts, timelines, and clearly labeled uncertainties.",
        agent=researcher,
    )
    writing_task = Task(
        description=("Using the research, write a one-page executive brief for senior leadership: "
                     "headline takeaway, key findings, risks, and recommended actions."),
        expected_output="A concise executive brief in markdown, under 500 words.",
        agent=writer, context=[research_task],
    )
    audit_task = Task(
        description=("Review the brief for formatting, tone, and data integrity. Remove or flag "
                     "any claim not supported by the research. Return the final corrected brief."),
        expected_output="The final, compliance-checked executive brief in markdown.",
        agent=auditor, context=[research_task, writing_task],
    )
    return Crew(agents=[researcher, writer, auditor],
                tasks=[research_task, writing_task, audit_task],
                process=Process.sequential, verbose=False)


def log_row(row):
    RESULTS.mkdir(exist_ok=True)
    path = RESULTS / "run_log.csv"
    new = not path.exists()
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["topic", "status", "seconds", "total_tokens",
                                          "prompt_tokens", "completion_tokens"])
        if new:
            w.writeheader()
        w.writerow(row)


def main():
    # CrewAI's token counter is cumulative for the whole script run, so we log the difference per topic.
    prev = {"total_tokens": 0, "prompt_tokens": 0, "completion_tokens": 0}
    for i, topic in enumerate(TOPICS, 1):
        folder = RESULTS / slugify(topic)
        if (folder / "final.md").exists():
            print(f"[{i}/{len(TOPICS)}] skip (done): {topic}")
            continue
        print(f"[{i}/{len(TOPICS)}] running: {topic}")
        start = time.time()
        try:
            result = build_crew(topic).kickoff()
            outs = [t.raw for t in result.tasks_output]
            folder.mkdir(parents=True, exist_ok=True)
            (folder / "research.md").write_text(outs[0])
            (folder / "draft.md").write_text(outs[1])
            (folder / "final.md").write_text(outs[2])
            u = getattr(result, "token_usage", None)
            cur = {k: (getattr(u, k, 0) or 0) for k in prev}
            log_row({"topic": topic, "status": "ok", "seconds": round(time.time() - start),
                     **{k: cur[k] - prev[k] for k in prev}})
            prev = cur
        except Exception as e:
            print(f"  FAILED: {e}")
            log_row({"topic": topic, "status": f"failed: {str(e)[:80]}",
                     "seconds": round(time.time() - start),
                     "total_tokens": "", "prompt_tokens": "", "completion_tokens": ""})


if __name__ == "__main__":
    main()
