# Access Control Incident Analysis

## Incident Summary

| **Date / Time** | 10/03/2023 at 08:29:57 AM |
| **Event Source** | AdsmEmployeeService |
| **User** | Legal\Administrator (contractor) |
| **IP Address** | 152.207.255.255 |
| **Action** | Unauthorised payroll event — FAUX_BANK |

## Notes

I identified the incident using the event log. The activity originated 
from an account with Administrator permissions at the recorded IP address.

Cross-referencing with the employee directory confirmed the account 
belongs to a contractor whose end date was recorded as 12/27/2019. 
The account was never deactivated.

## Issue

A contractor account with Administrator-level permissions remained active 
more than three years past its end date. This created an unmonitored 
access point that was used to initiate an unauthorised payroll transaction.

The core failure was the absence of a structured offboarding process and 
access review cycle.

## Recommendations

| Control Type | Recommendation |
-------------------------------------------------------------
| **Technical** | Implement RBAC and MFA across all accounts |
| **Operational** | Enforce offboarding process with immediate access revocation on end date; schedule periodic access reviews |
| **Managerial** | Apply Least Privilege Policy — contractors should never hold Administrator permissions by default |

## Key Takeaway

The threat actor didn't need to bypass any technical control. 
The account was simply never closed. Access governance failures 
are as dangerous as technical vulnerabilities.