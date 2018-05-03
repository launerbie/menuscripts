#!/usr/bin/env python
import subprocess

output = (subprocess.check_output(["amixer", "get", "Master"])).decode()
volumeline = output.split("\n")[-2]

vs = volumeline.split()
vol = vs[3].strip('[]')
state = vs[5].strip('[]')

print("[volume {} {}]".format(vol, state))
