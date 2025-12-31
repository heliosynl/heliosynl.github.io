---
title: "Ubuntu Network Setting Record"
date: 2025-12-31
excerpt: 'Ubuntu Network Setting Record'
type: record
tags:
  - record
---

Content
=====
{:.no_toc}

* toc
{:toc}

# Using LAN network connect
register the network card in HKU [here](https://its.hku.hk/kb/network-card-registration/)

# Locking the IP address (general)
## Ubuntu
first DHCP connection
### check current address, gateway, DNS, netmask
```sh
nmcli device show
```

output:
```sh
...
IP4.ADDRESS[1]:                         10.64.87.3/23
IP4.GATEWAY:                            10.64.86.1
IP4.ROUTE[1]:                           dst = 10.64.86.0/23, nh = 0.0.0.0, mt = 100
IP4.ROUTE[2]:                           dst = 0.0.0.0/0, nh = 10.64.86.1, mt = 100
IP4.DNS[1]:                             147.8.235.74
IP4.DNS[2]:                             147.8.235.73
IP4.DOMAIN[1]:                          hku.hk
...
```

- address: 10.64.87.3
- gateway: 10.64.86.1
- DNS: 147.8.235.74
- netmask: /23
  - netmask need to change into CIDR form
  - for instance, /24 : 255.255.255.0
    - /23: 255.255.254.0
    - /25: 255.255.255.1
  - original 255.255.255.255 correspond to /32, meaning there are 32 number 1 in 255.255.255.255 (11111111.11111111.11111111.1111111)
  - so /24 meaning 24 number 1 (11111111.11111111.11111111.0)

### Setting
- Settings
  - Network
    - Wired, gear on the side
      - IPv4 Method: Manual
      - Addresses: use address, netmask, gateway above
      - DNS: use DNS server above
      - Apply