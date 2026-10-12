# Research Summary: CCPA/CPRA Compliance for California Businesses

**Knowledge caveat:** This is based on my training knowledge, which has a cutoff and may not reflect the latest regulatory changes, settlements, or bills. Confidence labels:
- **[HIGH]** = well established
- **[MED]** = I believe this is correct but exact figures or dates should be verified
- **[LOW/UNSURE]** = uncertain, may be outdated, or I cannot confirm it

---

## 1. Legal Framework (Current State)

- **[HIGH]** The California Consumer Privacy Act (CCPA, AB 375) was enacted in 2018 and operative Jan 1, 2020. AG enforcement began July 1, 2020.
- **[HIGH]** The California Privacy Rights Act (CPRA, Proposition 24) was approved by voters in Nov 2020. It amended the CCPA and created the California Privacy Protection Agency (CPPA). Most amendments became operative **Jan 1, 2023**, with a lookback to personal information collected from **Jan 1, 2022**.
- **[HIGH]** Enforcement is shared by the **California Attorney General** and the **CPPA** (civil and administrative enforcement).
- **[HIGH]** Regulations are issued by the CPPA (formerly the AG). The first CPPA regulations were finalized in March 2023.
- **[HIGH]** Enforcement-timing litigation: a trial court in 2023 delayed enforcement of the CPPA's regulations until March 2024. The Court of Appeal reversed in Feb 2024, so the regulations are enforceable now. Statutory CPRA provisions have been enforceable since July 1, 2023.

## 2. Who Is Covered

A for-profit entity doing business in California that meets **any one** of these:
- **[HIGH]** Annual gross revenue above a threshold, originally **$25M**. **[MED]** The CPPA adjusted it for inflation in early 2025 to about **$26.6M**; verify the exact figure.
- **[HIGH]** Buys, sells, or shares personal information of **100,000+** California consumers or households (the CPRA raised this from 50,000).
- **[HIGH]** Derives **50%+** of annual revenue from selling or sharing personal information.
- **[HIGH]** Also covered: entities that control or are controlled by a covered business and share common branding and consumer data, and certain joint ventures (40%+ ownership by covered businesses).
- **[HIGH]** The employee/HR data and B2B contact data exemptions **expired Jan 1, 2023**, and legislative extensions failed. Covered businesses must therefore treat employee, applicant, contractor, and B2B contact data as in scope.
- **[HIGH]** Common exemptions are data governed by HIPAA/CMIA (PHI), GLBA, FCRA, and DPPA, plus publicly available information. These are mostly data-level or entity-level carve-outs with nuances. Nonprofits are generally not covered. **[UNSURE]** The precise scope of the exemptions needs counsel review case by case.

## 3. Core Obligations (Current Constraints)

**Consumer rights [HIGH]:**
- Know/access, delete, correct (new under the CPRA), and data portability.
- Opt out of sale **and sharing** (cross-context behavioral advertising).
- Limit use and disclosure of **sensitive personal information**.
- Non-discrimination/non-retaliation.

**Business duties [HIGH unless noted]:**
- Notice at collection, and a privacy policy updated at least every 12 months.
- "Do Not Sell or Share My Personal Information" and "Limit the Use of My Sensitive Personal Information" links (or an alternative opt-out link).
- Honor **opt-out preference signals** such as Global Privacy Control (GPC).
- Data minimization, purpose limitation, and retention disclosure.
- Contract requirements with service providers, contractors, and third parties.
- "Reasonable security" obligations.
- Opt-in consent for sale/sharing of data of consumers under 16 (parental consent under 13).
- Avoid "dark patterns" in consent flows (the regulations set symmetry-in-choice rules).
- Training for staff who handle requests, and recordkeeping (**[MED]** 24 months for request records).

**Response timelines:**
- **[MED]** Confirm receipt within 10 business days.
- **[HIGH]** Respond within 45 days, extendable by another 45.
- **[MED]** Process opt-out/limit requests within 15 business days.

## 4. Penalties and Liability

- **[HIGH]** Administrative/civil penalties are **$2,500 per violation** and **$7,500 per intentional violation or violation involving minors under 16**, with the statute's CPI adjustments. **[MED]** The 2025 adjusted figures are about $2,663 and $7,988; verify.
- **[HIGH]** The **private right of action** applies only to certain **data breaches** (Civ. Code §1798.150): statutory damages of **$100–$750 per consumer per incident**, or actual damages. It requires a 30-day cure notice. The CPRA added email address plus password or security question to the covered data types.
- **[HIGH]** The CPRA removed the mandatory 30-day cure period for administrative enforcement. Whether to allow cure is now at the CPPA's or AG's discretion.
- **[HIGH]** Per-violation counting means exposure can scale with the number of consumers affected.

## 5. Enforcement Landscape (Precedents)

