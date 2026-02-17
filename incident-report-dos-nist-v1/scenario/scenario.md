# Scenario

This scenario simulates a network disruption within a multimedia company that provides web design, graphic design, and social media marketing services to small businesses.

The organization experienced a Denial of Service (DoS) attack that disrupted internal network operations for approximately two hours.

The disruption was caused by a large volume of incoming ICMP traffic that overwhelmed network resources. As a result, internal systems became inaccessible and normal business operations were temporarily impacted.

Initial investigation revealed that the firewall had not been properly configured to restrict or limit inbound ICMP traffic. This misconfiguration allowed an external actor to send excessive ICMP packets into the network, ultimately causing service instability.

Following containment efforts, the organization implemented rate limiting, source IP verification, network monitoring tools, and IDS/IPS capabilities to reduce future exposure.

This project focuses on analyzing the incident using the NIST Cybersecurity Framework (CSF) to identify control gaps and define structured improvements across the Identify, Protect, Detect, Respond, and Recover functions.
