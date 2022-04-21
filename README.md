# Welcome to NetBox: Networking Toolbox

[![License](https://img.shields.io/github/license/illusion173/SE300_Metasploits)](https://github.com/illusion173/SE300_Metasploits/blob/main/LICENSE)
[![Version](https://img.shields.io/badge/Version-B1.0-success)](https://github.com/illusion173/SE300_Metasploits)
[![Issues](https://img.shields.io/github/issues/illusion173/SE300_Metasploits)](https://github.com/illusion173/SE300_Metasploits/issues)
[![Python](https://img.shields.io/badge/Python-3.10-brightgreen)](https://www.python.org/)
## Developed by ERAU students: Jeremiah Webb, Haskell Cappers, Ryan Lucas & Adam Fitch
[![Build](https://img.shields.io/github/illusion173/SE300_Metasploits/actions/workflows/python-app.yml)](https://github.com/illusion173/SE300_Metasploits/actions)

### Requirements
Currrently only runs on debian based Linux sytems with the apt package manager & local administrator on computer with sudo privileges.
Must have Python 3.10, pip and pip3 installed in order for NetBox to function.

### Description
NetBox is a standard Networking Toolbox. Currently the tools within it are the following:
- Wireshark
- Nmap
- Nmap to JSON
- Metasploit Framework
- Logging in Functionality

Please note do *NOT* use these tools under any circumstance in a network unless you have written consent and permission to use NetBox and its inherent tools.

NetBox is mainly used for scanning computers and servers for potential vulnerabilities. If the user wishses to attempt to exploit potential vulnerabilities in a controlled environment, they can do so in the same GUI.

### Language
Python 3.10: https://www.python.org/

## Installation



Run the following command to begin:
After cloning the repo to your desired directory and navigating to the desired directory, run the following commands:
```
sudo apt-get install python3
sudo apt-get install python3-pip
sudo pip3 install PyQt5
sudo python3 SetupGui.py
When in the msfconsole
type in: sudo msfrpcd -P password -f -n -S -a 127.0.0.1
sudo ./runPythonPip.sh

```

After accepting all the needed software to be installed, the GUI will ask for a username and password.

Please remember the username and password. if you lose the username and password all data gotten while using NetBox will be lost.


After running the above command, run this command to run the full application:

```
sudo python3 baseGui.py
```

This will present a login screen, use the username and password you entered to access the application. 

To add users to the program, other administrators or general users, you must be a administrator. 

A general user is only allowed to run Nmap scans, and will not be able to view the scanned data.
