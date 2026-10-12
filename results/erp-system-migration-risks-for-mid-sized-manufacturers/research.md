# Research Summary: ERP Migration Risks for Mid-Sized Manufacturers

**Method note:** This was compiled from general knowledge without live data access. I have not verified it against current vendor roadmaps or recent survey reports. Items are tagged **[High confidence]**, **[Medium confidence]**, or **[UNCERTAIN]**. Check anything tagged Medium or UNCERTAIN against primary sources before using it in decisions or citations.

---

## 1. Scope and definitions
- "Mid-sized manufacturer" has no universal definition. Common working ranges are roughly 100–1,000 employees or about $50M–$1B revenue. **[UNCERTAIN: thresholds vary by source, country, and vendor segment.]**
- "Migration" covers several different paths, each with a different risk profile:
  - On-premise to cloud (SaaS or private cloud)
  - Legacy ERP to a new vendor (replatforming)
  - Same-vendor upgrade, e.g., SAP ECC to S/4HANA
  - Consolidating multiple ERPs or plants onto one system

## 2. Current constraints
**Vendor and technology drivers**
- **SAP ECC 6.0:** Mainstream maintenance is scheduled to end in 2027, with extended maintenance (at a premium) to 2030. **[Medium confidence.]** SAP has also discussed longer options tied to its RISE offering. **[UNCERTAIN: details and dates should be checked with SAP.]**
- **Microsoft Dynamics legacy products:** AX 2012 and older NAV versions are already out of mainstream support or near it. **[Medium confidence.]** Dynamics GP has a published end-of-life path, around 2029. **[UNCERTAIN: exact dates.]**
- **Oracle JD Edwards and other long-lived on-premise products:** Vendors state long-term support commitments, but the product investment focus has shifted to cloud offerings. **[UNCERTAIN: specific support-through dates.]**
- **Cloud-first vendor strategy:** Major vendors (SAP, Microsoft, Oracle, Infor) are directing new innovation, especially AI features, to cloud editions. This pressures on-premise customers to move. **[High confidence on direction; UNCERTAIN on specifics per vendor.]**

**Organizational constraints typical of mid-sized firms**
- Small internal IT teams with little migration experience **[High confidence]**
- Heavy dependence on system integrators and implementation partners **[High confidence]**
- Limited capacity to backfill key operations staff who are pulled into the project **[High confidence]**
- Tighter budgets and less tolerance for overruns than large enterprises **[Medium confidence]**
- A shortage of skilled ERP consultants, especially for SAP S/4HANA **[Medium confidence. Based on widely reported market commentary, not verified data.]**

**External and regulatory constraints**
- E-invoicing and tax-reporting mandates are rolling out in several countries (e.g., parts of the EU). **[Medium confidence that these exist; UNCERTAIN on exact country dates, which change frequently.]**
- Industry compliance (FDA 21 CFR Part 11, ISO 9001/13485, AS9100, CMMC for defense suppliers) requires validated systems and traceability. This extends testing and documentation. **[High confidence.]**

## 3. Key risks (ranked roughly by how often they are cited)
1. **Scope creep and over-customization.** Replicating legacy processes in the new system raises cost and complicates future upgrades. **[High confidence]**
2. **Data migration and quality.** Duplicate, incomplete, or inconsistent data in these areas is a common cause of delays and go-live problems:
   - Bills of materials (BOMs)
   - Routings
   - Item masters
   - Vendor and customer records
   - Inventory balances

   **[High confidence]**
3. **Production and supply chain disruption at cutover.** Errors in MRP, scheduling, or inventory can lead to missed shipments or stockouts. **[High confidence]**
4. **Shop-floor and system integration.** Links to MES, SCADA, PLM, WMS, CRM, EDI partners, and quality systems can be fragile. **[High confidence]**
5. **Change management and user adoption.** Resistance, inadequate training, and weak executive sponsorship. **[High confidence]**
6. **Budget and schedule overruns.** See Section 5 for the data-quality caveats.
7. **Partner and vendor risk.** Dependence on the implementer, licensing model changes, and shifts to subscription pricing that raise long-term total cost of ownership. **[Medium confidence]**
8. **Inadequate testing.** Insufficient user acceptance testing, volume testing, or parallel runs. **[High confidence]**
9. **Cybersecurity and business continuity** during and after cutover. **[Medium confidence]**
10. **Loss of institutional knowledge** when long-tenured staff leave or are overloaded. **[Medium confidence]**
11. **Benefit-realization risk.** The system goes live, but the promised efficiencies are not measured or captured. **[Medium confidence]**

