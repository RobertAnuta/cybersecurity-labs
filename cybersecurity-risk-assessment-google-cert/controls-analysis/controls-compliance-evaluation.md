# Botium Toys: Scope, Goals, and Risk Assessment Report

## Scope and Goals of the Audit

### Scope

The scope of this audit covers the entire security program at Botium Toys. This includes employee equipment and devices, the internal network, core business systems, data storage, ecommerce platforms, and legacy systems.

The review focuses on evaluating existing assets, implemented security controls, and compliance practices currently in place.

### Goals

- Assess existing assets and their protection level
- Evaluate current controls
- Identify compliance gaps
- Determine which security controls and best practices should be implemented to improve Botium Toys’ security posture

## Current Assets

Assets managed by the IT Department include:

- On-premises equipment supporting daily operations
- Employee devices such as desktops, laptops, smartphones, remote workstations, peripherals, and surveillance cameras
- Retail products stored in warehouse facilities
- Core systems including accounting, telecommunications, database management, security systems, ecommerce, and inventory management
- Internet connectivity
- Internal network infrastructure
- Data retention and storage systems
- Legacy systems requiring manual monitoring and maintenance

## Risk Assessment

### Risk Description

There is inadequate management and classification of assets. Several critical security controls are either missing or insufficiently enforced.

Botium Toys may not be fully compliant with U.S. and international regulatory standards due to gaps in access control, encryption, monitoring, and recovery planning.

### Control Best Practices

According to the NIST Cybersecurity Framework, the first function is Identify.

Botium Toys should:

- Clearly identify and classify all assets
- Assign ownership and accountability
- Assess the business impact of asset compromise
- Align asset management with business continuity planning

Without structured identification and classification, risk visibility remains limited.

### Risk Score

Overall Risk Score: 8 out of 10 (High)

This score reflects insufficient control implementation, weak governance enforcement, and exposure to compliance violations.

### Additional Comments and Key Findings

The operational impact of asset loss is currently rated as medium because assets are not formally classified, making impact estimation difficult.

However, regulatory and financial exposure is high due to insufficient protection of sensitive information.

Key findings include:

#### Access and Data Exposure

- All employees have access to internally stored data.
- Cardholder data and PII/SPII may be accessible beyond operational necessity.
- Least privilege and separation of duties are not implemented.

This significantly increases insider and misuse risk.

#### Encryption and Data Protection

- Credit card information is not encrypted.
- Sensitive customer data lacks layered confidentiality protection.

This creates clear PCI-DSS and GDPR exposure.

#### Monitoring and Detection

- No Intrusion Detection System (IDS) is deployed.
- Legacy systems are monitored without a structured schedule.
- Intervention procedures are unclear.

Detection maturity is low.

#### Business Continuity

- No disaster recovery plan exists.
- No backup strategy is in place for critical systems.

In the event of ransomware or infrastructure failure, recovery capability would be limited.

#### Existing Positive Controls

- A firewall blocks traffic based on defined security rules.
- Antivirus software is installed and regularly monitored.
- Data integrity controls are in place.
- A breach notification plan exists for E.U. customers.
- Privacy policies and documentation procedures are enforced.
- Physical security measures such as locks, CCTV, and fire systems are operational.

Baseline protection exists, but layered defense and governance maturity are insufficient.

#### Password Management Weaknesses

- Password requirements are minimal.
- No centralized password management system exists.
- Enforcement of complexity requirements is inconsistent.

This increases the likelihood of credential compromise and operational inefficiency.

## Overall Assessment

Botium Toys demonstrates basic perimeter security controls but lacks structured governance, layered detection, and recovery preparedness.

The primary weakness is not the absence of all controls. It is the absence of structured oversight, enforcement mechanisms, and prioritized risk management.

Strengthening asset classification, access governance, encryption, monitoring, and disaster recovery planning would significantly reduce overall risk exposure.
