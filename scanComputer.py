import os

#use http://scanme.nmap.org for testing purposes only!
userInputtedIP = "http://scanme.nmap.org"

def runComputerScan():
    oscommmand = ('nmap -A -O -oX' + userInputtedIP +'.xml ' + 'userInputtedIP')
    os.system(oscommmand)
    osconvert = ('xsltproc' + ''  + userInputtedIP +'.xml ' + '-o' + '' + userInputtedIP + '.html')
    os.system(osconvert)
