# Executive Brief: Cloud Cost Optimization (FinOps) for Mid-Sized Companies

**Basis:** Compiled from analyst knowledge, not live sources. Items marked *(verify)* need confirmation before they inform commitments or budgets. "Mid-sized" is assumed to mean roughly 200–2,000 employees, which should be confirmed.

---

## Headline Takeaway

**FinOps is an operating discipline, not a one-time cost-cutting project. Mid-sized companies can capture meaningful savings by building visibility and accountability first, then making conservative commitments. We cannot yet responsibly forecast a savings percentage, so the first 30 days should establish our own baseline.**

---

## Key Findings

- **Proven levers are well established:** eliminating idle resources, rightsizing, commitment discounts (Savings Plans, Reservations, Committed Use Discounts), scheduling non-production environments, storage tiering, and managing data-transfer costs.
- **Visibility precedes savings.** The framework progresses from Inform to Optimize to Operate. Tagging, allocation, budgets, and anomaly alerts are the foundation.
- **Mid-sized companies face distinct constraints:** no dedicated FinOps owner, weak tagging inherited from fast growth, competition with feature work for engineering time, smaller negotiating leverage, and less financial buffer for a wrong commitment.
- **AI/GPU spend is the fastest-emerging cost area.** Best practices are immature and usage is hard to forecast.
- **Standards are maturing.** The FOCUS billing-data specification is normalizing cost data across providers, but version support varies *(verify)*.
- **Tool ROI is unproven at our scale.** Paid platforms may not pay back at lower spend, and vendor savings claims should be treated skeptically. Native provider tools are a sensible starting point.

---

## Key Risks

1. **Over-commitment:** 1- or 3-year purchases that exceed steady-state usage or become obsolete after architecture changes.
2. **Reliability regressions** from aggressive rightsizing or spot-capacity adoption.
3. **Phantom savings:** cost avoidance mistaken for bill reduction, with savings absorbed by growth.
4. **Organizational drag:** unclear ownership, weak executive sponsorship, and finance–engineering friction.
5. **Poor data quality:** inconsistent tags and disputed shared-cost allocation undermine trust in reports.
6. **AI workload volatility:** GPU scarcity and new pricing models.
7. **Lock-in and tool sprawl:** deep optimization for one provider reduces flexibility, and platform fees can erode savings.

---

## Recommended Actions

| Timeframe | Action |
|---|---|
| **Now** | Name an accountable executive sponsor and a single FinOps owner. Confirm the "mid-sized" scope and our cloud-spend baseline. |
| **Weeks 0–4** | Enable native cost exports, budgets, and anomaly alerts. Audit tagging. Remove idle and orphaned resources. |
| **Months 1–3** | Launch team-level showback. Schedule non-production shutdowns. Make **conservative** initial commitment purchases, covering only proven steady-state usage. |
| **Months 3–9** | Establish a recurring cost-review cadence, define unit-cost metrics (e.g., cost per customer), and improve forecasting. Add AI/GPU spend tracking. |
| **9+ months** | Automate and add policy guardrails. Evaluate paid tooling only against a quoted, spend-matched business case. |

**Verification before major commitments:** Obtain current provider commitment terms, vendor quotes matched to our spend, and the latest FinOps Foundation and Flexera survey data. If we operate in the EU, have legal confirm whether the EU Data Act applies.

**Success measure:** Track actual bill reduction and unit-cost trends, not projected savings.