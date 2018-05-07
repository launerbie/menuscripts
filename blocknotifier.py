#!/usr/bin/env python3

import sys
import time
import os
import subprocess
import json
from datetime import datetime

HOME = os.environ['HOME']
PIPEREADER = HOME+"/pipes/pipereader"

def slowflush(message, socket, delay=0.03):
    temp = sys.stdout
    sys.stdout = open(socket, 'w')

    for i in range(len(message)):
        print(message[:i+1])
        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.close()
    sys.stdout = temp

#dict -> int
def block_height(block):
    return int(block['data']['height'])

#dict -> dict -> bool
def is_new_block(current, new):
    print("new:", block_height(new), type(new))
    print("current:", block_height(current), type(current))
    if block_height(new) > block_height(current):
        return True
    else:
        return False

#dict -> string
def block_summary(block):
    timestamp = int(block['data']['timestamp'])
    t = datetime.fromtimestamp(timestamp)
    s = "Height:{height} Txs:{tx_count} Fees:{reward_fees} Time:{time}".format(**block['data'], **{'time':t})
    return s

#dict
def get_latest():
    output = subprocess.check_output(['curl', 'https://chain.api.btc.com/v3/block/latest'])
    block = json.loads(output.decode())
    return block

#dict
def prime_the_system():
    block = get_latest()
    msg = "Current block: "+ block_summary(block)
    slowflush(msg, PIPEREADER)
    time.sleep(15)
    return block

#dict -> None
def loop_update_latest(startingblock):
    currentblock = startingblock
    foundnew = False
    calledprocesserror = False
    while True:
        try:
            block = get_latest()
            if is_new_block(currentblock, block):
                msg = "New block found! "+ block_summary(block)
                slowflush(msg, PIPEREADER)
                currentblock = block
                foundnew = True
            elif foundnew == True or calledprocesserror == True:
                msg = "Latest block: "+ block_summary(block)
                slowflush(msg, PIPEREADER)
                foundnew, calledprocesserror = (False, False)
            else:
                pass
            time.sleep(30)
        except subprocess.CalledProcessError:
            calledprocesserror = True
            timeout(60)

#None
def timeout(seconds):
    msg = "Failed to get block from API. Waiting "+str(seconds)+" seconds before trying again."
    slowflush(msg, PIPEREADER)
    time.sleep(seconds)

#None
def main():
    try:
        latestblock = prime_the_system()
        loop_update_latest(latestblock)
    except subprocess.CalledProcessError:
        timeout(60)

if __name__ == '__main__':
    while True:
        main()

