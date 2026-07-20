# Security Awareness Training Platform

## Project Status: Work in Progress

## Overview

I designed and I am building an end-to-end Security Awareness Training program, combining a compliance framework, training content, and a functional tracking application. The goal of this project is to demonstrate how a security awareness program is designed, delivered, and measured in a real organizational context, from the underlying compliance requirements to the technical implementation of a training and tracking tool.

This project bridges my background in Learning & Development with cybersecurity, an area where I bring direct, hands-on training design experience rather than only theoretical knowledge.

## Project Goals

- Build a hybrid compliance framework by mapping training requirements from NIST CSF and ISO 27001
- Design training content across 8 core awareness topics, each aligned with a specific compliance control
- Apply learning design principles (VARK model) to each training module
- Build a functional mini LMS application (Python/Flask) that delivers content and tracks completion
- Produce a tracking and reporting layer that maps completion data back to compliance requirements

## Compliance Framework

This project uses a hybrid framework, combining training and awareness requirements from NIST CSF and ISO 27001, rather than adopting either standard in full. Each training module maps to a specific control from one or both frameworks, so the program has a clear compliance rationale instead of being a generic list of security topics.

| Framework | Control | What It Requires |
|---|---|---|
| NIST CSF | PR.AT-1 | Users are informed and trained on recognizing security threats, including social engineering |
| ISO 27001:2022 | A.6.3 | Personnel receive awareness education and training relevant to their job function |

This mapping is intentionally lightweight. The goal is not to reproduce a full corporate policy, but to show that each module is grounded in a real compliance requirement rather than being an arbitrary topic choice. The full mapping for each module is listed in the Training Modules table below and repeated at the top of each individual module document.

## Project Structure

```
05_security-awareness-training-platform/
├── README.md
├── training-materials/
│   ├── module-01-phishing-social-engineering.md
│   ├── module-02-data-classification-handling.md
│   ├── module-03-least-privilege.md
│   ├── module-04-devices-system-security.md
│   ├── module-05-physical-security.md
│   ├── module-06-secure-communication.md
│   ├── module-07-third-party-security.md
│   └── module-08-ai-usage.md
├── app/
│   ├── app.py
│   ├── models.py
│   ├── templates/
│   └── static/
├── diagrams/
│   ├── application-flow.png
│   ├── database-schema.png
│   └── database-schema.md
└── screenshots/
```

## Database Schema

The application uses three SQLite tables: `USERS`, `MODULES`, and `COMPLETIONS`. `COMPLETIONS` is the core tracking table, linking a user to a module with the score, pass/fail status, and completion date for that attempt. The full entity relationship diagram and table notes are in `diagrams/database-schema.md`.

## Training Modules

| # | Module | Compliance Mapping | Status |
|---|---|---|---|
| 1 | Phishing & Social Engineering Defense | NIST PR.AT-1, ISO A.6.3 | In progress |
| 2 | Data Classification & Handling | ISO A.5.12, A.8.10 | Planned |
| 3 | Principle of Least Privilege | NIST PR.AC, ISO A.8.2 | Planned |
| 4 | Devices & System Security | NIST PR.PT, ISO A.8.1 | Planned |
| 5 | Physical Security | ISO A.7 | Planned |
| 6 | Secure Communication | NIST PR.DS, ISO A.5.14 | Planned |
| 7 | Third-Party Security | ISO A.5.19-5.22 | Planned |
| 8 | AI Usage | Custom policy, no direct NIST CSF/ISO 27001 mapping | Planned |

## Tools Used

- Python (Flask) and SQLite for the training and tracking application
- Canva for training visuals and infographics
- Markdown for training content and documentation

## What This Project Demonstrates

- Ability to translate compliance requirements (NIST CSF, ISO 27001) into practical training content
- Instructional design skills applied to a security context, including learning style considerations
- Basic full-stack development skills (Python, Flask, SQLite)
- Ability to design a tracking and reporting system tied to compliance evidence

## Next Steps

- Complete written content for remaining 7 modules
- Design supporting visuals for each module
- Build the Flask application folder structure and database models
- Build routes and templates, tested end to end on the pilot module first
- Implement completion tracking and a compliance-mapped reporting dashboard
