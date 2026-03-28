# pfSense Configuration

## Version

pfSense CE 2.7.2 (FreeBSD/amd64)

## Interface Assignment

| Interface | Adapter (VirtualBox) | Network | IP Address | Role |
|---|---|---|---|---|
| WAN | em0 | NAT | 10.0.2.15 (DHCP) | Internet access |
| LAN | em1 | intnet-lan | 192.168.10.1/24 | LAN segment (attacker + victim 1) |
| OPT1 | em2 | intnet-dmz | 192.168.20.1/24 | DMZ segment (victim 2) |
| OPT2 | em3 | intnet-siem | 192.168.30.1/24 | SIEM segment (Splunk) |

## DHCP Server Configuration

I configured pfSense as DHCP server on all internal interfaces.

| Interface | DHCP Range | Gateway |
|---|---|---|
| LAN (em1) | 192.168.10.100 - 192.168.10.200 | 192.168.10.1 |
| OPT1/DMZ (em2) | 192.168.20.100 - 192.168.20.200 | 192.168.20.1 |
| OPT2/SIEM (em3) | 192.168.30.100 - 192.168.30.200 | 192.168.30.1 |

## Firewall Rules

> To be configured. Rules will control cross-segment traffic to simulate realistic network segmentation.

Planned rules:

- LAN to DMZ: allow specific ports only (HTTP, SSH)
- LAN to SIEM: deny direct access
- DMZ to SIEM: allow syslog (UDP 514)
- WAN to LAN/DMZ/SIEM: deny all inbound

## Current Status (28 March 2026)

- [x] Interfaces assigned and active
- [x] DHCP server active on LAN, DMZ, SIEM interfaces
- [x] WAN internet connectivity via NAT
- [ ] Firewall rules configured
- [ ] Logging to Splunk enabled
