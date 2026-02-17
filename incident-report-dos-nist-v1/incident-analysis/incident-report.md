# Incident Report Analysis

## Summary

In this project, I analyzed a Denial of Service (DoS) attack that disrupted a multimedia company’s internal network for approximately two hours. The attack was caused by a large number of ICMP packets sent into the network, which prevented normal internal traffic from accessing essential systems.

The main issue was an unconfigured firewall that allowed unrestricted inbound ICMP traffic. Because there was no rate limiting or traffic monitoring in place, the network became overloaded before the issue was identified and contained.

I structured my analysis using the NIST Cybersecurity Framework to evaluate control gaps and define practical improvements.

## Identify

During my review, I identified weaknesses in configuration management and network oversight:

- Firewall rules were not fully reviewed or documented  
- There was no regular audit of inbound traffic policies  
- Risk assessments did not focus on network exposure  
- The dependency on internal network availability was high, but not formally assessed  

The incident was not caused by advanced techniques. It was the result of incomplete configuration and limited visibility.

## Protect

From a protection perspective, the organization lacked preventive controls that could have reduced the impact:

- No ICMP rate limiting was configured  
- Source IP validation was not enabled  
- Firewall configuration standards were not clearly defined  

After the incident, improvements included:

- Implementing ICMP rate limiting  
- Enforcing source IP verification  
- Reviewing and tightening firewall rules  

These changes reduce the likelihood of similar disruptions.

## Detect

Detection capabilities were limited before the incident:

- No alerts were configured for unusual traffic spikes  
- Network monitoring was not proactive  
- IDS/IPS controls were introduced only after the attack  

This meant the organization reacted only after services were already affected.

Improving monitoring and alerting significantly reduces detection time and limits impact.

## Respond

The response actions were effective but reactive:

- Incoming ICMP traffic was blocked  
- Non-critical services were temporarily taken offline  
- Critical systems were restored once stability returned  

There was no predefined response plan specifically addressing network flooding scenarios. This increased reliance on manual decision-making during the incident.

## Recover

Recovery focused on restoring availability and stabilizing core services. Once traffic was controlled, systems were gradually brought back online.

The incident highlighted the importance of:

- Documented incident response procedures  
- Post-incident review  
- Continuous configuration validation  
- Ongoing monitoring improvements  

Using the NIST CSF framework helped me structure the analysis beyond what happened, focusing instead on why it happened and how to reduce the risk moving forward.
