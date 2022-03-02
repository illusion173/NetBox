import socket
from netaddr import *
import nmap
import sys
import os
from os.path import exists
from colorama import Fore, Back, Style
import subprocess
import json

print("****************************************************\n")
print("Running ScanNetworkVerbose on Network")
print("Are you sure you want to scan entire network?")
print("Input 1 (MOST VERBOSE AND TIME CONSUMING): Prints verbose output, runs stealth syn scan, T5 timing, OS and version detection + full port range scan.")
print("Input 2: Full TCP Port Scan detection")
print("Input 3: Prints verbose output, runs stealth syn scan, T4 timing, OS and version detection + traceroute and scripts against target services.")
print("Input 4: to exit the program.")
userInput = input('Please input your selection: ')


'''
Essentially a boogie af switch statement.
'''
if userInput == '1':

if userInput == '2':


if userInput == '3':


if userInput == '4':



proc = subprocess.check_output("ifconfig").decode('utf-8')
print (proc)
print("****************************************************\n")
print("Popular Subnet CIDR Notations:\n")
print("255.255.255.255 = /32")
print("255.255.255.254 = /31")
print("255.255.255.0 = /24")
print("255.255.254.0 = /23")
print("255.255.0.0 = /16\n")
print("****************************************************\n")