# Framework and Technical References

## NIST Cybersecurity Framework (CSF)

For this project, I used the NIST Cybersecurity Framework as a structured method to analyze the incident and organize improvement actions.

The CSF is built around five core functions:

- Identify  
- Protect  
- Detect  
- Respond  
- Recover  

Instead of treating the incident as a one-time technical failure, the framework helped me evaluate gaps across governance, prevention, monitoring, and recovery processes.

## Denial of Service (DoS)

A Denial of Service attack aims to disrupt normal system availability by overwhelming network or system resources.

In this case, the disruption was caused by a high volume of ICMP packets sent into the internal network, which exhausted available capacity and prevented legitimate traffic from functioning properly.

## ICMP (Internet Control Message Protocol)

ICMP is a network protocol used primarily for diagnostic purposes, such as the `ping` command.

Although it is legitimate and necessary for network troubleshooting, unrestricted ICMP traffic can be abused to overload systems if proper controls are not configured.

## Firewall Configuration

A firewall controls inbound and outbound network traffic based on defined rules.

In this incident, the firewall was not properly configured to limit ICMP traffic or validate incoming source addresses. This misconfiguration created unnecessary exposure.

## IDS/IPS (Intrusion Detection and Prevention Systems)

IDS monitors traffic for suspicious patterns and generates alerts.

IPS can actively block or filter malicious traffic based on predefined rules.

In this scenario, IDS/IPS capabilities were introduced after the incident to improve monitoring and reduce detection time.

