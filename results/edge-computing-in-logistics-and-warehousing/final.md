# Executive Brief: Edge Computing in Logistics and Warehousing

**Audience:** Senior Leadership
**Basis:** Desk research from background knowledge. No live sources were consulted and no figures were independently verified. Items marked **[VERIFY]** need confirmation before use in decisions.

---

## Headline Takeaway

Edge computing is a candidate infrastructure layer for warehouse robotics, computer vision, and cold-chain monitoring. The case rests on **latency, resilience to connectivity loss, and bandwidth savings**. The business case is **unproven**. We lack verified ROI, payback, and adoption data. We recommend **targeted, evidence-gated pilots** rather than broad rollout.

## Key Findings

- **Where edge fits:**
  - Real-time robotics (AMRs, sortation).
  - Vision-based safety and quality checks.
  - Yard and gate OCR.
  - In-vehicle telematics.
  - Local alerting where connectivity is weak.
  - Use cases exist across these areas, but adoption levels vary and have not been quantified.
- **Why it matters:**
  - Robotics and safety systems need low latency, and cloud round-trips can be a limiting factor.
  - Processing video locally reduces bandwidth.
  - Local processing also keeps worker video on-site.
- **Biggest practical barriers:**
  - Unreliable in-building connectivity (metal racking, large floors). Performance varies widely by site.
  - Poor interoperability among multi-vendor robots and legacy WMS/PLC systems. Standards exist, but their adoption is uneven **[VERIFY current adoption]**.
  - Difficulty patching and managing large fleets of dispersed, heterogeneous devices. This is widely reported as a pain point (medium confidence).
  - A shortage of staff who combine OT, networking, ML, and DevOps skills (medium confidence).
- **Economics:**
  - Upfront costs (hardware, network upgrades, integration) are substantial.
  - Payback depends heavily on volume and labor costs.
  - We have no reliable payback figure. Published payback figures are mostly vendor-sourced.
  - Market-size estimates vary enormously by research firm and definition. Neither should be relied on without a primary methodology.
- **Technology trajectory:**
  - Edge AI hardware is becoming more efficient.
  - 5G-Advanced is emerging, and Wi-Fi 7 products have begun entering the market. Enterprise warehouse adoption pace is **[VERIFY]**.
  - Private 5G rollouts have reportedly been slower than early forecasts (medium confidence).
  - Production maturity of small language and vision-language models at the edge in logistics is **[VERIFY]**.

## Key Risks

- **Cybersecurity:** Many hard-to-patch devices widen the attack surface. A compromised robot or gateway could disrupt operations or pivot into IT networks.
- **Physical safety:** Faulty edge inference, such as a missed pedestrian, could cause harm. Certifying AI safety components remains difficult.
- **Operational:** Failed fleet-wide updates, model drift (as packaging, lighting, or product mix changes), and hardware failures in harsh environments.
- **Financial:** Retrofit and integration cost overruns, and stranded assets if a vendor exits or changes platform.
- **Regulatory (relevant if EU-exposed; all dates medium confidence, [VERIFY]):**
  - **Cyber Resilience Act:** Affects connected-device makers and possibly integrators. Reporting obligations are expected around Sept 2026 and main obligations around Dec 2027.
  - **Machinery Regulation (2023/1230):** Expected to apply from around Jan 2027.
  - **AI Act:** High-risk obligations were originally scheduled for around Aug 2026, but delays have been discussed. The current schedule is uncertain. Worker-monitoring and safety-component uses could be affected.
  - **NIS2:** Logistics and transport are covered sectors. National implementation status varies.
  - **Other jurisdictions:** US (federal and state, including biometric and worker-surveillance laws), UK, and APAC rules have **not been researched**.
- **Privacy and labor:** Video and productivity monitoring raise worker-privacy, labor-relations, and legal concerns. Rules vary by jurisdiction.
- **Supply chain:** Dependence on a few accelerator suppliers, with possible shortages or export-control impacts. Current supply situation is **[VERIFY]**.
- **Strategic:** Over-investing at the edge where cloud processing would suffice. Not every workload needs the edge.

## Known Evidence Gaps

- No verified market-size, adoption-rate, ROI, or cost-per-site figures.
- No verified case studies with measured outcomes.
- Vendor product roadmaps (hyperscalers, NVIDIA, robotics vendors) may have changed.
- Regional coverage is thin (China, India, Southeast Asia, Latin America are not addressed). Last-mile, ocean, and air-freight use cases are less covered.

## Recommended Actions

*These are management recommendations drawn from the findings. They are not research-verified facts.*

1. **Pilot, don't scale.**
   - Select 1–2 high-value use cases at a single site, such as package dimensioning or damage detection.
   - Define throughput, downtime, and labor-hour targets.
   - Treat safety-critical vision (e.g., forklift-pedestrian detection) with extra caution given AI safety certification difficulty.
2. **Validate the business case.** Obtain named case studies with measured outcomes. Cross-check at least 2–3 independent market sources. Interview operators and integrators.
3. **Make security and fleet management prerequisites.** Require secure update and rollback, network segmentation, and OT/IT governance before deployment.
4. **Protect flexibility.** Favor open standards (VDA 5050, OPC UA, MQTT/Sparkplug) where supported, and avoid single-vendor dependency. Verify vendors' actual standards support.
5. **Confirm regulatory exposure.** Have Legal verify EU timelines against primary sources. Have Legal also review worker-monitoring and biometric rules in every operating jurisdiction.
6. **Build capability.** Assess our skills gap and identify integration partners.

## Decision Requested

Approve a scoped pilot and a proposed 60–90 day validation effort covering case studies, regulatory review, and cost modeling. A go/no-go on wider investment would follow. The 60–90 day duration is a planning proposal, not a research-derived figure.

---

### Compliance Review Notes (for internal reference)

- **Softened:**
  - "Becoming core infrastructure" became "candidate infrastructure layer", because adoption is unquantified.
  - "Cannot tolerate cloud delays" became "need low latency".
  - "Streaming video centrally is costly" became "reduces bandwidth", which matches the research.
- **Corrected:**
  - "ROI and market-size figures are mostly vendor-sourced" was inaccurate. The research says payback figures are mostly vendor-sourced and market sizes vary by firm and definition.
  - "All apply" for the EU regulations became conditional. The research says they are relevant if operating in the EU, affect integrators only "possibly", and carry uncertain AI Act and NIS2 status.
  - Regulation dates are now stated with their source confidence.
- **Added:** Confidence and verify flags, the supply-chain risk, an evidence-gaps section, and a label separating recommendations from findings.
- **Adjusted:** The example pilot was changed to avoid leading with safety-critical vision.
- **Not changed:** No unsupported statistics were present. The Amazon robot-fleet figure and the Gartner prediction were not used in the brief, which is appropriate because both are unverified.