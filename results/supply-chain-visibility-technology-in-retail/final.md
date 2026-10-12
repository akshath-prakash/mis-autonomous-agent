# Executive Brief: Supply Chain Visibility (SCV) in Retail

**Prepared for:** Senior Leadership
**Basis:** Desk research from background knowledge, not live database or web retrieval. Nothing here has been checked against primary sources.
**Confidence key:** **[H]** High, **[M]** Medium, **[L]** Low/Unverified. Items marked *verify* must be confirmed against primary sources before we commit funds.

---

## Headline Takeaway

**Visibility technology is mature in transportation tracking and apparel RFID. It is weak at sub-tier supplier depth, data quality and partner interoperability. Regulation and retailer mandates are the strongest adoption drivers, but their dates keep shifting. We should invest in durable foundations (data standards, supplier integration, decision rules) rather than build to any single compliance deadline.**

---

## Key Findings

- **Proven capabilities:**
  - Multimodal shipment tracking (ocean, truck, parcel, air) is mainstream among large retailers. **[M]**
  - Item-level RFID is established in apparel and footwear, where Walmart, Target and Inditex (Zara) have used it for years. **[H]**
  - Store inventory accuracy is commonly cited as rising from roughly 60–75% to 95%+ with RFID, often attributed to Auburn University RFID Lab research. Figures vary by study and context, so treat them as *indicative only*. **[M]**
- **Persistent gaps:**
  - Visibility beyond tier-1 suppliers is limited. **[H]**
  - Master data is inconsistent and ERP/WMS/TMS systems are siloed. **[H]**
  - GS1/EPCIS adoption is uneven. **[H]**
  - Ocean carrier data is inconsistent in timeliness and accuracy. **[M]**
- **Demand drivers:**
  - **UFLPA** (in effect since June 2022) increases the need for supply-chain origin documentation. **[H]**
  - **FSMA 204** food traceability. **[H]**
  - **EU product passport and due-diligence rules.** **[M]**
  - **Tariff and de minimis changes.** The US de minimis exemption ended for China/Hong Kong in May 2025 and for most other countries in late August 2025. Policy has changed repeatedly, so *verify current status*. **[M]**
  - **Repeated disruptions:** Red Sea rerouting, the Panama Canal drought and the Baltimore bridge collapse. **[H on events; M on quantified impact]**
- **Key milestones (all dates shifting or uncertain):**

| Milestone | Timing | Confidence / caveat |
|---|---|---|
| GS1 Sunrise 2027: point-of-sale able to scan 2D barcodes (GS1 Digital Link) | Industry target of end-2027 | **[M-H]** on the target date. **[L]** on actual retailer readiness, and adoption is uneven. |
| FSMA 204 compliance | Originally Jan 20, 2026. FDA announced an intent to extend by ~30 months (to about July 2028). | **[M]** *Verify final legal status.* |
| EU Digital Product Passport (ESPR) | Framework in force since July 2024. First requirements are expected roughly 2026–2028+, and textiles are a priority category. | **[M]** on the framework. **[L]** on category dates, including textiles. |
| EU Battery Regulation battery passport | Feb 2027 | **[M]** |
| EUDR and EU CSDDD | Both delayed or revised (EUDR more than once; CSDDD via the 2025 "Omnibus" process, possibly to ~2028 for the first wave). | **[L-M]** *Verify current dates.* |

- **Emerging technology:** AI and agentic AI in control towers (auto-rebooking, supplier outreach, exception resolution) are at pilot or early-production stage. Maturity is expected over roughly 2–5 years, and vendor claims are often ahead of production reality. **[L]**

---

## Principal Risks