Settlement amounts are from memory; verify against the AG and CPPA press releases.
- **[HIGH]** Sephora (AG, Aug 2022): $1.2M. Failure to disclose sale and failure to honor GPC.
- **[MED]** DoorDash (AG, Feb 2024): about $375K, over marketing cooperative data sharing.
- **[MED]** Tilting Point Media (AG and LA City Attorney, 2024): about $500K, children's data.
- **[MED]** Honda (CPPA, 2025): about $632K. Issues cited included asymmetric opt-out choices and excessive verification demands.
- **[MED]** Todd Snyder (CPPA, 2025): about $345K. Opt-out mechanism problems.
- **[MED]** Healthline Media (AG, mid-2025): about $1.55M, reported as the largest CCPA settlement at that time.
- **[LOW/UNSURE]** Additional 2025 actions (for example Tractor Supply, Sling TV) and the amounts reported for them. I cannot confirm the details; check current sources.
- **[MED]** Recurring themes: failure to honor opt-out signals (GPC), broken or confusing opt-out mechanisms, over-collection for verification, deficient vendor contracts, and children's data.
- **[LOW/UNSURE]** Reported multi-state coordinated GPC sweeps in 2025. Verify.
- **[MED]** CPPA leadership has changed. Tom Kemp is reported as executive director in 2025, succeeding Ashkan Soltani. Verify.

## 6. Planned and Recent Developments (Timelines)

**A. CPPA regulations on risk assessments, cybersecurity audits, and automated decision-making technology (ADMT)**
- **[MED]** Formal rulemaking ran through 2024–2025. The CPPA board adopted the final package in mid-2025, and the Office of Administrative Law approved it around **Sept 2025**, with an effective date of **Jan 1, 2026**.
- **[MED]** Phase-in dates as I recall them (verify against the final text):
  - **Risk assessments:** required for high-risk processing (selling/sharing, sensitive PI, certain ADMT uses, and others). Requirements apply from Jan 1, 2026. Assessments for pre-2026 activities are due by about the end of 2027, and attestations/summaries are submitted to the CPPA by about **April 1, 2028**.
  - **ADMT:** compliance for covered "significant decisions" (such as lending, housing, education, employment, healthcare) by about **Jan 1, 2027**. This includes pre-use notice, opt-out, and access rights.
  - **Cybersecurity audits** (independent, annual), phased by revenue: about **April 1, 2028** (over ~$100M), **2029** ($50–100M), **2030** (under $50M).
- **[LOW/UNSURE]** The exact thresholds, definitions (scope narrowed during rulemaking compared with earlier drafts), and dates.

**B. Delete Act (SB 362) and data brokers**
- **[MED]** The CPPA's **DROP** (Delete Request and Opt-out Platform) opens to consumers around **Jan 1, 2026**. Registered data brokers must begin processing deletion requests from it around **Aug 1, 2026**, at recurring intervals (about every 45 days).
- **[MED]** Penalties include per-day fines (about $200/day) for non-registration and for unprocessed deletion requests.

**C. Other California legislation**
- **[MED]** AB 1008 (2025) clarifies that personal information can exist in AI systems.
- **[MED]** Neural data was added as sensitive PI (SB 1223).
- **[MED]** AB 566 (2025) requires browsers to offer a built-in opt-out preference signal, with an operative date around **Jan 1, 2027**.
- **[LOW/UNSURE]** Age-signal legislation (AB 1043), data broker amendments (SB 361), and bills curbing CIPA litigation (SB 690). I cannot confirm final status or effective dates.

**D. Federal and other**
- **[UNSURE]** No comprehensive federal privacy law exists. Prior attempts (such as the APRA) stalled. Federal preemption of the CCPA is a possibility but not predictable.
- **[UNSURE]** Future CPPA rulemaking on other topics is possible; the board's agenda changes.

## 7. Key Risks

1. **Opt-out signal handling (GPC) and cookie/tracker configuration:** the most frequent enforcement theme.
2. **Vendor/ad-tech contracts:** missing required contractual terms can turn a "service provider" relationship into a "sale/share."
3. **Employee/HR and B2B data:** often overlooked since the exemptions expired.
4. **Data breach class actions:** statutory damages of $100–$750 per consumer scale quickly.
5. **Parallel litigation (CIPA wiretapping/pen-register claims over website trackers):** not CCPA, but a major related exposure. **[MED]** The status of reform efforts is uncertain.
6. **AI/ADMT:** new obligations phasing in 2026–2027. Compliance programs will need inventories, risk assessments, and opt-out/access mechanisms.
7. **Minors' data:** heightened penalties and opt-in requirements. **[MED]** The California Age-Appropriate Design Code has been subject to ongoing litigation (NetChoice v. Bonta); its status is uncertain.
8. **Regulatory uncertainty:** thresholds adjust for CPI, the regulations are evolving, and enforcement priorities shift.

## 8. Summary of Key Open Questions (Verification Needed)

- Exact current revenue threshold and penalty amounts after CPI adjustment.
- Final text and effective dates of the risk assessment, cybersecurity audit, and ADMT regulations.
- Complete list and amounts of 2025–2026 enforcement actions.
- Status of the 2025–2026 bills (AB 566, AB 1043, SB 361, SB 690).
- Whether the Delete Act DROP timeline held as planned.
- Any litigation challenging the new regulations.

## 9. Recommended Primary Sources

- California Legislative Information (Civ. Code §1798.100 et seq.)
- CPPA website (cppa.ca.gov): regulations, board meeting materials, enforcement advisories
- California AG privacy page (oag.ca.gov/privacy/ccpa), for settlements
- California Office of Administrative Law, for regulation approvals