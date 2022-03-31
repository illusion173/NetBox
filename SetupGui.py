import os
import sys
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtCore    import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic       import loadUi
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QHBoxLayout, QPushButton, QVBoxLayout
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import ( QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QStyle,QDialog)
import time
#For some odd reason, warnings are good!
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "NetBox Setup"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.mainScreenUI()
        
    def mainScreenUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        
        
        ContinueBtn = QPushButton('Continue', self)
        ContinueBtn.move(100, 100)
        ContinueBtn.clicked.connect(self.setupBtn_onClick)
        self.contineLabel = QLabel('Continue to run setup commands', self)
        self.contineLabel.setGeometry(250, 100, 400, 30)
        self.show()
    
    @pyqtSlot()
    def setupBtn_onClick(self):
        self.statusBar().showMessage('Importing a Pcap file')
        self.cams = SetupWindow(self.contineLabel.text())
        self.cams.show()
        self.close()
        
class SetupWindow(QDialog):
    def __init__(self, value, parent = None):
        super().__init__(parent)
        self.setWindowTitle("NetBox Setup")
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
        
        label1 = QLabel(value)
        self.updateBtn = QPushButton('Update', self)
        self.updateBtn.setIconSize(QSize(200, 200))
        self.updateBtn.clicked.connect(self.update_script)
        
        self.nmapBtn = QPushButton('Nmap', self)
        self.nmapBtn.setIconSize(QSize(200, 200))
        self.nmapBtn.clicked.connect(self.nmap_script)
        
        self.wiressharkBTN = QPushButton('Wireshark', self)
        self.wiressharkBTN.setIconSize(QSize(200, 200))
        self.wiressharkBTN.clicked.connect(self.wireshark_script)
        
        self.pythonBtn = QPushButton('Python', self)
        self.pythonBtn.setIconSize(QSize(200,200))
        self.pythonBtn.clicked.connect(self.python_script)
        
        self.pipBtn = QPushButton('Python3-Pip', self)
        self.pipBtn.setIconSize(QSize(200,200))
        self.pipBtn.clicked.connect(self.pip_script)
        
        self.pythonLibBtn = QPushButton('Python Libray', self)
        self.pythonLibBtn.setIconSize(QSize(200,200))
        self.pythonLibBtn.clicked.connect(self.pythonLib_script)
        
        self.xsltproc = QPushButton('XSLT', self)
        self.xsltproc.setIconSize(QSize(200,200))
        self.xsltproc.clicked.connect(self.xslt_script)
        
        self.metaBtn = QPushButton('Metasploit', self)
        self.metaBtn.setIconSize
        self.metaBtn.clicked.connect(self.meta_script)
        
        self.adminUsernameLabel = QLineEdit()
        self.adminUsernameLabel.setPlaceholderText('Enter Username')
        username = self.adminUsernameLabel.text()
        self.adminCreatBtn = QPushButton('Create', self)
        self.adminCreatBtn.setIconSize(QSize(200, 200))
        self.adminCreatBtn.clicked.connect(self.adminCreat)
        
        self.passwordLabel = QLineEdit()
        self.passwordLabel.setPlaceholderText('Enter Password')
        self.passwordLabel.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordBtn = QPushButton('Create', self)
        self.passwordBtn.setIconSize(QSize(200, 200))
        self.passwordBtn.clicked.connect(self.passwordCreat)
                
        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Go Back!')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)
        
        layoutH = QHBoxLayout()
        layoutH.addWidget(self.updateBtn)
        layoutH.addWidget(self.nmapBtn)
        layoutH.addWidget(self.wiressharkBTN)
        layoutH.addWidget(self.pythonBtn)
        layoutH.addWidget(self.pipBtn)
        layoutH.addWidget(self.pythonLibBtn)
        layoutH.addWidget(self.xsltproc)
        layoutH.addWidget(self.metaBtn)
        layoutH.addWidget(self.adminUsernameLabel)
        layoutH.addWidget(self.adminCreatBtn)
        layoutH.addWidget(self.passwordLabel)
        layoutH.addWidget(self.passwordBtn)
        layoutV.addLayout(layoutH)
        
        self.nmapBtn.hide()
        self.wiressharkBTN.hide()
        self.pythonBtn.hide()
        self.pipBtn.hide()
        self.pythonLibBtn.hide()
        self.xsltproc.hide()
        self.metaBtn.hide()
        self.adminUsernameLabel.hide()
        self.adminCreatBtn.hide()
        self.passwordLabel.hide()
        self.passwordBtn.hide()
        self.setLayout(layoutV)
        self.show()
        
        
    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()
    
    def update_script(self):
        #os.command('sudo apt-get update')
        self.nmapBtn.show()
        self.updateBtn.hide()
        
    def nmap_script(self):
       # os.command('sudo apt-get install nmap')
        self.wiressharkBTN.show()
        self.nmapBtn.hide()
        
    def wireshark_script(self):
       # os.command('sudo apt-get install wireshark')
        self.pythonBtn.show()
        self.wiressharkBTN.hide()
        
    def python_script(self):
       # os.command('sudo apt-get python3')
        self.pipBtn.show()
        self.pythonBtn.hide()
        
    def pip_script(self):
       # os.command()
        self.xsltproc.show()
        self.pipBtn.hide()
        
    def pythonLib_script(self):
       # os.command('sudo pip3 install readline | pip3 install binascii | pip3 install struct | pip3 install textwrap | pip3 install multiprocessing | pip3 install threading | pip3 install queue | pip3 install subprocess | pip3 install time | pip3 install colorama | pip3 install ipaddress | pip3 install python-nmap | pip3 install ipinfo | pip3 install scapy | pip3 install shodan | pip3 install python-whois | pip3 install paramiko | pip3 install netfilterqueue | pip3 install flask | pip3 install PyQt5 | pip3 install beautifulsoup4 | pip3 install lxml | pip3 install parse-nmap ')
        self.pythonLibBtn.hide()
        self.xsltproc.show()

    def xslt_script (self):
       # os.command('sudo apt-get install xsltproc')
        self.xsltproc.hide()
        self.metaBtn.show()
    
    def meta_script(self):
       # os.command('cd /tmp | curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall | chmod +x msfinstall | sudo ./msfinstall')
        self.metaBtn.hide()
        self.adminUsernameLabel.show()
        self.adminCreatBtn.show()
    
    def runMetaScript(self):
        print("Running MetaScript")
        #os.command('msfconsole')
        #os.command('msgrpc')
        #os.command('sudo msfrpcd -P  -f -n -S -a 127.0.0.1')
                
    def adminCreat(self):
        username = self.adminUsernameLabel.text()
        
        if username == '':
            self.errorMessage()
            self.adminUsernameLabel.clear()
        else:
            self.adminUsernameLabel.hide()
            self.adminCreatBtn.hide()
            self.passwordLabel.show()
            self.passwordBtn.show()
            

        
    def passwordCreat(self):
        self.passwordLabel.setEchoMode(QLineEdit.EchoMode.Normal)
        password = self.passwordLabel.setText()
        if password == '':
            self.errorMessage()
        else:
            self.passwordBtn.show()
        self.passwordLabel.hide()
        self.passwordLabel.hide()
    
    def errorMessage(self):
        username = QMessageBox()
        username.setIcon(QMessageBox.Critical)
        username.setWindowTitle('ERROR')
        username.setText('Please fill in designated area')
        username.setStandardButtons(QMessageBox.Ok)
        username.exec_()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())