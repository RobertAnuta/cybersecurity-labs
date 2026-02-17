# Risk Assessment – Botium Toys

## Overview

*This scenario is based on a fictional company!*
In this project, I analyzed the results of an internal audit conducted for Botium Toys, a growing retail company expanding its online presence.
The IT department prepared an initial scope, goals, and risk assessment report outlining current assets, controls, and areas of concern.

Based on that documentation, I performed a structured review of existing controls and evaluated compliance exposure using the NIST Cybersecurity Framework as a reference.

## Project Structure

- `scenario/scenario.md`  
  Contains the scope, goals, asset inventory, and preliminary risk assessment report prepared by the IT department.

- `analysis/risk-assessment-report.md`  
  My structured audit analysis, including evaluation of risks and control maturity.

- `analysis/controls-compliance-evaluation.md`  
  My review of implemented controls, identified gaps, compliance exposure, and recommendations.

- `references/`  
  Supporting concepts and regulatory context referenced in my assessment.

## Key Findings

Through this review, I identified several significant control gaps:

- No encryption for stored or transmitted credit card data  
- Broad internal access to sensitive data  
- No disaster recovery plan or backups  
- Lack of formal asset classification  
- Weak password policy enforcement  
- No intrusion detection system  

While foundational controls such as firewall protection, antivirus, and physical security measures are in place, overall control maturity is inconsistent.

## Risk Exposure

From my assessment, the absence of encryption and limited access governance creates elevated regulatory risk, particularly in relation to PCI DSS requirements. In addition, the lack of backups introduces operational risk that could directly impact business continuity.

Although some privacy and availability controls exist, security governance lacks structure and consistency.

## Purpose of This Analysis

My goal in this project was not only to identify missing controls, but to evaluate how gaps in governance, visibility, and enforcement increase overall business exposure.

This assessment focuses on improving control maturity, strengthening compliance alignment, and building a more resilient security foundation as the organization grows.
