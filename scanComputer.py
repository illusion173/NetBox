import os


def runComputerScan(userInputtedIP):
    print("Running runComputerScan Function")
    oscommmand = ('sudo nmap -v -A -O -oX ' + userInputtedIP +'.xml ' + userInputtedIP)
    os.system(oscommmand)
    osconvert = ('sudo xsltproc' + ' '  + userInputtedIP +'.xml ' + '-o ' + userInputtedIP + '.html')
    os.system(osconvert)


