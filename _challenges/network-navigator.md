---
layout: challenge
title: "Network Navigator"
difficulty: Medium
category: Network Analysis
questions:
  - title: "Identify the Exfiltration Method"
    description: "What protocol is being used to exfiltrate data in the captured traffic?"
    answer: "dns"
  - title: "Data Destination"
    description: "What is the IP address of the server receiving the exfiltrated data?"
    answer: "192.168.1.100"
  - title: "Hidden Message"
    description: "What is the decoded message being sent in the DNS queries?"
    answer: "operation_shadowfall"
files:
  - name: "capture.pcap"
    path: "/assets/challenges/network-navigator/capture.pcap"
  - name: "network_topology.png"
    path: "/assets/challenges/network-navigator/network_topology.png"
hints:
  - "Look for unusual patterns in DNS query names"
  - "Check the timing between packets"
  - "Base64 encoding is commonly used in DNS exfiltration"
---

## Background
Security teams have detected suspicious network traffic originating from a corporate workstation. The traffic appears to be using a covert channel to exfiltrate sensitive data. Your task is to analyze the captured traffic and identify the method being used.

## Objective
Using the provided packet capture:
1. Identify the protocol being used for data exfiltration
2. Find the destination of the exfiltrated data
3. Decode the hidden message in the traffic

## Tools Recommended
- Wireshark
- NetworkMiner
- tshark

## Analysis Steps
1. Examine the packet capture file
2. Look for unusual patterns in:
   - DNS queries
   - HTTP headers
   - Timing intervals
3. Decode any suspicious data
4. Document the exfiltration method

## Notes
- All required data is contained within the packet capture
- Focus on anomalous traffic patterns
- Consider timing-based covert channels

Remember to document your analysis methodology and any tools used during the investigation.
