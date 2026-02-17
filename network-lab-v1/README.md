# \# Cybersecurity Network Lab v1

# 

### \## Overview

This lab demonstrates the design and implementation of a segmented network using virtualization. The goal is to simulate a realistic environment where internal users, a DMZ server, and external traffic are controlled through a centralized firewall.

# 

### \## Objectives

##### \- Design a segmented network (WAN, LAN, DMZ)

##### \- Implement a firewall acting as both router and security gateway

##### \- Simulate internal clients using different operating systems

##### \- Prepare the environment for firewall rule testing and traffic control

# 

### \## Network Components

##### \- Firewall: pfSense (routing and traffic filtering)

##### \- LAN Clients:

#####   - Windows client

#####   - Ubuntu client

##### \- DMZ - Ubuntu Server

##### \- Virtualization platform: VirtualBox

### 

### \## Network Design

##### The network is divided into three main zones:

##### \- \*\*WAN\*\*: Simulated Internet access

##### \- \*\*LAN\*\*: Internal user network

##### \- \*\*DMZ\*\*: Isolated network for exposed services

##### 

##### All inter-network traffic is routed and filtered by the firewall.

# 

### \## Diagram

##### !\[Network Diagram](diagrams/network-diagram-v1.png)

# 

### \## Status

##### Infrastructure design completed.

##### Next step: VirtualBox network configuration and VM deployment.

# 



