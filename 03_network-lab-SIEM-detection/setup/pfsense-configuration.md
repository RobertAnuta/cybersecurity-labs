# pfSense Configuration

**Version:** pfSense CE 2.7.2 (FreeBSD/amd64)

## Interface Assignment

| Interface | Adapter | Network | IP | Role |
|---|---|---|---|---|
| WAN | em0 | NAT | 10.0.2.15 (DHCP) | Internet |
| LAN | em1 | intnet-lan | 192.168.10.1/24 | LAN segment |
| OPT1 | em2 | intnet-dmz | 192.168.20.1/24 | DMZ segment |
| OPT2 | em3 | intnet-siem | 192.168.30.1/24 | SIEM segment |

## DHCP

pfSense handles DHCP for all internal segments.

| Interface | Range | Gateway |
|---|---|---|
| LAN | 192.168.10.100 - .200 | 192.168.10.1 |
| OPT1 / DMZ | 192.168.20.100 - .200 | 192.168.20.1 |
| OPT2 / SIEM | 192.168.30.100 - .200 | 192.168.30.1 |

## Firewall Rules

Rules apply on the inbound interface. Traffic from DMZ to SIEM is controlled on OPT1, not OPT2.

**OPT1 (DMZ)**

| Action | Protocol | Source | Destination | Port | Description |
|---|---|---|---|---|---|
| Pass | IPv4 | OPT1 subnet | any | any | Allow DMZ outbound |
| Pass | IPv4 TCP | OPT1 subnet | 192.168.30.100 | 9997 | Allow DMZ to Splunk |

**LAN** uses the default allow rule (LAN subnets to any).

**OPT2 (SIEM)** allows outbound traffic from the SIEM subnet.

## NAT

Left on Automatic. pfSense created outbound NAT rules for all three internal subnets automatically.

## Static Routes on VMs

Adding a second NAT adapter for file transfers created routing conflicts on Kali and Ubuntu DMZ. Fixed with persistent static routes:

**Ubuntu DMZ** (netplan):
```yaml
routes:
  - to: 192.168.30.0/24
    via: 192.168.20.1
```

**Kali** (/etc/network/interfaces):
```
up ip route add 192.168.30.0/24 via 192.168.10.1 dev eth0
```

**Windows 10**:
```
route add 192.168.30.0 mask 255.255.255.0 192.168.10.1 -p
```

## Status

- [x] All interfaces active
- [x] DHCP running on all internal interfaces
- [x] Firewall rules configured and tested
- [x] DMZ to Splunk forwarding verified (port 9997)
- [ ] pfSense log forwarding to Splunk (future)