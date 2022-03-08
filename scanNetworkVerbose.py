import socket
from netaddr import *
import nmap
import sys
import os
from os.path import exists
from colorama import Fore, Back, Style
import subprocess
import json

'''
https://highon.coffee/blog/nmap-cheat-sheet/
'''

print("Scan Network Verbose Script running...\n")

userInput = 'scanme.nmap.org'
scanner = nmap.PortScanner()

def saveFile(nm_json):
    if os.path.exists("NetworkScanoutput.json"):
        with open("NetworkScanoutput.json", "w", encoding="utf8") as outfile:
            json.dump(nm_json, outfile, ensure_ascii=False, indent = 4)
    if not os.path.exists("NetworkScanoutput.csv"):
        file = open("NetworkScanoutput.json", "x")
        with open("NetworkScanoutput.json", "w", encoding="utf8") as outfile:
            json.dump(nm_json, outfile, ensure_ascii=False, indent = 4)

def networkScanVerbose():
    try:
        scanData = scanner.scan(hosts = userInput, arguments = '-v -p 1-65535 -sV -O -sS -T4')
        Output = scanData['scan']
        saveFile(Output)
    except KeyboardInterrupt:
        sys.exit('\n^C\n')
    except Exception as e: 
        e = sys.exc_info()[1]
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')

networkScanVerbose()


print("Done scanning...\n")