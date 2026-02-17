# Incident Report – DoS Attack Analysis (NIST CSF)

## Context

In this project, I analyzed a Denial of Service (DoS) incident affecting a multimedia company that provides web design, graphic design, and social media marketing services to small businesses.

The organization experienced a two-hour internal network outage caused by a flood of ICMP packets. The disruption prevented access to internal systems and significantly impacted operational continuity.

I used the NIST Cybersecurity Framework (CSF) to structure my analysis, identify control gaps, and develop a practical security improvement plan.

## Objective

Through this project, I aimed to:

- Analyze the root cause of the ICMP-based DoS attack  
- Evaluate control failures and monitoring weaknesses  
- Assess operational and business impact  
- Map findings to the NIST CSF functions  
- Propose structured and prioritized security improvements  

## Incident Summary

- **Attack Type:** ICMP Flood (Denial of Service)  
- **Entry Vector:** Unconfigured firewall  
- **Impact Duration:** 2 hours  
- **Primary Impact:** Internal network services became unavailable  
- **Root Cause:** Lack of ICMP rate limiting and insufficient firewall configuration  

## Key Findings

During my analysis, I identified the following critical weaknesses:

- The firewall allowed unrestricted inbound ICMP traffic  
- No rate limiting mechanism was implemented  
- Monitoring capabilities were insufficient to detect abnormal traffic early  
- The response was reactive rather than based on a predefined incident plan  
- IDS/IPS controls were implemented only after the incident occurred  

These gaps significantly increased the organization’s exposure to volumetric network attacks.

## Project Structure

- `case-study/incident-report.md`  
  My detailed technical breakdown of the incident, including timeline, impact assessment, and root cause analysis.

- `incident-analysis/nist-csf-improvement-plan.md`  
  My structured security improvement plan mapped to the NIST Cybersecurity Framework (Identify, Protect, Detect, Respond, Recover).

- `references/framework-and-concepts.md`  
  Supporting explanations of the NIST CSF and the technical concepts referenced throughout the project.

## Takeaway

Working through this incident helped me understand how small configuration gaps can scale into operational disruption. The firewall was not “broken”, it was simply incomplete. That distinction matters.

What stood out to me most was how the organization relied on reactive containment instead of structured preparation. The network was restored, but the visibility and monitoring gaps remained a risk until addressed properly.

Applying the NIST CSF forced me to think beyond the attack itself. Instead of focusing only on blocking ICMP traffic, I had to consider governance, monitoring maturity, incident readiness, and long-term resilience.

This project strengthened my ability to analyze not just what happened, but why it was possible, and how structured improvements reduce future exposure.

