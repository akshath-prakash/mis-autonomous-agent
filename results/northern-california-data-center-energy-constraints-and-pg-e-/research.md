# Research Summary: Northern California Data Center Energy Constraints and PG&E Grid Upgrades

**Method note:** I had no live web access for this task. Everything below comes from my training knowledge, which has a cutoff and may be out of date. Each item carries a confidence label:
- **[HIGH]** I am confident this is accurate in substance.
- **[MED]** I am fairly sure of the direction, but figures or details may be off.
- **[LOW / UNVERIFIED]** I recall something but am unsure. Do not cite without checking.

I have deliberately left out specific numbers I could not recall reliably.

---

## 1. Context: who serves the data centers

- **[HIGH]** Northern California data center load is split across several utilities, so "PG&E constraints" is only part of the picture.
  - **PG&E** is an investor-owned utility (IOU) serving much of the Bay Area, including most of San Jose, the East Bay, the Peninsula, and the Central Valley/Sacramento-adjacent areas such as Tracy and Stockton.
  - **Silicon Valley Power (SVP)** is the City of Santa Clara's municipal utility. It serves one of the densest data center clusters in the US. It is not PG&E, and it faces its own capacity and import constraints.
  - **SMUD** is the Sacramento municipal utility and a separate, growing data center market.
- **[MED]** Santa Clara and San Jose are the historic core markets. Developers are also looking at the East Bay, the Central Valley, and the Sacramento region because of power and land limits in the core.

## 2. Current constraints

**Grid capacity and interconnection**
- **[HIGH]** Large-load (data center) requests have grown faster than transmission and substation capacity in parts of the Bay Area. Developers report long waits for new service.
- **[MED]** PG&E has publicly described a large pipeline of data center load requests, measured in multiple gigawatts, on earnings calls in 2024–2025.
  - **[LOW / UNVERIFIED]** My recollection is that the figure went from the mid-single-digit GW range to roughly 10 GW across successive quarters. I am not confident of the exact numbers or dates.
  - **[UNCERTAIN]** The pipeline is requests, not firm commitments. The share likely to be built and energized is unknown to me. PG&E has said only a portion is likely to materialize, but I do not remember the figure.
- **[MED]** Reporting in 2024–2025 indicated that some new data center projects in the PG&E territory, especially around San Jose, were being told to expect multi-year waits.
  - **[LOW / UNVERIFIED]** I vaguely recall energization dates in the late 2020s to early 2030s for some projects. I cannot cite a specific source or date, so please verify.
- **[MED]** Substation and transmission lead times (equipment such as large transformers, permitting, and CEQA review) are a major bottleneck. Transformer supply chain tightness is a national issue.

**Cost and rates**
- **[HIGH]** California IOU retail rates, including PG&E's, are among the highest in the US. This makes cost allocation for new large loads politically sensitive.
- **[MED]** There is an active policy concern that existing ratepayers could bear grid-upgrade costs driven by data centers.
- **[MED]** PG&E leadership has argued publicly that large-load growth can spread fixed costs and put downward pressure on rates.
  - **[LOW / UNVERIFIED]** The exact claimed magnitude (a percentage per year) is something I do not recall reliably.
  - Regulators and consumer advocates dispute this argument.

**Reliability and supply**
- **[HIGH]** Diablo Canyon nuclear plant (PG&E territory) has had its operation extended by state law (SB 846) beyond the original retirement dates, to roughly 2029–2030.
  - **[UNCERTAIN]** I am not sure of the current status of federal NRC license renewal and related approvals.
- **[HIGH]** The January 2025 Moss Landing battery storage fire (Vistra facility) removed a large block of storage in the PG&E area. It raised scrutiny of battery siting and safety.
  - **[UNCERTAIN]** I do not know the current effect on capacity or the recovery timeline.
- **[MED]** California's grid has historically been tight during summer evening peaks and heat events. Data center load growth adds to long-term resource adequacy needs.

**Environmental and permitting**
- **[MED]** Backup diesel generators at data centers are subject to Bay Area Air Quality Management District (BAAQMD) permitting. This is a recurring friction point.
  - **[UNCERTAIN]** I am not sure of the current regulatory changes or specific cases.
- **[MED]** Land and local permitting constraints in Santa Clara and San Jose also limit new builds, independent of power.

## 3. Planned developments and PG&E / regulatory responses

- **[MED]** **Large-load interconnection reform.** PG&E has proposed or pursued a more structured process for transmission-level, large-load customers, including cluster-style studies and requirements for financial commitments, aimed at filtering speculative requests. This is associated with PG&E "Electric Rule 30" and a CPUC proceeding.
  - **[UNCERTAIN]** I am not confident of the rule number, the proceeding docket number, or the current status (proposed vs. approved). Verify at the CPUC.
