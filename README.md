# Smurf Attack Demo

An educational demonstration of how a Smurf-attack packet is constructed: a single ICMP echo request is built with a spoofed source IP and addressed to a broadcast address, then its headers are printed and one packet is sent.

This is a teaching aid for understanding IP spoofing and ICMP broadcast amplification. Use it only on networks and systems you own or are explicitly authorized to test, in an isolated lab. Do not use it against any network without permission.

## Features

- Uses Scapy to craft an `IP`/`ICMP` packet with a spoofed source and a broadcast destination
- Prints the constructed packet's header details
- Sends a single packet (`count=1`) to illustrate the mechanism, not to flood

## Built with

- Python 3
- Scapy

## Run it

```bash
python -m venv .venv && source .venv/bin/activate
pip install scapy
sudo python demo.py   # raw sockets require elevated privileges
```

Educational / authorized-lab use only.
