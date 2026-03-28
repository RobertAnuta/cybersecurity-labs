# Lab Setup - Network Environment

## Overview

In this document I describe the virtual lab environment built for cybersecurity practice, specifically for simulating insider threat scenarios and SOC detection workflows.

## Host Machine

- **Hypervisor:** Oracle VirtualBox
- **Host RAM:** 24 GB
- **Host OS:** Windows 11

## Virtual Machines

| VM | Role | OS | RAM | CPU | Disk | Network |
|---|---|---|---|---|---|---|
| pfSense | Firewall / Router | pfSense CE 2.7.2 | 1 GB | 1 core | 20 GB | WAN: NAT, LAN: intnet-lan, DMZ: intnet-dmz, SIEM: intnet-siem |
| Kali Linux | Attacker | Kali Linux 2025.4 | 4 GB | 2 cores | 80 GB | intnet-lan |
| Windows 10 | Victim 1 | Windows 10 | 4 GB | 2 cores | 50 GB | intnet-lan |
| Ubuntu Server | Victim 2 / DMZ | Ubuntu Server 24.04.3 LTS | 2 GB | 2 cores | 20 GB | intnet-dmz |
| Splunk SIEM | SIEM | Ubuntu Server 24.04.3 LTS + Splunk Enterprise | 4 GB | 4 cores | 50 GB | intnet-siem |

> Note: For Splunk VM I reduced the RAM from 8 GB to 4 GB due to host memory constraints. All VMs cannot run simultaneously at full allocation due to my hardware limitation.

## Network Architecture

I configured pfSense to act as the central firewall and router between all network segments. Each segment is isolated as a separate VirtualBox Internal Network.

| Network | Segment | Subnet | Gateway (pfSense) | Hosts |
|---|---|---|---|---|
| LAN | intnet-lan | 192.168.10.0/24 | 192.168.10.1 | Kali (attacker), Windows 10 (victim 1) |
| DMZ | intnet-dmz | 192.168.20.0/24 | 192.168.20.1 | Ubuntu Server (victim 2) |
| SIEM | intnet-siem | 192.168.30.0/24 | 192.168.30.1 | Splunk Enterprise |
| WAN | NAT | 10.0.2.0/24 | 10.0.2.1 | Internet access via host |

## IP Address Assignments

| VM | IP Address | Assignment |
|---|---|---|
| Kali Linux | 192.168.10.100 | DHCP (pfSense) |
| Windows 10 | 192.168.10.101 | DHCP (pfSense) |
| Ubuntu Server DMZ | 192.168.20.100 | DHCP (pfSense) |
| Splunk SIEM | 192.168.30.100 | DHCP (pfSense) |
| pfSense LAN | 192.168.10.1 | Static |
| pfSense DMZ | 192.168.20.1 | Static |
| pfSense SIEM | 192.168.30.1 | Static |

## Software Installed

| VM | Software | Version | Notes |
|---|---|---|---|
| Splunk SIEM | Splunk Enterprise | 10.2.1 | Trial license, boot-start enabled |
| Ubuntu Server DMZ | OpenSSH Server | Latest | For remote administration |
| pfSense | pfSense CE | 2.7.2 | DHCP server active on all interfaces |

## Current Status (28 March 2026)

- [x] pfSense installed and configured with 3 network interfaces
- [x] Kali Linux installed and connected to LAN
- [x] Windows 10 installed and connected to LAN
- [x] Ubuntu Server DMZ installed, updated, SSH enabled
- [x] Splunk SIEM installed, Splunk Enterprise running on boot
- [x] All VMs receiving correct IPs via DHCP
- [x] LAN connectivity verified (Kali ping to pfSense gateway successful)
- [ ] pfSense firewall rules configured
- [ ] Cross-network connectivity tested
- [ ] Splunk web interface configured
- [ ] Log forwarding configured (syslog to Splunk)
- [ ] Attack scenario executed and documented
