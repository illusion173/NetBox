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
import csv
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
    
        
        self.pythonLibBtn = QPushButton('Python Libray', self)
        self.pythonLibBtn.setIconSize(QSize(200,200))
        self.pythonLibBtn.clicked.connect(self.pythonLib_script)
        
        self.xsltproc = QPushButton('XSLT', self)
        self.xsltproc.setIconSize(QSize(200,200))
        self.xsltproc.clicked.connect(self.xslt_script)
        
        self.metaBtn = QPushButton('Metasploit', self)
        self.metaBtn.setIconSize
        self.metaBtn.clicked.connect(self.meta_script)
                
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
        layoutV.addLayout(layoutH)
        
        self.nmapBtn.hide()
        self.wiressharkBTN.hide()
        self.pythonBtn.hide()
        self.pipBtn.hide()
        self.pythonLibBtn.hide()
        self.xsltproc.hide()
        self.metaBtn.hide()
        self.setLayout(layoutV)
        self.show()
        
    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()
    
    def update_script(self):
        os.system('sudo apt-get update')
        self.nmapBtn.show()
        self.updateBtn.hide()
        
    def nmap_script(self):
        os.system('sudo apt-get install nmap')
        self.wiressharkBTN.show()
        self.nmapBtn.hide()
        
    def wireshark_script(self):
        os.system('sudo apt-get install wireshark')
        self.pythonBtn.show()
        self.wiressharkBTN.hide()
        
    def python_script(self):
        os.system('sudo apt-get python3')
        self.pythonLib_script.show()
        self.pythonBtn.hide()
        
        
    def pythonLib_script(self):
        os.system('sudo pip3 install readline | pip3 install binascii | pip3 install struct | pip3 install textwrap | pip3 install multiprocessing | pip3 install threading | pip3 install queue | pip3 install subprocess | pip3 install time | pip3 install colorama | pip3 install ipaddress | pip3 install python-nmap | pip3 install ipinfo | pip3 install scapy | pip3 install shodan | pip3 install python-whois | pip3 install paramiko | pip3 install netfilterqueue | pip3 install flask | pip3 install PyQt5 | pip3 install beautifulsoup4 | pip3 install lxml | pip3 install parse-nmap ')
        self.pythonLibBtn.hide()
        self.xsltproc.show()

    def xslt_script (self):
        os.system('sudo apt-get install xsltproc')
        self.xsltproc.hide()
        self.metaBtn.show()
    
    def meta_script(self):
        os.system('cd /tmp | curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall | chmod +x msfinstall | sudo ./msfinstall')
        self.metaBtn.hide()

    def runMetaScript(self):
        print("Running MetaScript")
        os.system('msfconsole')
        os.system('load msgrpc')
        time.sleep(20)
        os.system('sudo msfrpcd -P  -f -n -S -a 127.0.0.1')
        self.CreatenewUser = NewUserMenu()        
        self.CreatenewUser.show()
        
class NewUserMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.title = 'New User Registration'
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.mainScreenUI()

    def mainScreenUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        # Create Admin button
        adminCreateBtn = QPushButton('Create', self)
        adminCreateBtn.move(100, 100)
        adminCreateBtn.clicked.connect(self.CreateAdminBtn_OnClick)
        self.adminCreateLabel = QLabel('Create a new admin user', self)
        self.adminCreateLabel.setGeometry(250, 100, 400, 30)


    @pyqtSlot()
    def CreateAdminBtn_OnClick(self):
        self.cams = AdminWindow()
        self.cams.show()
        self.close()

class AdminWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Creating new Admin User')
        self.setWindowIcon(self.style().standardIcon(
            QStyle.SP_FileDialogInfoView))
        self.setFixedSize(480, 480)
        #adminLabel = QLabel(value)
        
        
        pageLayout = QGridLayout()
        # Username Box
        userName = QLabel('<font size="4"> Username </font>')
        self.placeHolderUsername = QLineEdit()
        self.placeHolderUsername.setPlaceholderText('Enter Username')
        pageLayout.addWidget(userName, 0, 0)
        pageLayout.addWidget(self.placeHolderUsername, 0, 1)

        # Password Box
        password = QLabel('<font size="4"> Password </font>')
        self.placeHolderPassword = QLineEdit()
        self.placeHolderPassword.setPlaceholderText('Enter password')
        self.placeHolderPassword.setEchoMode(QLineEdit.EchoMode.Password)
        pageLayout.addWidget(password, 1, 0)
        pageLayout.addWidget(self.placeHolderPassword, 1, 1)

        # Login Button
        self.generalPasswordBtn = QPushButton('Create', self)
        self.generalPasswordBtn.setIconSize(QSize(200, 200))
        self.generalPasswordBtn.clicked.connect(self.CreateActualAdminUser)
        pageLayout.addWidget(self.generalPasswordBtn, 3, 0, 1, 2)
        pageLayout.setRowMinimumHeight(2, 75)
        self.setLayout(pageLayout)
        
        self.goBackBtn = QPushButton(self)
        self.goBackBtn.setStyleSheet(
            'background-color: rgb(0,0,255); color: #fff')
        self.goBackBtn.setText('Go Back!')
        self.goBackBtn.clicked.connect(self.GoMainWindow)
        self.goBackBtn.setGeometry(0,0,480,50)

    def CreateActualAdminUser(self):
        self.placeHolderUsername.setEchoMode(QLineEdit.EchoMode.Normal)
        genPassword = self.placeHolderPassword.text()
        genUsername = self.placeHolderUsername.text()

        if genUsername == '':
            self.ErrorMessage()
        elif genPassword == '':
            self.ErrorMessage()
        else:
            newUserTableAdmin = [[genUsername, genPassword]]
            with open("Admin_Users.csv", "a") as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(newUserTableAdmin)
            
            self.CreatedUser()

    def CreatedUser(self):
        createUser = QMessageBox()
        createUser.setIcon(QMessageBox.Information)
        createUser.setWindowTitle('Accepted')
        createUser.setText(
            'New user has been created! If you wish to make a new user close window and press the Go Back Button')
        createUser.setStandardButtons(QMessageBox.Ok)
        createUser.exec_()

    def ErrorMessage(self):
        username = QMessageBox()
        username.setIcon(QMessageBox.Critical)
        username.setWindowTitle('ERROR')
        username.setText('Please fill in designated area')
        username.setStandardButtons(QMessageBox.Ok)
        username.exec_()

    def GoMainWindow(self):
        self.cams = NewUserMenu()
        self.cams.show()
        self.close()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())