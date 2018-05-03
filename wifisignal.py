#!/usr/bin/env python3
from subprocess import check_output
"""
Reads the output of

  nmcli -t -f active,ssid,bars dev wifi

and prints either [No wifi] or [ssid:signal].
"""

fields = "active,ssid,signal"
output_raw = check_output(["nmcli", "-t", "-f", fields, "dev", "wifi"])
output = output_raw.decode()
networks = output.splitlines()

def active(n):
    if n.split(':')[0] == 'yes':
        return True
    else:
        return False

active_networks = [n for n in networks if active(n)]

if len(active_networks) == 0:
    print("[No WiFi]")
else:
    active, ssid, signal = active_networks[0].split(':')
    print("[{}:{}]".format(ssid, signal))

