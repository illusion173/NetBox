from netaddr import *
import nmap
import sys
import os
from os.path import exists
from colorama import Fore, Back, Style
import json

'''
https://highon.coffee/blog/nmap-cheat-sheet/
'''

def saveFile(nm_json, userInput):
    if os.path.exists("NetworkVerbose.json"):
        with open("NetworkVerbose.json", "w", encoding="utf8") as outfile:
            json.dump(nm_json, outfile, ensure_ascii=False, indent = 4)
    if not os.path.exists("NetworkVerbose.csv"):
        file = open("NetworkVerbose.json", "x")
        with open("NetworkVerbose.json", "w", encoding="utf8") as outfile:
            json.dump(nm_json, outfile, ensure_ascii=False, indent = 4)

def networkScanVerbose(userInput):
    print("Running networkScanVerbose Function")
    try:
        scanner = nmap.PortScanner()
        scanData = scanner.scan(hosts = userInput, arguments = '-v -p 1-65535 -sV -O -sS -T4')
        Output = scanData['scan']
        saveFile(Output, userInput)
    except KeyboardInterrupt:
        sys.exit('\n^C\n')
    except Exception as e: 
        e = sys.exc_info()[1]
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')