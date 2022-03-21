import os

def runComputerScan(userInputtedIP):
    print("Running runComputerScan Function")
    oscommmand = ('nmap -v -A -O -oX ' + userInputtedIP +'.xml ' + userInputtedIP)
    os.system(oscommmand)
    osconvert = ('xsltproc' + ' '  + userInputtedIP +'.xml ' + '-o ' + userInputtedIP + '.html')
    os.system(osconvert)
