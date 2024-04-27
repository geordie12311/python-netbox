"""
Python Script using pynetbox
to add devices from a text file
to Netbox
"""

import pynetbox
import time

device = "Test1"

def adddev(dev):
    nb = pynetbox.api(url='http://192.168.1.20/',
                      token='b26141e2f8e529817fa9644c4cf013ed56b02be7')

    result = nb.dcim.devices.create(
        name=dev,
        device_type=1,
        role=2,
        site=3,
    )
    print(result)

file1 = open('device-list.txt')
Lines = file1.readlines()
count = 0
# Strips the newline character
for line in Lines:
    count +=1
    time.sleep(0.5)
    dev = line
    adddev(dev)