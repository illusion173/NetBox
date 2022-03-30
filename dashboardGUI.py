# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from scanComputer import *
from scanNetworkVerbose import *
from scanNetwork import *
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QHBoxLayout, QPushButton, QVBoxLayout
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
import csv

checkedLogin = 0

class HelpWindow(QWidget):
    def __init__(self):
        super(HelpWindow, self).__init__()
        self.resize(400, 300)

        # Label
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 400, 300)
        self.label.setText('Sub Window')
        self.label.setStyleSheet('font-size:40px')


class Dashboard(QWidget):
    def __init__(self):
        super(Dashboard, self).__init__()
        # set the title
        self.setWindowTitle("NetBox")

        self.setFixedSize(1600, 900)
        self.buttonTitle = QLabel("Scans Available", self)
        self.buttonTitle.move(1400, 30)
        self.buttonTitle.setStyleSheet("font-size: 14px;")

       # Assemble Buttons
        self.pushButtonScanComputer = QPushButton("Scan Computer", self)
        self.pushButtonScanComputer.setGeometry(1400, 50, 150, 50)
        self.pushButtonScanNetwork = QPushButton("Scan Network", self)
        self.pushButtonScanNetwork.setGeometry(1400, 100, 150, 50)
        self.pushButtonScanNetworkVerbose = QPushButton(
            "Scan Network Verbose", self)
        self.pushButtonScanNetworkVerbose.setGeometry(1400, 150, 150, 50)
        self.pushButtonHelp = QPushButton("HELP", self)
        self.pushButtonHelp.setGeometry(1400, 200, 150, 50)

        # Assign Functions to buttons
        self.pushButtonScanComputer.clicked.connect(self.takeInputScanComputer)
        self.pushButtonScanNetwork.clicked.connect(self.takeInputScanNetwork)
        self.pushButtonScanNetworkVerbose.clicked.connect(
            self.scanNetworkVerbose)

        self.sub_window = HelpWindow()
        self.pushButtonHelp.clicked.connect(self.sub_window.show)

    # main Functions here
    def takeInputScanComputer(self):
        userIpAddressSingleComputer, done1 = QtWidgets.QInputDialog.getText(
            self, "Single Verbose", "Enter an IP Address: ")
        print(userIpAddressSingleComputer)
        print("Successful Input 1")
        if(userIpAddressSingleComputer != ""):
            runComputerScan(userIpAddressSingleComputer)

    def takeInputScanNetwork(self):
        userIpAddressNetwork, done2 = QtWidgets.QInputDialog.getText(
            self, "Host Discovery", "Enter Network IP Address: ")
        print("Successful Input 2")
        if (userIpAddressNetwork != ""):
            scanLocalDevices(userIpAddressNetwork)

    def scanNetworkVerbose(self):
        userIpAddressNetworkVerbose, done3 = QtWidgets.QInputDialog.getText(
            self, "Network Verbose", "Enter Network IP Address: ")
        print("Successful Input 3")
        if(userIpAddressNetworkVerbose != ""):
            networkScanVerbose(userIpAddressNetworkVerbose)

class createSystem(QWidget):
     def __init__(self, LoginSystem):
          QWidget.__init__(self)
            
