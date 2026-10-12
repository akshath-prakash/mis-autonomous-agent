# Executive Brief: Zero Trust Architecture (ZTA)

**Audience:** Senior Leadership | **Basis:** Research from background knowledge, not live-verified. Items marked *(verify)* need confirmation before external use. No adoption percentages, market-size figures or cost figures are cited, because none could be verified.

---

## Headline Takeaway

**Zero trust is a strategy and architecture approach, not a product, and it is typically a multi-year effort *(duration unverified)*.** Most large enterprises report having started, but few claim mature, enterprise-wide implementation. We should favor disciplined, phased execution with clear metrics over buying a "zero trust" platform.

---

## Key Findings

- **Strong standards backing.** NIST SP 800-207 (Aug 2020) and the CISA Zero Trust Maturity Model v2.0 (Apr 2023) give us vendor-neutral reference frameworks. CISA's model covers five pillars: Identity, Devices, Networks, Applications & Workloads, and Data.
- **Adoption is widespread but uneven.** Most large enterprises report having started, but few claim mature, enterprise-wide programs. Identity (MFA, SSO) is typically furthest along. Data-centric controls and microsegmentation typically lag. *(Medium confidence; based on general industry picture, not measured data.)*
- **Public-sector mandates serve as reference models.** US federal directives (EO 14028, May 2021; OMB M-22-09, Jan 2022) and the DoD Zero Trust Strategy (target-level ZT by end of FY2027 *(verify; timeline may have been revised)*) act as reference models and create contractor and supply-chain pressure. They are not direct mandates for most private firms. EU rules (NIS2, DORA) do not mandate ZT by name, but they push risk-based access control, segmentation and resilience, which ZT supports.
- **Common entry points** are phishing-resistant or multifactor authentication, SSO and identity consolidation, replacing VPN with ZTNA, endpoint posture checks, and privileged access management.
- **Published adoption figures are not comparable.** Vendor and analyst surveys define "implemented" differently and often skew toward customers or security-aware respondents. We should not benchmark against them without checking methodology.

---

## Key Risks

1. **False confidence.** Declaring success after deploying one component (e.g., MFA or ZTNA) while lateral-movement and data-layer gaps remain.
2. **Identity concentration.** Compromise of an identity provider or its tokens undermines the model.
3. **Security stack vulnerabilities.** Remote-access and edge security products, including those from leading vendors, have had serious exploited vulnerabilities (e.g., Palo Alto GlobalProtect CVE-2024-3400 and several Ivanti issues). ZT tooling is not immune.
4. **Availability dependency.** Policy engines and cloud-delivered ZTNA/SASE become critical dependencies, and outages can block all access, so break-glass procedures are essential.
5. **Legacy, OT, and identity sprawl.** Older systems, devices that cannot run agents, and post-acquisition identity fragmentation slow progress.
6. **Program fatigue.** Siloed funding, scope creep, lost sponsorship, and hard-to-quantify ROI can stall multi-year efforts.
7. **Vendor lock-in and privacy.** Proprietary signals and platforms raise switching costs. Continuous monitoring of users and devices raises employee privacy and data-protection issues (e.g., GDPR, works councils).

---

## Recommended Actions

*These are management recommendations drawn from the identified risks and barriers. They are not findings from the research.*

1. **Appoint an executive sponsor and a cross-functional steering group** spanning network, identity, endpoint, application, and data teams. Consider consolidating funding, since siloed budgets are a common barrier.
2. **Baseline our maturity** against the CISA model, and inventory assets, identities, applications, and data flows first.
3. **Prioritize common entry points:** phishing-resistant MFA, identity consolidation, and VPN-to-ZTNA migration for high-risk access.
4. **Harden the foundation:** protect the identity provider, define break-glass procedures, and set vendor vulnerability-response expectations.
5. **Plan for hard problems:** compensating controls (e.g., segmentation, gateways) for legacy and OT systems, and a phased data classification effort.
6. **Define outcome-based metrics internally** to demonstrate value and sustain funding. There is no widely agreed quantitative "done" metric, so we must set our own. Candidates include reduced standing privileges and lateral-movement containment, which are illustrative only.
7. **Limit lock-in:** require interoperability in procurement, since the vendor market has overlapping categories and unclear interoperability.
8. **Involve Legal and HR early** on monitoring and privacy requirements.

---

## Open Items to Verify

- Current adoption benchmarks (use independent, methodology-transparent surveys)
- Status of 2025 US federal policy changes and any DoD timeline revisions
- Realistic cost and duration estimates (multi-year, often described as 3–5+ years, with no authoritative source; *unverified*)
- Maturity of AI-related ZT capabilities (early-stage; product maturity unclear)

**Decision requested:** Approve sponsorship, a maturity baseline, and a phased roadmap for the next planning cycle.

---

### Compliance Review Log (not part of the executive distribution)

| # | Original claim | Action |
|---|---|---|
| 1 | "Now the accepted standard for enterprise security" | **Removed.** Unsupported; it contradicts the research finding that few organizations are mature. |
| 2 | "Our advantage will come from…" | **Reworded.** It was a speculative competitive claim, now a neutral recommendation. |
| 3 | "Adoption is broad but shallow" | **Reworded and flagged.** The research rates it Medium confidence and it rests on self-reported starts. |
| 4 | EU rules "reward" ZT-aligned controls | **Corrected** to match the source: they push risk-based controls that ZT supports. |
| 5 | DoD FY2027 target stated without caveat | **Flagged *(verify)*.** The research notes possible revision. |
| 6 | "Single points of failure" | **Corrected** to "critical dependencies," as the research states. |
| 7 | "Should not benchmark against" vendor data | **Softened** to "not comparable; check methodology." |
| 8 | Metric examples and "single consolidated budget line" | **Labeled as recommendations or illustrative.** They are not research-backed, and the research says no agreed metric exists. |
| 9 | "Multi-year" in the headline | **Flagged *(unverified)*.** The 3–5+ year range is tagged Low/Unverified in the research. |
| 10 | Vendor-vulnerability examples | **Added** the specific, research-supported examples (CVE-2024-3400, Ivanti). |