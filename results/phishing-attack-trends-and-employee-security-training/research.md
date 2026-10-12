# Research Summary: Phishing Attack Trends and Employee Security Training

**Method note:** I had no live web or database access for this task. Everything below comes from my background knowledge of published reports, which may be incomplete or out of date. Each item carries a confidence label:
- **[High]**: well-established and consistently reported
- **[Medium]**: I'm fairly sure of the substance, but exact figures or wording should be verified
- **[Low/Unverified]**: vendor claims, uncertain recall, or projections

I have deliberately left out figures I couldn't recall reliably.

---

## 1. Current Phishing Attack Trends

**Prevalence and impact**
- Phishing remains one of the top initial access vectors for breaches and fraud. **[High]**
- **Verizon DBIR** consistently attributes a majority of breaches to the "human element" (error, misuse, stolen credentials, social engineering). Recent editions put it in roughly the 60–75% range, and the figure varies by edition and methodology. **[Medium]** Check the exact percentage for the edition you cite.
- **IBM Cost of a Data Breach** reports in recent years list phishing among the most common initial vectors, at roughly 15–16% of breaches, with average breach costs in the ~$4.4–4.9M range. **[Medium]** Verify the edition year and figures.
- **FBI IC3** reports phishing/spoofing among the most-reported complaint categories. Business Email Compromise (BEC) accounts for billions of dollars in annual reported losses (on the order of $2–3B per year). **[Medium]** Exact counts and dollar figures vary by year, so verify.
- **APWG** reported record phishing volumes around 2022 (roughly 4.7M attacks in a year). Quarterly counts since have fluctuated. **[Medium for 2022 record; Low for later quarterly figures]**

**Technique shifts**
- **AI-enabled phishing:** Generative AI is improving grammar, localization, and personalization, which removes the old "bad spelling" red flag. **[High on direction]** Some vendors claim huge percentage increases in phishing since ChatGPT's release (e.g., "over 1,000%"). **[Low/Unverified]** These are vendor-sourced with unclear methodology, so don't cite them as fact.
- **Deepfake voice/video fraud:** There are documented cases, including a widely reported 2024 Hong Kong case involving a roughly $25M transfer after a deepfake video call. **[Medium]** The scale of the broader trend is **[Unknown]**.
- **Adversary-in-the-middle (AiTM) and phishing-as-a-service kits** (e.g., Evilginx-style tooling, EvilProxy, Tycoon 2FA) bypass SMS/app-based MFA by stealing session tokens. **[High]**
- **QR-code phishing ("quishing")** evades link scanners and moves the victim to unmanaged mobile devices. **[High]**
- **Vishing and help-desk social engineering** (e.g., Scattered Spider–style attacks, the 2023 MGM incident) are growing. **[Medium–High]**
- **Callback/TOAD phishing**, **smishing**, **MFA-fatigue/push-bombing**, **OAuth consent phishing**, and **"ClickFix"-style fake-CAPTCHA/paste-a-command lures** (rising from about 2024) are all active. **[Medium]**
- **Abuse of legitimate services** (shared documents, e-signature platforms, cloud storage, compromised accounts) makes detection harder. **[High]**

---

## 2. State of Employee Security Training

**Common practice**
- Typical programs combine annual or periodic awareness modules with simulated phishing campaigns and, increasingly, "just-in-time" or embedded training after a failed simulation. **[High]**
- Industry framing has moved from "awareness" toward "human risk management" or "security behavior and culture programs." **[Medium]** This is partly vendor and analyst marketing.

**Evidence on effectiveness (important and contested)**
- A large 2025 study (UC San Diego Health, ~19,500 employees, presented at IEEE S&P) found that annual training and embedded post-click training had very small or statistically insignificant effects on phishing failure rates. **[Medium]** Verify the exact sample size and effect size before quoting.
- An earlier ETH Zurich field study (2022) found embedded training could be ineffective or even counterproductive in some cases. **[Medium]**
- Vendor-reported improvements (e.g., click rates falling from X% to Y%) are widely marketed, but they are generally not peer-reviewed and often measure simulation click rates, not real-world incident reduction. **[High confidence that the caveat applies; figures Unverified]**
- Employee **reporting rates** (not just click rates) are increasingly recommended as a more meaningful metric. **[Medium]**
- DBIR data has shown that many users click quickly (within about a minute of opening) and that only a minority report. **[Medium]** Exact numbers vary by year, so verify.

---

## 3. Current Constraints

- **Measurement problems:** Click rate is an imperfect proxy. Simulation difficulty varies, so results aren't comparable across companies or vendors. **[High]**
- **Training fatigue and low engagement:** Annual compliance modules often show weak behavior change. **[Medium–High]**
- **Resources:** Budget, staff time, and security-team capacity limit program depth, especially for SMBs. **[High on direction; specific figures Unknown]**
- **Culture and ethics:** Punitive simulations can erode trust and reduce reporting. **[Medium]**
- **Technical limits:** Email filters miss novel or well-crafted lures. Legacy MFA is phishable. Attacks increasingly arrive outside email (SMS, voice, collaboration tools, QR codes). **[High]**
- **Data limits:** Statistics come from different sources with different definitions (attacks vs. breaches vs. complaints vs. losses), and they are heavily underreported. **[High]** Treat cross-source comparisons cautiously.

