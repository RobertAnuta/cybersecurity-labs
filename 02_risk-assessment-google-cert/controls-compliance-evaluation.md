# Controls and Compliance Evaluation

This document summarizes the results of the internal controls and compliance review conducted based on the scope, goals, and risk assessment report prepared by the IT department.

## Controls Review

### Controls Currently in Place

The organization has implemented several foundational security controls:

- Firewall configured with defined security rules  
- Antivirus software installed and monitored  
- Physical security measures including locks, CCTV surveillance, and fire detection/prevention systems  
- Manual monitoring and maintenance of legacy systems  
- Basic password policy  
- Data availability and integrity controls  
- 72-hour breach notification plan for E.U. customers  
- Documented privacy policies and procedures  

These controls show that baseline security measures exist, particularly around perimeter defense and physical protection.

### Controls Not Implemented

The review identified several significant gaps:

- Encryption for stored and transmitted credit card information  
- Least privilege access control model  
- Separation of duties  
- Intrusion Detection System (IDS)  
- Disaster recovery plan  
- Backups for critical data  
- Centralized password management system  
- Formal asset classification and inventory management  

These missing controls increase both operational and regulatory exposure.

### Controls Implemented but Weak/Incomplete

Some controls exist but are not aligned with best practice:

- Password policy does not meet modern complexity standards  
- Legacy system monitoring lacks a defined schedule  
- Broad internal access to sensitive data weakens governance  
- Asset visibility is limited, affecting risk prioritization  

These issues reflect control maturity gaps rather than complete absence of security measures.

## Compliance Review

### PCI DSS

The organization is not fully aligned with PCI DSS requirements.

- Access to cardholder data is not restricted  
- Credit card data is not encrypted  
- Secure password management is not enforced  
- The cardholder data environment lacks sufficient safeguards  

This creates significant financial and regulatory risk.

### GDPR

There is partial alignment with GDPR requirements.

- A 72-hour breach notification plan exists  
- Privacy documentation and procedures are enforced  

However:

- Data classification and inventory processes are incomplete  
- Broad internal access to customer data increases exposure  

### SOC Principles

Control maturity related to SOC standards is inconsistent.

- Data availability and integrity controls are implemented  
- User access policies exist but are not strictly enforced  
- Confidentiality of sensitive data is not adequately controlled  

Overall, confidentiality controls require improvement.

## Recommendations

Based on this review, the most urgent issue is the lack of encryption for payment data. In my view, this should be addressed immediately. Storing and processing credit card information without encryption creates unnecessary regulatory and financial exposure.

I would also prioritize redesigning access control around the principle of least privilege. Currently, access to sensitive data is too broad. Clear role definitions and enforced restrictions would significantly reduce internal risk.

Another critical gap is the absence of backups and a formal disaster recovery plan. Without backups, the organization is exposed to operational disruption that could be avoided with relatively straightforward controls.

Password policy requirements should be strengthened and supported by a centralized enforcement mechanism. The current approach creates both security risk and operational inefficiencies.

Finally, asset inventory and classification need to become structured processes rather than assumptions. Without knowing exactly what needs protection and how critical each asset is, risk management remains reactive.

From my perspective, addressing these areas would significantly improve control maturity, reduce compliance exposure, and create a more stable foundation for future growth.
