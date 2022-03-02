import json
import os
from flask import Flask, request, render_template

'''
things installed
pip install flask
sudo apt-get install xsltproc

app = Flask(__name__)
@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    variable = request.form['userInput']
    return variable

#establish user inputted IP from the website
userInputtedIP = my_form_post()
'''
userInputtedIP = 'scanme.nmap.org'
print("Running Intensive scan on computer IP: " + userInputtedIP+"\n")
oscommmand = ('nmap -A -O -oX' + 'userInputtedIP' +'.xml ' + 'userInputtedIP')
os.system(oscommmand)
osconvert = ('xsltproc' + ' userInputtedIP' +'.xml ' + '-o' + ' userInputtedIP' + '.html')
os.system(osconvert)
print("Confirm Existance of new HTML\n")
osLs = ('ls -l')
os.system(osLs)