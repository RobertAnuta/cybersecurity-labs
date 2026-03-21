# Incident Report — DoS Attack Analysis (NIST CSF)

## Overview

I analyzed a Denial of Service (DoS) incident affecting a multimedia 
company whose internal network was disrupted for approximately two hours 
by an ICMP flood attack. The root cause was a misconfigured firewall with 
no rate limiting or traffic monitoring in place.

I used the NIST Cybersecurity Framework to structure my analysis across 
all five functions: Identify, Protect, Detect, Respond, and Recover.

## Incident Summary

**Attack Type**: ICMP Flood (Denial of Service)
**Entry Vector**: Misconfigured firewall (no ICMP restrictions)
**Impact Duration**: ~2 hours
**Root Cause**: No rate limiting, no traffic monitoring, no IDS/IPS

## Skills Demonstrated:

- Incident analysis using NIST CSF
- Root cause identification and control gap assessment
- Security improvement planning

## Files

- [`incident-report.md`](./incident-report.md): full analysis mapped 
to NIST CSF functions with findings and recommended improvements

## Takeaway

Working through this incident helped me understand how small 
configuration gaps can scale into operational disruption. The firewall 
was not broken, it was simply incomplete. That distinction matters.

What stood out most was how the organization relied on reactive 
containment instead of structured preparation. The network was restored, 
but the visibility and monitoring gaps remained a risk until addressed.

Applying the NIST CSF forced me to think beyond the attack itself, not 
just how to block ICMP traffic, but how to improve governance, monitoring 
maturity, and incident readiness across the board.