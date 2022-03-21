import sys
import os
import subprocess

# Please make sure you are in the correct directory that you want the file to be saved in before running the code.
# DO NOT RUN THIS IN ROOT OR SUDO
def wireScan():
    print("Running WireScan Python Scripts ! \n")
    saveFile = input("What would you like the file to be saved as?\n") + ".pcap"
    duration = input("How many seconds would you like for the scan to be?\n")
    command = 'wireshark -i 2 -k -w '+ saveFile + ' -a duration:' + duration
    os.system(command)