1. **Regulatory instability:** EU and US rules (FSMA 204, EUDR, CSDDD) are being delayed, revised or simplified, so we risk building to moving targets. **[H]** *Verify current legal dates.*
2. **Execution at scale:** Pilots can succeed while rollout fails because of supplier compliance, tag-placement errors and store process drift. **[M]**
3. **Cybersecurity and third-party risk:** More connected systems enlarge the attack surface. Recent retail and distribution incidents include M&S and Co-op (UK, April–May 2025) and UNFI (US, June 2025). **[M-H]** on the events. *Verify operational impact details before citing them externally.*
4. **Technology and vendor bets:**
   - TradeLens (Maersk/IBM blockchain) was discontinued (announced Nov 2022, wound down in 2023). **[H]**
   - Blockchain food-traceability programs such as IBM Food Trust have faced adoption and cost questions, and their current status needs verification. **[M/L]**
   - Vendor consolidation, such as WiseTech's announced 2025 acquisition of E2open, can change roadmaps, pricing and support. **[M]** *Verify deal status and terms.*
5. **Privacy and AI reliance:** Item-level tracking linked to consumers raises privacy concerns, especially under GDPR. **[M]** Model errors and unverified AI predictions can mislead decisions. **[M]**
6. **Unquantified economics:** Our research did not establish reliable market-size, per-tag or reader cost, or ROI figures. Vendor and case-study claims differ and are rarely independently verified. We make no financial projections in this brief.

---

## Recommended Actions

1. **Fix the data foundation first.** Standardize product and location master data on GS1 identifiers (GTIN, GLN, SSCC). Set EPCIS-ready data requirements for new supplier contracts.
2. **Prioritize by maturity and obligation.** Extend RFID first in categories where adoption is mature (apparel and footwear). Run controlled pilots elsewhere with predefined success metrics. Gate scale-up on our own validated business case, because the research does not establish ROI. Business cases are harder for low-margin or low-value items.
3. **Prepare for Sunrise 2027.** Assess POS and e-commerce readiness for 2D barcodes now. Confirm whether peer retailers have formally committed to timelines, since this is an open data gap.
4. **Build modular, regulation-agnostic traceability.** Map tier-1 to tier-n for high-risk categories (UFLPA exposure, food, textiles) without locking into a single compliance date. Maintain a regulatory watch with a named owner.
5. **Reduce vendor and technology risk.** Favor open standards and API-based architectures. Include exit and data-portability terms in contracts. Subject blockchain-based solutions to heightened due diligence, given the TradeLens discontinuation and mixed food-traceability results.
6. **Embed security and privacy by design.** Require third-party security assessments. Run a privacy review of consumer-linked tracking.
7. **Govern AI use.** Pilot AI exception management with human oversight, defined decision rules and alert-volume targets. This guards against alert fatigue and over-reliance on unvalidated outputs.
8. **Close the evidence gaps within 60–90 days.** Validate the following through primary sources before final budget approval:
   - current legal dates (FSMA 204, EUDR, CSDDD, DPP);
   - retailer mandate scopes and deadlines (including Walmart's reported RFID expansion into fresh/perishables, which is **[L]**);
   - tag and reader costs;
   - ROI benchmarks;
   - the percentage of retailers with item-level RFID or end-to-end visibility.

   Sources: GS1, FDA, EU Official Journal and European Commission pages, CBP, Auburn RFID Lab, retailer supplier portals, and analyst reports (Gartner, Forrester, IDC).

---

**Decision requested:** Approve foundational data and standards work and a 60–90 day verification sprint. Scaled investment should be gated on validated costs, dates and pilot results.

---

### Compliance Review Log (for internal record)

- **Removed/softened:**
  - "Avoid unproven technologies such as blockchain" became "heightened due diligence." The research reports mixed results and an unverified current status, not a basis for a blanket prohibition.
  - "Scale RFID where economics are proven (apparel, high-value goods)" was corrected. "High-value goods" and "proven economics" are not supported by the research, which gives no quantified ROI.
  - "M&S, Co-op, UNFI incidents show the exposure" was reworded as illustrative. The research flags the operational impact details for verification and does not link the incidents to SCV systems.
  - "Reliable figures are not available" became "not established in our research." The research states it did not provide these figures. It does not say they do not exist.
- **Added caveats and confidence tags:**
  - the Sunrise 2027 readiness caveat;
  - EUDR/CSDDD *verify* flags;
  - the de minimis *verify* flag;
  - the AI claims flagged as Low confidence.
- **Unsupported content check:** No market-size, ROI, or per-tag cost figures appear in this brief. The only quantitative accuracy figure (60–75% to 95%+) is retained and labeled indicative.