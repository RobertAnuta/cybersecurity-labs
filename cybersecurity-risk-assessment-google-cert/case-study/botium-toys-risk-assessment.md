# Botium Toys – Security Risk Assessment

## Context

This case study simulates a full-scope security review of Botium Toys, a retail company operating both physical storefronts and online sales. The organization manages internal systems, ecommerce platforms, customer payment data, employee devices, and warehouse operations.

The objective was to evaluate the organization’s security posture, identify control gaps, and assess overall risk exposure.


## What I Reviewed

I analyzed:

- Asset inventory and ownership visibility
- Access control structure
- Data protection mechanisms
- Monitoring and detection capabilities
- Business continuity preparedness
- Compliance alignment (PCI-DSS, GDPR, SOC principles)


## Key Findings

### 1. Lack of Structured Asset Governance

Assets are inventoried but not classified.  
There is no formal ownership model or lifecycle management, especially for legacy systems.  

This creates uncertainty about impact if a system fails or is compromised.


### 2. Access Control Is the Biggest Weakness

- All employees can access internally stored data.
- Least privilege is not implemented.
- No separation of duties.
- No centralized password management.

This significantly increases insider risk and regulatory exposure.


### 3. Sensitive Data Is Not Properly Protected

- Credit card data is not encrypted.
- PII/SPII lacks layered protection.
- Password policy exists but is weak and unenforced.

This creates direct PCI-DSS and GDPR risk.


### 4. Detection Capabilities Are Missing

- No Intrusion Detection System (IDS).
- No structured monitoring schedule for legacy systems.
- No proactive threat visibility.

The organization relies heavily on perimeter controls (firewall, antivirus) without layered detection.


### 5. Business Continuity Is Not Addressed

- No disaster recovery plan.
- No backup strategy.

In the event of ransomware or system failure, operational downtime would likely be significant.


## Risk Perspective

Overall Risk Score: **8/10 (High)**

The most critical issue is not the absence of every control — baseline protections exist.  

The core problem is the lack of structured governance and layered defense.  
The organization is reactive rather than proactive.

Primary risk drivers:

- Regulatory fines
- Data breach exposure
- Operational disruption
- Insider misuse risk


## What I Would Fix First

If prioritizing improvements, I would implement:

1. Least Privilege and role-based access control
2. Encryption for cardholder data
3. Backup and disaster recovery planning
4. IDS deployment
5. Centralized password enforcement

These actions would immediately reduce regulatory and operational risk.


## Takeaway

This exercise reinforced the importance of structured governance in cybersecurity.  

From my compliance and operational background, I approach security from a risk visibility perspective:  
controls are only effective when ownership, monitoring, and accountability are clearly defined.

This case study demonstrates applied risk analysis, governance evaluation, and control prioritization aligned with real-world security operations.
