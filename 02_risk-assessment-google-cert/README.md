# Risk Assessment — Botium Toys (Google Cybersecurity Certificate)

## Overview

I conducted an internal audit analysis for Botium Toys, a fictional 
retail company expanding its online presence. The IT department provided 
the initial scope, asset inventory, and a preliminary risk assessment. 
My role was to evaluate existing controls, identify gaps, and assess 
compliance exposure.

What surprised me was how many security gaps I found. What I found 
interesting was that even with foundational knowledge, I could identify 
practical solutions for each one.

## Scenario

Botium Toys operates from a single location serving as office, 
storefront, and warehouse. Growing online sales introduced pressure 
around payment processing compliance and international data regulations 
(PCI DSS, GDPR).

Risk score assessed by the IT department: **8/10**

## Key Findings

Gap Risk

- No encryption for credit card data PCI DSS exposure
- Broad internal access to sensitive data Insider risk
- No disaster recovery plan or backups Business continuity
- No intrusion detection system Limited visibility
- Weak password policy Credential risk
- No formal asset classification Risk prioritization gaps

## Skills Demonstrated

- Internal audit analysis
- Controls and compliance evaluation (PCI DSS, GDPR, SOC)
- Risk identification and prioritization
- NIST CSF application

## Files

- [`controls-compliance-evaluation.md`](./controls-compliance-evaluation.md) 
  — my full review of implemented controls, gaps, compliance exposure, 
  and recommendations

## Takeaway

This project taught me that security gaps rarely exist in isolation. 
Each missing control created exposure in multiple directions — a weak 
password policy wasn't just a credential risk, it was also a governance 
and compliance gap. Thinking through those connections changed how I 
approach risk analysis.