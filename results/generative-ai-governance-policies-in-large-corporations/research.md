# Research Summary: Generative AI Governance Policies in Large Corporations

**Method and reliability note:** This summary comes from my training knowledge. I had no live web or database access for this task. I did not invent statistics. Where I recall a figure but can't verify it, I mark it. Anything dated late 2025 or later should be verified before use.

**Confidence labels:** [HIGH] well established, [MED] I believe this is correct but it should be checked, [LOW/UNSURE] uncertain or possibly outdated.

---

## 1. Current constraints (what shapes corporate policy today)

### A. Regulatory and legal
- **EU AI Act** [HIGH on structure, MED on exact dates]
  - Entered into force 1 Aug 2024, with phased application.
  - Prohibited practices and AI-literacy obligations applied from 2 Feb 2025.
  - General-purpose AI (GPAI) model obligations applied from 2 Aug 2025. A GPAI Code of Practice was published around July 2025 [MED].
  - Most high-risk system obligations and transparency duties are scheduled for 2 Aug 2026. High-risk AI embedded in regulated products is scheduled for 2 Aug 2027.
  - Maximum fines are up to €35M or 7% of global turnover for prohibited practices. Lower tiers apply to other breaches (I recall €15M/3%) [MED].
  - **[LOW/UNSURE]** The European Commission's "Digital Omnibus" proposal (late 2025) reportedly seeks to delay or soften some high-risk deadlines. I don't know whether it has been adopted, so the 2026 dates may shift.
- **United States** [MED overall; the landscape changes quickly]
  - There is no comprehensive federal AI statute.
  - Biden's EO 14110 (Oct 2023) was rescinded in Jan 2025. The current approach emphasizes deregulation and an AI Action Plan (July 2025).
  - **[LOW/UNSURE]** I recall a late-2025 executive action aimed at challenging or preempting state AI laws. Its details and legal durability need verification.
  - State laws are creating a patchwork:
    - Colorado AI Act (SB 24-205) covers high-risk or "consequential decision" systems. Its effective date was delayed to 30 June 2026 [MED], and further changes are possible.
    - California has frontier-model transparency (SB 53) and training-data transparency (AB 2013), both effective around Jan 2026 [MED].
    - Texas TRAIGA is effective around Jan 2026 [MED].
    - NYC Local Law 144 (automated hiring tools) has been enforced since 2023 [HIGH].
  - The SEC has brought "AI-washing" enforcement actions, such as the March 2024 cases against Delphia and Global Predictions [HIGH]. This is relevant to corporate AI disclosures.
- **China:** Interim Measures for Generative AI Services took effect Aug 2023 [HIGH]. AI-generated content labeling rules took effect around Sept 2025 [MED].
- **Other:**
  - The UK uses a principles-based, regulator-led approach with no omnibus AI law [MED].
  - Singapore issued a Model AI Governance Framework for Generative AI (2024) [MED].
  - South Korea's AI Basic Act is slated to take effect around Jan 2026 [LOW/UNSURE].
- **Existing laws applied to GenAI:**
  - Data protection (GDPR and similar). Italy's regulator fined OpenAI €15M in Dec 2024 [MED].
  - Copyright, where litigation is ongoing. NYT v. OpenAI is pending. A reported ~$1.5B Anthropic authors' settlement (2025) [MED]. Getty v. Stability AI in the UK [LOW on outcome details].
  - Consumer protection and liability. In the Air Canada chatbot case (Moffatt, 2024), the company was held responsible for its chatbot's statements [HIGH].
  - Sector rules: financial model-risk guidance (e.g., SR 11-7), EU DORA (applicable Jan 2025), and healthcare/HIPAA.

### B. Standards and frameworks (voluntary but widely referenced)
- **NIST AI RMF 1.0** (Jan 2023) and the **Generative AI Profile, NIST AI 600-1** (July 2024) [HIGH].
- **ISO/IEC 42001:2023** (AI management system), which is certifiable [HIGH]. **ISO/IEC 23894** covers AI risk management [HIGH].
- **OECD AI Principles** and the **G7 Hiroshima Code of Conduct** [HIGH, but they are high-level].

### C. Typical internal corporate controls (observed patterns)
- **Policy evolution** [HIGH on the pattern, MED on specifics]: Many firms went from blanket bans in 2023 to governed enterprise deployment.
  - Reported early restrictions: Samsung (after an internal code leak, ~May 2023), Apple, JPMorgan, Amazon, Verizon, Deutsche Bank.
  - Later practice: approved-tool lists and enterprise-licensed tools with no-training and data-retention terms.
