import socket
from netaddr import *
import nmap
import sys
import os
from os.path import exists
from colorama import Fore, Back, Style
import subprocess
import json


def saveFile(nm_json):
    if os.path.exists("NetworkScanoutput.json"):
        with open("NetworkScanoutput.json", "w", encoding="utf8") as outfile:
            json.dump(nm_json, outfile, ensure_ascii=False, indent = 4)
    if not os.path.exists("NetworkScanoutput.csv"):
        file = open("NetworkScanoutput.json", "x")
        with open("NetworkScanoutput.json", "w", encoding="utf8") as outfile:
            json.dump(nm_json, outfile, ensure_ascii=False, indent = 4)
        
scanner = nmap.PortScanner()

def scanLocalDevices(network):
    print("Running scanLocalDevices Function")
    try:
        print(f'[{Fore.YELLOW}?{Style.RESET_ALL}] Scanning for devices on {Fore.YELLOW}{network}{Style.RESET_ALL} network...') 
        scanData = scanner.scan(hosts = network, arguments = '-v -sn -sP')
        Output = scanData['scan']
        saveFile(Output)
    except KeyboardInterrupt:
        sys.exit('\n^C\n')
    except Exception as e: 
        e = sys.exc_info()[1]
        print(f'[{Fore.RED}!{Style.RESET_ALL}] Error: {Fore.RED}{e}{Style.RESET_ALL}')
    else:
        for host in scanner.all_hosts():
            if scanner[host]['status']['state'] == 'up':
                try:
                    if len(scanner[host]['vendor']) == 0:
                        try:
                            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] {host}      \t {socket.gethostbyaddr(host)[0]}")
                        except:
                            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] {host}")
                    else:
                        try:
                            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] {host}      \t {scanner[host]['vendor']}      \t {socket.gethostbyaddr(host)[0]}")
                        except:
                            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] {host}      \t {scanner[host]['vendor']}") 
                except:
                    print(f"[{Fore.GREEN}+{Style.RESET_ALL}] {host}      \t {scanner[host]['vendor']}")