- **[MED]** **Transmission planning.** The CAISO annual Transmission Planning Process (TPP) has approved multiple Bay Area and PG&E-area upgrades in recent cycles (2022–23, 2023–24, 2024–25 plans).
  - **[UNCERTAIN]** I cannot reliably name which specific projects target data center load vs. general growth, or their cost and in-service dates. Check CAISO's TPP documents.
- **[MED]** **PG&E capital plan.** PG&E has a large multi-year capital program covering substations, transmission, and distribution. Some of it is attributable to load growth.
  - **[UNCERTAIN]** I do not have a reliable dollar figure for the load-growth portion.
- **[LOW / UNVERIFIED]** **State legislation (2025 session).** I recall bills about data center energy use and tariffs, including SB 57 (Padilla), SB 58 (Padilla), and AB 222 (Bauer-Kahan). I do not remember which passed, were amended, vetoed, or held. **Do not rely on my recollection here.**
- **[MED]** **Alternative power strategies.** Developers in the region are exploring on-site generation (fuel cells such as Bloom Energy, gas turbines), battery storage, and flexible or curtailable load arrangements to speed up interconnection.
  - **[UNCERTAIN]** I cannot confirm specific current projects or approvals.
- **[LOW / UNVERIFIED]** Geographic shift to the Central Valley, the Sacramento region (SMUD), and other regions is plausible and reported, but I cannot give specific project names or capacities with confidence.

## 4. Timelines (what I can and cannot say)

| Item | Timeline | Confidence |
|---|---|---|
| Diablo Canyon extended operation | To about 2029–2030 under state law | [HIGH] on the general range; federal licensing status [UNCERTAIN] |
| New large data center energization in constrained PG&E Bay Area areas | Multi-year waits; possibly late 2020s to 2030s | [LOW / UNVERIFIED] on specific dates |
| Typical substation or transmission upgrade lead time | Several years (often 5+ for major transmission) | [MED], general industry knowledge |
| PG&E large-load rule reform | Under CPUC review or implementation | [UNCERTAIN] on stage and dates |
| CAISO TPP approvals | Annual cycle, with plans typically approved in spring | [MED] |

## 5. Key risks

- **Speculative demand:** The pipeline may be inflated by duplicate or speculative requests, which could lead to overbuilding of grid assets or to misjudged timelines. [MED]
- **Cost shifting to ratepayers:** If projects are canceled after upgrades are funded, stranded costs could fall on other customers. Regulators are addressing this through financial-commitment requirements. [MED]
- **Reliability:** Peak-demand stress, wildfire-related outages and Public Safety Power Shutoffs (PSPS) in PG&E territory, and storage or generation outages. [MED to HIGH]
- **Wildfire liability and PG&E financial health:** These affect PG&E's capital costs and ability to fund upgrades. PG&E emerged from bankruptcy in 2020. [HIGH] on the history; [UNCERTAIN] on current credit conditions.
- **Supply chain:** Transformers, switchgear, and breakers have long lead times. [MED]
- **Policy and political risk:** Possible state-level restrictions, tariffs, or reporting mandates on data centers. [UNCERTAIN] on the current legislative state.
- **Siting and environmental risk:** Air permits for backup generation, local opposition, and water use. [MED]
- **Demand-forecast uncertainty:** AI-driven load growth projections vary widely. A slowdown in AI investment would sharply change the need. [MED]

## 6. Items I could not confirm (do not cite without verification)

1. Exact current size of PG&E's data center pipeline (GW), and the share considered firm.
2. Specific energization dates for named projects or areas.
3. Specific CAISO-approved projects tied to Silicon Valley or data center load, and their costs and in-service dates.
4. Status and docket of the CPUC proceeding on large-load interconnection (Rule 30 or similar).
5. Outcomes of 2025 California data center bills (SB 57, SB 58, AB 222).
6. SVP and SMUD current capacity limits, moratoria, or pipeline numbers.
7. Current status of Moss Landing and Diablo Canyon federal licensing.
8. PG&E's claimed rate-impact figures from load growth.

## 7. Recommended primary sources for verification

- PG&E quarterly earnings call transcripts and investor presentations (pipeline GW figures)
- CPUC docket search (large-load interconnection and Rule 30; PG&E General Rate Case)
- CAISO Transmission Plan documents (2023–24 and 2024–25 and later)
- California Energy Commission (CEC) Integrated Energy Policy Report (IEPR) demand forecasts
- California Legislative Information site (bill status for SB 57, SB 58, AB 222)
- SVP and SMUD board and city council documents
- Local news (San Jose Spotlight, SF Chronicle, Bloomberg, Data Center Dynamics) for project-level reporting