---

## 4. Planned and Emerging Developments

- **Phishing-resistant authentication:** Passkeys/FIDO2 and hardware keys are being pushed by CISA guidance and major vendors. Adoption is growing but uneven. **[High on direction; adoption rates Unknown]**
- **Email authentication enforcement:** Google/Yahoo bulk-sender requirements (SPF/DKIM/DMARC) began in 2024. Microsoft announced similar consumer-side requirements in 2025. **[Medium]** Verify dates and scope.
- **Regulatory and compliance drivers:**
  - **PCI DSS v4.0:** Requirement 12.6.3.1 requires training on phishing and social engineering. Future-dated requirements became mandatory on **March 31, 2025**. **[Medium–High]**
  - **EU NIS2:** Requires cyber-hygiene training for management and staff. The transposition deadline was Oct 17, 2024, and national implementation has been uneven. **[Medium]** Check the status per member state.
  - **EU DORA:** Applied from Jan 17, 2025, and includes ICT training expectations for financial entities. **[Medium]**
  - **HIPAA, SEC cyber disclosure rules (Dec 2023), and others** create indirect training and governance pressure. **[Medium]**
- **Training evolution:** More adaptive/personalized training, role-based programs (finance, executives, help desk), simulations of vishing/smishing/deepfakes, easy one-click reporting, and AI-assisted detection plus user nudges. **[Medium]** Much of this is vendor roadmap, and its effectiveness is **[Unproven]**.
- **AI defense:** Vendors are deploying LLM-based email analysis and behavioral detection. Effectiveness against AI-generated lures is **[Unknown/Unverified]**.

---

## 5. Timeline of Key Reference Points

| Date | Event | Confidence |
|---|---|---|
| ~2022 | APWG reports record annual phishing volume | Medium |
| Late 2022 | ChatGPT release; subsequent concern about AI-generated phishing | High |
| 2022 | ETH Zurich embedded-training field study | Medium |
| 2023 | MGM/Caesars social-engineering incidents | Medium–High |
| Dec 2023 | SEC cyber-incident disclosure rules take effect | Medium |
| Early 2024 | Hong Kong deepfake video-call fraud reported | Medium |
| Feb 2024 | Google/Yahoo bulk-sender authentication rules begin | Medium |
| Oct 17, 2024 | NIS2 transposition deadline | Medium |
| Jan 17, 2025 | DORA applies | Medium |
| Mar 31, 2025 | PCI DSS 4.0 future-dated requirements mandatory | Medium–High |
| 2025 | UCSD Health phishing-training efficacy study | Medium |
| 2025 onward | Microsoft consumer-side email authentication requirements | Low–Medium, verify |

---

## 6. Risks

- **Over-reliance on training:** Evidence suggests training alone yields limited risk reduction. Pair it with technical controls (phishing-resistant MFA, DMARC, conditional access, link/attachment sandboxing, least privilege). **[Medium–High]**
- **MFA bypass:** AiTM kits defeat non-phishing-resistant MFA. **[High]**
- **Deepfake and voice impersonation:** Verification procedures for payments and credential resets are often immature. **[Medium]**
- **Third-party and supply-chain phishing:** Attacks via compromised vendor accounts bypass internal training. **[High]**
- **Metric gaming and false assurance:** Low click rates may reflect easy simulations. **[Medium]**
- **Regulatory exposure:** Compliance deadlines may drive checkbox training instead of behavior change. **[Medium]**
- **Employee trust:** Punitive approaches can suppress incident reporting. **[Medium]**

---

## 7. Key Uncertainties and Items Needing Verification

1. Exact figures for DBIR (human-element %, click/report times), IBM (average cost, phishing share), and IC3 (complaint counts, loss totals) by year. I did not state them precisely because I can't confirm them.
2. APWG quarterly and annual counts after 2022. My recall is unreliable.
3. The "% increase in phishing due to AI" claims. They are vendor-sourced and methodology is unclear, so **do not use them without verification**.
4. The real-world scale of deepfake-enabled fraud. Only individual cases are well documented.
5. The actual effect size of training across sectors. The evidence is mixed, with only a few large independent studies.
6. NIS2 national transposition status and enforcement timelines. These are **Unknown** and vary by country.
7. Adoption rates of passkeys/phishing-resistant MFA in enterprises. **Unknown.**
8. Whether "planned developments" from vendors (adaptive training, AI detection) will be delivered or effective. **Unproven.**
9. Anything dated after my knowledge cutoff, including 2025–2026 reports, is likely missing or outdated.

---

## 8. Recommended Next Steps

- Pull the latest **Verizon DBIR, IBM Cost of a Data Breach, FBI IC3 annual report, APWG Phishing Activity Trends, and CISA/ENISA** publications to replace the **[Medium]** figures with confirmed ones.
- Retrieve the primary **UCSD (IEEE S&P 2025)** and **ETH Zurich** papers to confirm the effectiveness findings.
- Confirm regulatory dates and scope against primary sources (PCI SSC, EUR-Lex/national NIS2 laws, DORA texts).
- Treat all vendor-sourced statistics as marketing until their methodology is reviewed.