## 4. Timelines
- **Typical mid-market implementation duration:** Commonly cited as about 9–18 months, and sometimes longer for multi-plant or heavily customized projects. **[UNCERTAIN: ranges come from general industry commentary, not a verified dataset.]**
- **Typical project phases:**
  - Selection (about 3–6 months) **[UNCERTAIN]**
  - Design and blueprint
  - Build and configure
  - Data migration and testing
  - Training
  - Cutover and go-live
  - Hypercare (often several weeks to a few months)
- **Planning implication:** If a vendor deadline falls in 2027–2030, a 12–24 month project plus selection time means decisions are needed well in advance. The exact start-by dates depend on each firm's situation. **[Medium confidence on logic; specific dates are firm-specific.]**
- **Go-live timing:** Many manufacturers avoid peak production seasons and fiscal year-end. **[High confidence on practice.]**

## 5. Failure and overrun statistics
- Surveys (e.g., from Panorama Consulting, Gartner, and others) have repeatedly reported that a substantial share of ERP projects exceed budget and schedule and fall short of expected benefits.
- **[UNCERTAIN: I cannot reliably quote exact percentages.]** Published figures vary widely by year, sample, and how "failure" is defined. Do not cite a specific number without retrieving the original report.
- Survey results may be biased, since respondents are often self-selected and many reports come from consultancies with an interest in the topic.

## 6. Illustrative case examples (from memory)
- **Hershey (c. 1999):** A problematic ERP, supply chain, and CRM rollout reportedly disrupted Halloween-season order fulfillment. **[Medium confidence; dollar impact UNCERTAIN.]**
- **Nike (c. 2001):** Problems with a supply chain planning implementation (i2) were reported to have caused a significant revenue shortfall. **[Medium confidence; figures UNCERTAIN.]**
- **Revlon (c. 2018):** An ERP implementation issue at a manufacturing facility was disclosed as affecting operations and led to shareholder litigation. **[Medium confidence on the event; UNCERTAIN on details.]**
- These are large companies. Mid-sized firms have less financial buffer, so similar disruption could be proportionally more damaging. **[Reasoned inference, not data.]**

## 7. Planned and emerging developments
- **AI and copilot features** (e.g., SAP Joule, Microsoft Copilot in Dynamics 365, Oracle and NetSuite AI features) are being added, mostly in cloud editions. **[Medium confidence on existence; UNCERTAIN on maturity, pricing, and manufacturing-specific value.]**
- **Composable or modular ERP:** a "core ERP plus best-of-breed add-ons" approach, aimed at reducing the need for customization. **[Medium confidence on trend.]**
- **Industry-specific cloud ERP** for discrete and process manufacturing is gaining traction. **[Medium confidence.]**
- **Migration tooling and accelerators** (e.g., SAP's migration and "clean core" guidance) aim to reduce customization risk. **[Medium confidence; effectiveness UNCERTAIN.]**
- **Pricing model shifts** toward subscription and consumption pricing may change TCO comparisons. **[Medium confidence.]**

## 8. Mitigation practices commonly recommended
- Clean and validate data early. Assign data ownership and run multiple mock migrations.
- Adopt "fit to standard" and limit customizations to a justified minimum.
- Secure active executive sponsorship and dedicate operational subject matter experts.
- Phase the rollout by plant, module, or business unit, where feasible.
- Plan for a rollback or fallback, and build inventory buffers before cutover.
- Run thorough integration testing, including shop-floor systems, and a dress rehearsal of cutover.
- Negotiate fixed-scope or milestone-based contracts with partners, and clarify support terms.
- Invest in training and super-users.
- Define benefit metrics before go-live and track them after.
- Consider independent project assurance or QA. **[Medium confidence; these are broadly cited best practices, not tested here.]**

## 9. Key uncertainties and data gaps
- Exact vendor end-of-support and maintenance dates (SAP, Microsoft, Oracle, Infor, Epicor, others) need checking against official vendor notices.
- Current failure, overrun, and cost statistics specific to mid-sized manufacturers. I have no verified figures.
- Typical cost ranges (as a percentage of revenue or per-user). I am **not** providing numbers because I cannot support them.
- Regional regulatory deadlines (e-invoicing, tax reporting) vary and change.
- Real-world results and pricing of AI features in ERP for manufacturing.
- Whether the case examples' figures are accurately remembered. Verify before citing.

## 10. Recommended next steps for verification
1. Retrieve the latest ERP surveys (Panorama Consulting, Gartner, Eurostat/industry bodies) and extract mid-market manufacturing data.
2. Confirm vendor lifecycle dates from official support portals.
3. Gather 3–5 mid-sized manufacturer case studies, including failures, from trade press and SEC filings.
4. Interview or survey practitioners (CIOs and plant managers at similar firms) on actual timelines and costs.
5. Check regulatory timelines for the specific countries where the target firms operate.