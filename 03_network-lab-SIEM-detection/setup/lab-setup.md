# Lab Setup

## Overview

The lab runs entirely on my personal PC using VirtualBox. Five VMs, three isolated network segments, one central firewall.

> Host has 24 GB RAM. I reduced Splunk from 8 GB to 4 GB to run all VMs simultaneously. Works fine for this scale.

## Virtual Machines

| VM | Role | OS | RAM | CPU | Disk |
|---|---|---|---|---|---|
| pfSense | Firewall / Router | pfSense CE 2.7.2 | 1 GB | 1 core | 20 GB |
| Kali Linux | Attacker | Kali Linux 2025.4 | 4 GB | 2 cores | 80 GB |
| Windows 10 | Victim 1 (LAN) | Windows 10 | 4 GB | 2 cores | 50 GB |
| Ubuntu Server | Victim 2 (DMZ) | Ubuntu Server 24.04.3 LTS | 2 GB | 2 cores | 20 GB |
| Splunk SIEM | SIEM | Ubuntu Server 24.04.3 LTS | 4 GB | 4 cores | 50 GB |

## Network

Each segment is a separate VirtualBox Internal Network. All cross-segment traffic routes through pfSense.

| Segment | Subnet | Gateway | Hosts |
|---|---|---|---|
| LAN (intnet-lan) | 192.168.10.0/24 | 192.168.10.1 | Kali, Windows 10 |
| DMZ (intnet-dmz) | 192.168.20.0/24 | 192.168.20.1 | Ubuntu Server |
| SIEM (intnet-siem) | 192.168.30.0/24 | 192.168.30.1 | Splunk |
| WAN (NAT) | 10.0.2.0/24 | 10.0.2.1 | Internet |

## IP Addresses

| VM | IP |
|---|---|
| Kali Linux | 192.168.10.100 |
| Windows 10 | 192.168.10.101 |
| Ubuntu Server DMZ | 192.168.20.100 |
| Splunk SIEM | 192.168.30.100 |

## Log Forwarding

I installed Splunk Universal Forwarder on all three monitored endpoints. Each forwarder sends to Splunk on port 9997.

| VM | Log Sources |
|---|---|
| Kali Linux | /var/log/auth.log, /var/log/syslog |
| Windows 10 | Security, System, Application Event Logs |
| Ubuntu Server DMZ | /var/log/auth.log, /var/log/syslog |

I had to add static routes on Kali and Ubuntu DMZ so forwarder traffic goes through the correct interface and not the temporary NAT adapter used for file transfers.

## Status

- [x] All VMs connected and receiving correct IPs
- [x] Splunk receiving logs from all 3 hosts
- [x] Static routes persistent after reboot
- [ ] Attack scenario executed
- [ ] Alerts configured in Splunk