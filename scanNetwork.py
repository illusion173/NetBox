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
for some reason issue with nmap module not being found
MAKE SURE TO RUN IN SUDO OR ROOT!
To install nmap for python:
1. sudo apt-get update
2. sudo apt-get install nmap
3. sudo apt-get install python3
4. sudo apt-get install pip3
5. sudo pip install python-nmap
6. sudo pip install colorama
'''
print("Running scanNetwork Python Script!\n")
print("I am running!\n")

def saveFile(nm_json):
    if os.path.exists("NetworkScanoutput.json"):
        with open("NetworkScanoutput.json", "w", encoding="utf8") as outfile:
            json.dump(nm_json, outfile, ensure_ascii=False, indent = 4)
    if not os.path.exists("NetworkScanoutput.csv"):
        file = open("NetworkScanoutput.json", "x")
        with open("NetworkScanoutput.json", "w", encoding="utf8") as outfile:
            json.dump(nm_json, outfile, ensure_ascii=False, indent = 4)
        
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
        print(IP)
    return IP

ipValue = IPNetwork(get_ip())
scanner = nmap.PortScanner()

print("****************************************************\n")
print("Printing ifconfig for IP input")
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

def scanLocalDevices():

    network = input('Please type the network you want to scan (Example: 192.168.1.0/24): ')

    print(f'The network address is {network}')

    try:
        print(f'[{Fore.YELLOW}?{Style.RESET_ALL}] Scanning for devices on {Fore.YELLOW}{network}{Style.RESET_ALL} network...') 
        scanData = scanner.scan(hosts = network, arguments = '-v -sn')
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
scanLocalDevices()

