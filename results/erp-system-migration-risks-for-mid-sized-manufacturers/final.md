# Executive Brief: ERP Migration Risk for Mid-Sized Manufacturers

**Evidence note:** This brief draws on general industry knowledge, not verified current data. Confidence tags are carried over from the underlying research. Vendor dates, statistics and case details must be confirmed against primary sources before any decision or external citation.

**Scope note:** "Mid-sized manufacturer" has no universal definition. Working ranges are roughly 100–1,000 employees or $50M–$1B revenue, and these vary by source. "Migration" covers different paths: on-premise to cloud, a change of vendor, a same-vendor upgrade such as SAP ECC to S/4HANA, and multi-plant consolidation. Each path carries a different risk profile.

## Headline Takeaway

**Vendor direction is pushing on-premise customers toward cloud editions, so many mid-sized manufacturers will need to plan a migration. The risks most often cited are in execution: data quality, over-customization and cutover disruption.** Mid-sized firms likely have less financial buffer than large enterprises to absorb a failed cutover. *(This is a reasoned inference, not data.)*

## Key Findings

- **Vendors are pushing customers to the cloud.** SAP, Microsoft, Oracle and Infor are directing new innovation, especially AI features, to cloud editions. *(High confidence on direction. Uncertain on specifics per vendor.)*
- **Support deadlines are approaching for some products.**
  - SAP ECC 6.0 mainstream maintenance is reported to end in 2027, with extended maintenance to 2030. *(Medium confidence.)*
  - Dynamics GP has a published end-of-life path around 2029. *(Uncertain.)*
  - Some vendors state long-term support commitments for long-lived on-premise products such as JD Edwards. *(Uncertain on dates.)*
  - Verify all dates with the vendors.
- **Timelines are long.** Mid-market implementations are commonly cited at about 9–18 months, and longer for multi-plant or heavily customized projects. Selection adds time, often cited at about 3–6 months. *(Uncertain. These ranges come from general commentary, not a verified dataset.)* Firms facing 2027–2030 vendor deadlines should plan early. Start dates are firm-specific.
- **Mid-sized firms face structural constraints.**
  - Small IT teams with little migration experience. *(High confidence.)*
  - Heavy reliance on integrators. *(High confidence.)*
  - Limited capacity to backfill operations staff. *(High confidence.)*
  - Tighter budgets and less tolerance for overruns. *(Medium confidence.)*
  - A shortage of skilled ERP consultants, especially for S/4HANA. *(Medium confidence. Based on market commentary, not verified data.)*
- **Regulated sectors face more validation work.** FDA 21 CFR Part 11, ISO 9001/13485, AS9100 and CMMC requirements call for validated systems and traceability. This extends testing and documentation. *(High confidence.)*
- **Failure data is unreliable.** Surveys (e.g., Panorama Consulting, Gartner) have repeatedly reported that a substantial share of ERP projects exceed budget and schedule or miss expected benefits. Figures vary widely by year, sample and definition of "failure". Respondents are often self-selected, and many reports come from consultancies with an interest in the topic. **No reliable percentage is available to cite.**

## Top Risks

*(Ranked roughly by how often they are cited, not by measured impact.)*

1. **Scope creep and over-customization:** replicating legacy processes raises cost and complicates future upgrades. *(High confidence.)*
2. **Poor data quality:** BOMs, routings, item masters, vendor and customer records, and inventory balances are common causes of delays and go-live problems. *(High confidence.)*
3. **Cutover disruption:** MRP, scheduling or inventory errors can cause missed shipments or stockouts. *(High confidence.)*
   - Hershey (c. 1999), Nike (c. 2001) and Revlon (c. 2018) are reported examples.
   - These examples are recalled from memory. All three are large companies, and Nike's case involved a supply chain planning system. *(Medium confidence on events. Financial figures and details are unverified.)*
4. **Fragile integrations:** links to MES, SCADA, PLM, WMS, CRM, EDI partners and quality systems. *(High confidence.)*
5. **Weak change management and sponsorship:** inadequate training and thin executive backing. *(High confidence.)*
6. **Inadequate testing:** insufficient user acceptance testing, volume testing or parallel runs. *(High confidence.)*
7. **Partner dependence and pricing shifts:** reliance on the implementer, licensing changes and subscription pricing that may raise long-term total cost of ownership. *(Medium confidence.)*

*Also cited, at medium confidence: cybersecurity and continuity during cutover, loss of institutional knowledge, and benefit-realization risk, where promised efficiencies are never measured or captured.*

## Recommended Actions

*These are broadly cited best practices, not tested here. (Medium confidence.)*

1. **Confirm the clock.** Verify current vendor end-of-support dates and regulatory deadlines (e.g., e-invoicing) for our operating regions. Regional dates change frequently.
2. **Start data cleanup early.** Assign data owners and plan multiple mock migrations.
3. **Adopt "fit to standard."** Limit customizations to a justified minimum.
4. **Secure sponsorship and capacity.** Obtain active executive sponsorship and dedicate operations subject matter experts, with a plan for backfill.
5. **Reduce cutover risk.**
   - Phase the rollout by plant, module or business unit where feasible.
   - Build inventory buffers.
   - Rehearse the cutover.
   - Define a rollback or fallback plan.
   - Avoid peak production periods and fiscal year-end.
6. **Structure partner contracts carefully.** Use fixed-scope or milestone-based terms with clear support obligations, and consider independent project assurance.
7. **Invest in training and super-users.**
8. **Define benefit metrics before go-live** and track them afterward.

## Before We Commit

Validate the evidence base before any investment decision:
- Pull current survey data (Panorama, Gartner) and extract mid-market manufacturing figures.
- Confirm vendor lifecycle dates from official support portals.
- Obtain 3–5 mid-sized manufacturer case studies, including failures, from trade press and SEC filings.
- Interview peer CIOs and plant managers on actual costs and timelines.
- Check regulatory timelines for the specific countries where we operate.

**Cost benchmarks are not provided** because no figures could be supported. Current failure and overrun statistics specific to mid-sized manufacturers, and the real-world results and pricing of AI features in ERP for manufacturing, are also open data gaps.

---

### Compliance Review Log
- **Headline:** Removed the unsupported claims that migration is "a question of when, not whether" and that "the main danger is execution, not the decision itself." Reframed the sentence on mid-sized firms' financial buffer as an inference.
- **Failure data:** Changed "come largely from consultancies" to "many reports come from consultancies," as the research states. Added the self-selection caveat.
- **Regulated sectors:** Changed "longer projects" to "more validation work," because the research supports extended testing and documentation but not a longer project duration.
- **Support deadlines:** Added the ECC extended-maintenance date, the JD Edwards caveat and an explicit "uncertain" tag for Dynamics GP. The original lumped these together as "medium to low."
- **Case examples:** Added the missing confidence tags and the caveat that all three are large companies. Noted that Nike's case was a supply chain planning system and not a full ERP.
- **Recommendation 3:** Replaced "require executive approval for any customization," which the research does not support, with "limit customizations to a justified minimum."
- **Other additions:** Added the scope and definition note, confidence tags on the risk list, and a statement that the recommended actions are untested best practices. Restored the testing risk and the training recommendation, which the research includes and the draft omitted.