- **Common policy elements:**
  - Acceptable-use policy and approved-tool lists.
  - Data classification rules (no confidential, personal, or regulated data in unapproved tools).
  - Human review of outputs for consequential uses.
  - Cross-functional AI governance committee or review board (legal, security, privacy, risk, HR, business).
  - AI use-case and model inventory with risk tiering.
  - Third-party and vendor due diligence, including contractual IP indemnities. Vendors such as Microsoft, Google, Adobe, and OpenAI offer copyright indemnity programs [HIGH].
  - Mandatory employee training, partly driven by the EU AI Act's AI-literacy duty.
  - Logging and monitoring, incident response, and disclosure to customers or employees where AI is used.
- **Governance roles:** Growing use of Chief AI Officer or equivalent roles, and board-level oversight [MED]. I have no verified adoption percentage.

### D. Practical constraints
- **Shadow AI:** Employees use unsanctioned tools. I recall the Microsoft/LinkedIn Work Trend Index (2024) reporting that a large majority (~75–80%) of AI users bring their own tools to work [LOW/UNSURE on exact figure; verify].
- **Technical and security:** data leakage, prompt injection, hallucination, model/vendor opacity, and difficulty auditing third-party models.
- **Capability gaps:** shortage of AI-risk expertise, unclear ownership between legal, IT, and the business, and tooling immaturity.
- **Cross-border complexity:** multinationals must reconcile EU, US-state, and Chinese requirements, and often adopt the strictest standard globally.

---

## 2. Planned or anticipated developments

| Item | Timing | Confidence |
|---|---|---|
| EU AI Act high-risk and transparency obligations | Scheduled Aug 2026 (embedded products Aug 2027) | MED; possible delay via Digital Omnibus (status UNSURE) |
| Colorado AI Act effective | 30 June 2026 | MED; further amendment or delay possible |
| California and Texas AI laws | ~Jan 2026 | MED |
| EU harmonized standards (CEN-CENELEC) supporting AI Act | Delayed; timing UNSURE | LOW |
| Agentic AI governance (agent identity, permissions, audit trails, kill switches) | Emerging 2025–2026; no settled standard | MED on trend, LOW on specifics |
| ISO 42001 certification uptake | Ongoing | MED on trend; no verified adoption count |
| US federal preemption or federal framework | Uncertain | LOW |
| Ongoing copyright litigation outcomes | Rolling, unpredictable | LOW |

Other expected trends, all MED/LOW and directional only:
- Shift from policy documents to automated enforcement (AI gateways, DLP, and monitoring tooling).
- Greater use of AI content provenance and labeling (e.g., C2PA).
- Rising AI-specific contract clauses and insurance considerations.
- Risk-tiered governance replacing blanket policies.

---

## 3. Key risks

- **Regulatory and compliance:** Fragmented, shifting rules, with a risk of over- or under-compliance if dates move. EU penalties are large.
- **Data and privacy:** Leakage of trade secrets or personal data through public tools, and cross-border transfer issues.
- **IP:** Infringement exposure from outputs, unclear ownership of AI-generated work, and training-data provenance.
- **Accuracy and liability:** Hallucinations in customer-facing or decision-making contexts, with precedent that companies are responsible for their AI's statements.
- **Bias and discrimination:** Particularly in HR, lending, and insurance uses.
- **Security:** Prompt injection, supply-chain and plugin risks, and agentic systems acting beyond intended permissions.
- **Reputational and disclosure:** AI-washing claims and public incidents.
- **Governance:** Shadow AI, unclear accountability, policy lagging technology, and "paper compliance" without enforcement.
- **Vendor concentration:** Dependence on a few model providers, and contract and change-management risk when models are updated.

---

## 4. Explicit uncertainties and data gaps

- **No verified quantitative data** here on the percentage of large companies with formal GenAI policies, governance committees, or Chief AI Officers. Survey figures exist from Gartner, McKinsey, Deloitte, and IBM, but I can't reliably quote them, so I omitted them.
- **No verified data** on fines or enforcement actions under the EU AI Act, because enforcement is still early [LOW].
- **Unverified post-2025 developments:** Digital Omnibus outcome, US federal preemption, the South Korea timeline, and any 2026 legislative changes.
- **Company-specific policies** (e.g., which firms ban or allow which tools) change often, and my examples may be outdated.
- **Cost, headcount, and budget figures** for AI governance programs: unknown, not estimated.

---

## 5. Recommended verification steps
1. Check the EU Commission and AI Office pages for the current AI Act timeline and Digital Omnibus status.
2. Check the Colorado, California, and Texas legislature pages, and law-firm trackers (IAPP, Mayer Brown, and similar) for state-law updates.
3. Pull the latest surveys (Gartner, McKinsey State of AI, IBM, Deloitte, KPMG) for adoption statistics, and cite the dates.
4. Review company 10-K risk-factor disclosures to see how large firms describe AI governance.
5. Confirm the status of the major copyright cases through court dockets.