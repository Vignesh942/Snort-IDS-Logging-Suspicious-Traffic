# Snort IDS — Logging Suspicious Network Traffic

## Overview
Snort is a powerful open-source network intrusion detection system (IDS) that monitors network traffic and detects suspicious activities based on predefined rules.

In this project, I configured Snort to detect and log suspicious traffic generated during Nmap scans. The setup runs purely in IDS mode (inline mode disabled), meaning Snort only monitors and logs suspicious activity without interfering with the network flow.

The rules used in this setup are the default pre-configured rules — no custom modifications were made to the snort.conf file. The goal was to understand how Snort identifies and logs network anomalies such as port scans or SYN floods using its built-in detection capabilities.

A demo video is included to showcase real-time monitoring and how alerts are generated when suspicious traffic is detected.

## Features
- Real-time monitoring and logging of network traffic
- Detection of common reconnaissance and scanning attacks (e.g., Nmap, SYN floods)
- Automatic logging of suspicious packets for analysis
- Ready for customization with additional Snort rules for advanced use cases

## License
This project is licensed under the MIT License.
