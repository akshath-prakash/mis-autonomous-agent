# MIS Autonomous Agent: Multi-Agent Executive Brief Generator

A three-agent workflow built with [CrewAI](https://www.crewai.com/) and Claude that researches a topic, drafts an executive brief, and audits it for unsupported claims before writing the final result to `executive_brief.md`.

The demo topic is **data center energy constraints and PG&E grid capacity upgrades in Northern California**, but the topic lives in the agent goals and task descriptions in `main.py` and can be swapped for anything.

## How it works

Three agents run in sequence, each handing its output to the next:

| Agent | Role | What it does |
|-------|------|--------------|
| **Researcher** | Lead Infrastructure Researcher | Gathers key facts, timelines, and risks, and labels anything it is unsure of |
| **Writer** | Executive Communications Director | Turns the research into a one-page executive brief (headline, findings, risks, actions) |
| **Auditor** | Compliance and Quality Evaluation Engine | Reviews the brief for formatting, tone, and data integrity, and removes or flags unsupported claims |

```
Research task  ->  Writing task  ->  Audit task  ->  executive_brief.md
 (Researcher)       (Writer)          (Auditor)
```

The writer receives the researcher's output as context. The auditor receives both the research and the draft, so it can check each claim in the brief against what the researcher actually reported.

## Tech stack

- Python 3.10+ (developed on 3.13)
- [CrewAI](https://github.com/crewAIInc/crewAI) for agent and task orchestration
- Anthropic Claude (`claude-sonnet-5-5`) as the LLM
- `python-dotenv` for loading the API key from a local `.env` file

## Setup

1. Clone the repo and enter the folder:
   ```bash
   git clone https://github.com/akshath-prakash/mis-autonomous-agent.git
   cd mis-autonomous-agent
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Add your Anthropic API key. Copy the example file and edit it:
   ```bash
   cp .env.example .env
   ```
   Then open `.env` and set `ANTHROPIC_API_KEY` to your key from [console.anthropic.com](https://console.anthropic.com). The `.env` file is listed in `.gitignore` and must never be committed.

## Run

```bash
python main.py
```

The run takes about one to three minutes. The terminal streams each agent's activity, and the final brief is saved to `executive_brief.md`. CrewAI may ask at the end whether to share an execution trace; answering no is fine and nothing is required.

A sample output is included in this repo as `executive_brief.md`.

## Design notes and limitations

- **No live data.** The researcher agent has no web search tool, so it answers from the model's built-in knowledge. Figures about PG&E and the Bay Area grid may be outdated or wrong. The task prompts tell the agents to flag uncertainty, and the sample brief marks unverified items with *(verify)*. Treat the output as a demonstration of the workflow, not a verified research report.
- **The auditor is a prompt-based check, not a guarantee.** It reduces unsupported claims but cannot independently verify facts without external sources.
- **Sequential process.** Tasks run one after another so each stage can build on the previous one.

## Security practices

- The API key lives only in a local `.env` file, which is excluded from version control.
- `.env.example` contains a placeholder, not a real key.
- If a key is ever exposed, delete it in the Anthropic console and create a new one.

## Possible extensions

- Give the researcher a web search tool so findings cite live sources.
- Add a source-citation requirement and have the auditor reject any claim without one.
- Parameterize the topic through a command-line argument.
- Log token usage and cost per run.

## Screenshots

![Agents running in the terminal](docs/terminal-run.png)
![Generated executive brief](docs/executive-brief.png)
