from ppadb.client import Client as AdbClient

import time
import subprocess
import os
import sys




client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()

if len(devices) == 0:
    print("No devices attached")
    quit()
device = devices[0]
while True:
    device.shell(f'input touchscreen tap 565 1075')
    # print("pressing")

