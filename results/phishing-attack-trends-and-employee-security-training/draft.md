# Executive Brief: Phishing Threats and Employee Security Training

## Headline Takeaway
**Phishing remains a leading path to breach, and awareness training alone does not stop it.** Independent evidence shows training has limited impact on its own. Risk reduction depends on pairing training with phishing-resistant authentication and verification controls.

*Note: This brief draws on background knowledge of published reports, not live sources. Figures marked "verify" should be confirmed before external use.*

## Key Findings

- **Phishing is persistent and costly.** Verizon's DBIR attributes roughly 60–75% of breaches to the "human element" (verify the edition). IBM puts phishing at about 15–16% of breaches, with average breach costs of roughly $4.4–4.9M (verify). FBI data shows Business Email Compromise losses in the billions annually.
- **Attacks are getting harder to spot.** Generative AI removes classic red flags such as poor grammar. Adversary-in-the-middle kits steal session tokens and bypass SMS and app-based MFA. Attackers also use QR codes, voice calls, help-desk impersonation, and fake-CAPTCHA lures to move outside email. Deepfake fraud is documented, including a ~$25M Hong Kong case, but its overall scale is unknown.
- **Training effectiveness is contested.** A large 2025 study (UC San Diego Health, ~19,500 employees) found annual and post-click training had minimal measurable effect. A 2022 ETH Zurich study found embedded training could be ineffective or counterproductive. Vendor-reported improvements are mostly unreviewed and measure simulation clicks, not real incidents.
- **Better metrics exist.** Employee *reporting* rates are a more meaningful indicator than click rates.
- **Compliance pressure is rising.** PCI DSS 4.0 training requirements became mandatory March 31, 2025. NIS2 and DORA add obligations in the EU, and national implementation varies.

## Risks

1. **False assurance:** Low simulation click rates may reflect easy tests, not real resilience.
2. **MFA bypass:** Non-phishing-resistant MFA is vulnerable to token theft.
3. **Impersonation fraud:** Payment and credential-reset verification is often immature against deepfake and voice attacks.
4. **Supply-chain phishing:** Compromised vendor accounts bypass internal training.
5. **Checkbox compliance:** Regulatory deadlines can drive training that satisfies auditors without changing behavior.
6. **Eroded trust:** Punitive simulations can suppress incident reporting, which delays detection.

## Recommended Actions

1. **Prioritize phishing-resistant authentication** (passkeys/FIDO2) for administrators, finance, executives, and other high-risk roles.
2. **Harden high-value processes.** Require out-of-band verification for wire transfers, vendor banking changes, and help-desk credential resets.
3. **Reposition training as one layer, not the control.** Make it role-based, cover voice, SMS, and QR scenarios, and make reporting one-click and blame-free.
4. **Change the metrics.** Track reporting rate, time-to-report, and real incident outcomes rather than click rates alone.
5. **Enforce email authentication** (SPF, DKIM, DMARC) and review filtering gaps outside email.
6. **Validate before committing budget.** Confirm current DBIR, IBM, and IC3 figures, review the UCSD and ETH Zurich studies, check regulatory scope with counsel, and treat vendor statistics as marketing until methodology is reviewed.

## Decision Requested
Endorse a shift in investment from awareness volume toward authentication and process controls, and authorize a 30-day validation of the figures above.