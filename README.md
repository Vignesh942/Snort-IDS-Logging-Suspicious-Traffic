# Snort IDS Logging Suspicious Network Traffic

## Overview
Snort is a powerful open source network intrusion detection system (IDS) that monitors network traffic and detects suspicious activities based on predefined rules.


This Project demonstrates a home lab using **Snort (IDS)** installed on **Linux Mint** to monitor and log suspicious network activity. A separate machine (Kali) was used to generate test traffic (Nmap scans). Snort captures alerts on the Mint host and writes them to the alert log. A small Python script is included to tail the alert file and print readable notifications.

The setup runs purely in IDS mode (inline mode disabled), meaning Snort only monitors and logs suspicious activity without interfering with the network flow.


## Features
- Real time monitoring and logging of network traffic
- Detection of common reconnaissance and scanning attacks (e.g., Nmap, SYN floods)
- Automatic logging of suspicious packets for analysis
- Ready for customization with additional Snort rules for advanced use cases




