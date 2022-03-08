import os

#use http://scanme.nmap.org for testing purposes only!

def runComputerScan(userInputtedIP):
    print("Running runComputerScan Function")
    oscommmand = ('nmap -A -O -oX' + userInputtedIP +'.xml ' + 'userInputtedIP')
    os.system(oscommmand)
    osconvert = ('xsltproc' + ' '  + userInputtedIP +'.xml ' + '-o' + '' + userInputtedIP + '.html')
    os.system(osconvert)
