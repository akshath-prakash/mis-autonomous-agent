# Executive Brief: Zero Trust Architecture (ZTA)

**Audience:** Senior Leadership | **Basis:** Research from background knowledge, not live-verified. Items marked *(verify)* need confirmation before external use.

---

## Headline Takeaway

**Zero trust is a multi-year strategy, not a product.** It is now the accepted standard for enterprise security, but most organizations are only partway through it. Our advantage will come from disciplined, phased execution with clear metrics, not from buying a "zero trust" platform.

---

## Key Findings

- **Strong standards backing.** NIST SP 800-207 (2020) and the CISA Zero Trust Maturity Model v2.0 (2023) give us a vendor-neutral blueprint. CISA's model covers five pillars: Identity, Devices, Networks, Applications & Workloads, and Data.
- **Adoption is broad but shallow.** Most large enterprises have started, but few have mature, enterprise-wide programs. Identity (MFA, SSO) is furthest along. Data controls and microsegmentation lag.
- **Public-sector mandates set the benchmark.** US federal directives (EO 14028, OMB M-22-09) and the DoD target of FY2027 serve as reference models and create supply-chain pressure. They are not direct mandates for most private firms. EU rules (NIS2, DORA) reward ZT-aligned controls without requiring them by name.
- **Common entry points** are phishing-resistant MFA, SSO consolidation, replacing VPN with ZTNA, endpoint posture checks, and privileged access management.
- **Market data is unreliable.** Vendor survey "adoption" figures use inconsistent definitions. We should not benchmark against them.

---

## Key Risks

1. **False confidence.** Declaring success after deploying one tool (e.g., MFA or ZTNA) while lateral-movement and data-layer gaps remain.
2. **Identity concentration.** A compromised identity provider or token undermines the whole model.
3. **Security stack vulnerabilities.** Remote-access and edge products, including those from leading vendors, have had serious exploited flaws.
4. **Availability dependency.** Cloud-delivered policy engines become single points of failure, so break-glass procedures are essential.
5. **Legacy, OT, and identity sprawl.** Older systems, devices that cannot run agents, and post-acquisition identity fragmentation slow progress.
6. **Program fatigue.** Siloed funding, scope creep, lost sponsorship, and hard-to-quantify ROI can stall multi-year efforts.
7. **Vendor lock-in and privacy.** Proprietary platforms raise switching costs, and continuous monitoring raises employee data-protection concerns.

---

## Recommended Actions

1. **Appoint an executive sponsor and a cross-functional steering group** spanning network, identity, endpoint, application, and data teams, with a single consolidated budget line.
2. **Baseline our maturity** against the CISA model, and inventory assets, identities, and data flows first.
3. **Prioritize quick wins:** phishing-resistant MFA, identity consolidation, and VPN-to-ZTNA migration for high-risk access.
4. **Harden the foundation:** protect the identity provider, define break-glass procedures, and set vendor vulnerability-response expectations.
5. **Plan for hard problems:** compensating controls for legacy and OT systems, and a phased data classification effort.
6. **Define outcome-based metrics** (e.g., reduced standing privileges, lateral-movement containment) to demonstrate value and sustain funding.
7. **Avoid lock-in:** require interoperability and open standards in procurement.
8. **Involve Legal and HR early** on monitoring and privacy requirements.

---

## Open Items to Verify

- Current adoption benchmarks (use independent, methodology-transparent surveys)
- Status of 2025 US federal policy changes and any DoD timeline revisions
- Realistic cost and duration estimates (commonly cited as 3–5+ years, *unverified*)

**Decision requested:** Approve sponsorship, a maturity baseline, and a phased roadmap for the next planning cycle.