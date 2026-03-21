# Access Control Incident — Unauthorised Payroll Transaction

## Overview

A growing business detected an unauthorised deposit made to an unknown 
bank account. The finance manager confirmed no legitimate transaction 
was initiated. I was tasked with investigating the incident and 
identifying how it happened.

What I found interesting was the moment I cross-referenced the event 
log data with the employee directory, the same IP address, timestamp, 
and account pointed directly to a contractor with Administrator 
permissions whose account should have been deactivated years earlier. 
That connection made the impact immediately clear.

## Scenario

The investigation started with a single event log entry. From there, 
I traced the activity back to an account that had no business being 
active, and certainly not with Admin-level access.

## Skills Demonstrated

- Event log analysis
- Access control review
- Threat identification through data correlation
- Security recommendations across technical, operational 
  and managerial controls

## Files

- [`access-control-analysis.md`](./access-control-analysis.md) — 
  full investigation findings, identified issues, and recommendations

## Takeaway

This project reinforced that access governance failures can be just 
as damaging as technical vulnerabilities. The attacker didn't need 
to break anything — the door was already open.