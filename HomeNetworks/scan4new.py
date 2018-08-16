#!/usr/bin/env python
print ('begin scan4new.py\n')
# imports
import socket
import fcntl
import struct
import sys  
import multiprocessing
import subprocess
import os

#interface and netmask hardcoded
ifname = 'wlan0'
netmask = 24
#get my local ip
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
myIp = s.getsockname()[0]
print('mon ip: ' + myIp )
s.close()
ip_parts = myIp.split('.')
base_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'+'0'
print('ip du reseau: ' + base_ip)

print ('\nend scan4new.py')