class LoginSystem(QWidget):
   
    def __init__(self ):
        super().__init__()
        self.setWindowTitle('NetBox Login')
        self.resize(480, 100)
        pageLayout = QGridLayout()
        #Username Box
        userName = QLabel('<font size="4"> Username </font>')
        self.placeHolderUsername = QLineEdit()
        self.placeHolderUsername.setPlaceholderText('Enter Username')
        pageLayout.addWidget(userName, 0, 0)
        pageLayout.addWidget(self.placeHolderUsername, 0, 1)

        #Password Box
        password = QLabel('<font size="4"> Password </font>')
        self.placeHolderPassword = QLineEdit()
        self.placeHolderPassword.setPlaceholderText('Enter password')
        self.placeHolderPassword.setEchoMode(QLineEdit.EchoMode.Password)
        pageLayout.addWidget(password, 1, 0)
        pageLayout.addWidget(self.placeHolderPassword, 1, 1)
        
        #Show Password Button
        self.showBox = QPushButton('Show',self)
        self.showBox.clicked.connect(self.showPass)      
        pageLayout.addWidget(self.showBox,1,3,1,2)
        pageLayout.setRowMinimumHeight(2,75)
        #Drop Down Box
        self.combobox = qtw.QComboBox(self)
        self.combobox.addItems(['Regular','Administrator'])
        pageLayout.addWidget(self.combobox, 2,0) 
        self.label = QLabel(self)
         
        #Login Button
        self.button_login = QPushButton('Login',self)
        self.button_login.clicked.connect(self.adminUser)
        pageLayout.addWidget(self.button_login, 3, 0, 1, 2)
        pageLayout.setRowMinimumHeight(2, 75)
        self.combobox.resize(20,1)     
        self.setLayout(pageLayout)  
           
    #File Writer Function
        self.fileWriter()

    #Show Password Function
    def showPass(self):
        print("Password has been shown")   
        self.placeHolderPassword.setEchoMode(QLineEdit.EchoMode.Normal)
        
    #Write Files For Demonstration Purposes
    #Normal User
    def fileWriter(self):
        normalUser = [ ['Jack', '123'],
                      ['Joe', '456'],
                      ['Frank', '789'],
                      ['Bob', '321'] ]
        with open("Normal_Users.csv",'w') as csvfile:
            csvwriter =csv.writer(csvfile)
            csvwriter.writerows(normalUser)
        
    #Administrators
        adminUser = [ ['Adam','123'],
                     ['Haskell','456'],
                     ['Jeremiah','789'],
                     ['Ryan','321']]
        with open("Admin_Users.csv",'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(adminUser)
            
    #Display success when admin user logs in
    def adminUser(self):        
        print(self.combobox.currentText())
        if self.combobox.currentText() == "Administrator":
            adminInfo=[]
            msg = QMessageBox()
        #Read File  
            with open("Admin_Users.csv") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    adminInfo.append(row)
            print(adminInfo)
        
            username= str(self.placeHolderUsername.text()) 
            print(username)  
        
            password= str(self.placeHolderPassword.text())
            print(password)
        
            column1 = [col[0] for col in adminInfo]
            column2 = [col[1] for col in adminInfo]        
        
            if username in column1 and password in column2:
                for checkUsers in range(0,len(column1)):
                    if column1[checkUsers] == username and column2[checkUsers] == password:
                        print("Admin Access Granted") 
                        print("Success")
                        msg.setText("Welcome Admin")
                        msg.exec_() 
                        checkedLogin = 1
                        self.newDashboard = Dashboard()
                        self.newDashboard.show()
            else:
                print("Incorrect")
                msg.setText("Username/Password does not exist")
                msg.exec_()
                self.placeHolderPassword.clear()             
    #Normal User Function
        self.normUser()

    #Display success when user logs in       
    def normUser(self):
        if self.combobox.currentText() == "Regular":
            print("Normal Access")
            normInfo=[]
            msg = QMessageBox()
                #Read File  
            with open("Normal_Users.csv") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    normInfo.append(row)
                print(normInfo)
        
                username= str(self.placeHolderUsername.text()) 
                print(username)  
        
                password= str(self.placeHolderPassword.text())
                print(password)
        
                column1 = [col[0] for col in normInfo]
                column2 = [col[1] for col in normInfo]
        
                if username in column1 and password in column2:
                    for checkUsers in range(0,len(column1)):
                        if column1[checkUsers] == username and column2[checkUsers] == password:
                            print("Success")
                            msg.setText("Welcome")
                            msg.exec_()
                    
                else:
                    print("Incorrect")
                    msg.setText("Username/Password does not exist")
                    msg.exec_()  
                    self.placeHolderPassword.clear()
                    

if __name__ == "__main__":
    # create pyqt5 app
    app = QApplication(sys.argv)
    # create the instance of our Window
    form = LoginSystem()
    form.show()
    # start the app
    sys.exit(app.exec())
