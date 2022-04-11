# -*- coding: utf-8 -*-
import webbrowser
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from scanComputer import *
from scanNetworkVerbose import *
from scanNetwork import *
from PyQt5.QtWidgets import QStatusBar, QFileDialog, QComboBox, QStyle, QDialog, QMainWindow, QAction, QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QWidget, QLabel, QApplication, QHBoxLayout, QPushButton, QVBoxLayout, QMenu
import csv
import os
from PyQt5.uic import loadUi
from fileinput import filename
from exploitTest import *
fileCreate = ""
checkedLogin = 0


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'NetBox - WireShark'
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.mainScreenUI()

    def mainScreenUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        # import Pcap button
        importBtn = QPushButton('Import', self)
        importBtn.move(100, 100)
        importBtn.clicked.connect(self.importBtn_onClick)
        self.importLable = QLabel('Import a Pcap file', self)
        self.importLable.setGeometry(250, 100, 400, 30)

        # create new Pcap file
        createBtn = QPushButton('Create', self)
        createBtn.move(100, 200)
        createBtn.clicked.connect(self.createBtn_onClick)
        self.createLineEdit = QLabel('Create a new Pcap file', self)
        self.createLineEdit.setGeometry(250, 200, 400, 30)

        convertBtn = QPushButton('Convert', self)
        convertBtn.move(100, 300)
        convertBtn.clicked.connect(self.convertBtn_onClick)
        self.convertLabel = QLabel('Convert .pcap file to HTML')
        self.convertLable = (250, 300, 400, 30)

    @pyqtSlot()
    def importBtn_onClick(self):
        #self.statusBar().showMessage('Importing a Pcap file')
        self.cams = ImportWindow(self.importLable.text())
        self.cams.show()
        self.close()

    @pyqtSlot()
    def createBtn_onClick(self):
       # self.statusBar().showMessage('Create New Pcap file')
        self.cams = createWindow(self.createLineEdit.text())
        self.cams.show()
        self.close()

    @pyqtSlot()
    def convertBtn_onClick(self):
       # self.statusBar().showMessage('Converting pcap file to html')
        self.cams = ImportWindow(self.importLable.text())
        self.cams.show()
        self.close()


class ImportWindow(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Importing')
        self.setWindowIcon(self.style().standardIcon(
            QStyle.SP_FileDialogInfoView))
        self.filename = QLineEdit()

        label1 = QLabel(value)
        self.searchButton = QPushButton('Search', self)
        self.searchButton.setIconSize(QSize(200, 200))
        self.searchButton.clicked.connect(self.browseFile)
        self.continueButton = QPushButton('Continue', self)
        self.continueButton.setIconSize(QSize(200, 200))
        self.continueButton.clicked.connect(self.importFile)

        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet(
            'background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Go Back!')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)

        layoutH = QHBoxLayout()
        layoutH.addWidget(self.continueButton)
        layoutV.addLayout(layoutH)
        layoutH.addWidget(self.filename)
        layoutH.addWidget(self.searchButton)
        self.continueButton.hide()
        self.setLayout(layoutV)

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()

    def browseFile(self):
        fname = QFileDialog.getOpenFileName(self, 'open file', '/home')
        self.filename.setText(fname[0])
        if fname:
            self.inputFileName = fname[0]
            if not self.inputFileName.endswith('.pcap'):
                self.WrongFile()
                self.filename.clear()
                #print('that is not a valid pcap file. ')
            else:
                self.continueButton.show()
#           need error checking to make sure the file that is clicked is a pcap file

    def importFile(self):
        command = 'wireshark -r ' + self.inputFileName
        os.system(command)

    def WrongFile(self):
        wrongFile = QMessageBox()
        wrongFile.setIcon(QMessageBox.Critical)
        wrongFile.setWindowTitle('ERROR')
        wrongFile.setText(
            'That is not a .pcap file. Pleas select the correct file type')
        wrongFile.setStandardButtons(QMessageBox.Ok)
        wrongFile.exec_()


class createWindow(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Create new file')
        self.setWindowIcon(self.style().standardIcon(
            QStyle.SP_FileDialogInfoView))
        self.createFilename = QLineEdit()
        self.durationLabel = QLabel("Choose Duration")
        self.dropDown = QComboBox(self)
        self.dropDown.addItems([' ', '30', '60', '90', '120', '150', '180'])
        self.secondsLabel = QLabel('Sec')

        label1 = QLabel(value)
        self.button = QPushButton('Create', self)
        self.button.setIconSize(QSize(200, 200))
        self.button.clicked.connect(self.createFile)

        layoutV = QVBoxLayout()
        self.pushButton = QPushButton(self)
        self.pushButton.setStyleSheet(
            'background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Go Back!')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)

        layoutH = QHBoxLayout()
        layoutH.addWidget(self.createFilename)
        layoutH.addWidget(self.button)
        layoutH.addWidget(self.durationLabel)
        layoutH.addWidget(self.dropDown)
        layoutH.addWidget(self.secondsLabel)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()

    def createFile(self):
        fileCreate = self.createFilename.text()
        fileCreate = fileCreate + '.pcap'
        if self.dropDown.currentText() == '30':
            duration = '30'
        if self.dropDown.currentText() == '60':
            duration = '60'
        if self.dropDown.currentText() == '90':
            duration = '90'
        if self.dropDown.currentText() == '120':
            duration = '120'
        if self.dropDown.currentText() == '150':
            duration = '150'
        if self.dropDown.currentText() == '180':
            duration = '180'
        if self.dropDown.currentText() == '210':
            duration = '210'
        if self.dropDown.currentText() == '240':
            duration = '240'
        command = 'wireshark -i 2 -k -w ' + fileCreate + ' -a duration:' + duration
        os.system(command)


class HelpWindow(QWidget):
    def __init__(self):
        super(HelpWindow, self).__init__()
        self.resize(400, 300)

        # Label
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 400, 300)
        self.label.setText('Sub Window')
        self.label.setStyleSheet('font-size:40px')


class Dashboard(QMainWindow):
    def __init__(self):
        super(Dashboard, self).__init__()
        # set the title
        self.setWindowTitle("NetBox")
        self.setStyleSheet(
            "background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, stop: .5 #1168a6, stop: 1 #1174a6);")
        self.setFixedSize(1600, 900)
        self.buttonTitle = QLabel("Scans Available", self)
        self.buttonTitle.move(1400, 25)
        self.buttonTitle.setStyleSheet("font-size: 20px; color: 1174a6")
        self.buttonTitle.setGeometry(1400, 50, 150, 50)
        self.setWindowIcon(QtGui.QIcon("Logo.png"))
       # Assemble Buttons
        self.pushButtonScanComputer = QPushButton("Scan Computer", self)
        self.pushButtonScanComputer.setGeometry(1400, 100, 150, 50)
        self.pushButtonScanNetwork = QPushButton("Host Discovery", self)
        self.pushButtonScanNetwork.setGeometry(1400, 150, 150, 50)
        self.pushButtonScanNetworkVerbose = QPushButton(
            "Scan Network Verbose", self)
        self.pushButtonScanNetworkVerbose.setGeometry(1400, 200, 150, 50)

        self.pushButtonHelp = QPushButton("Exploit Computer", self)
        self.pushButtonHelp.setGeometry(1400, 250, 150, 50)

        self.pushButtonWireScan = QPushButton("WireShark Scan", self)
        self.pushButtonWireScan.setGeometry(1400, 300, 150, 50)

        # Assign Functions to buttons
        self.pushButtonScanComputer.clicked.connect(self.takeInputScanComputer)
        self.pushButtonScanNetwork.clicked.connect(self.takeInputScanNetwork)
        self.pushButtonScanNetworkVerbose.clicked.connect(
            self.scanNetworkVerbose)

        self.wiresharkWindow = Window()
        self.exploitWindow = ExploitComputerWindow()
        self.pushButtonWireScan.clicked.connect(self.wiresharkWindow.show)

        self.pushButtonHelp.clicked.connect(self.exploitWindow.show)

        # Logo addition
        self.logoLabel = QPushButton("", self)
        self.logoLabel.setStyleSheet(
            "background-image : url(Logo_15.png); border-style: solid; border-color: #000000; border-width: 3px;")
        self.logoLabel.setGeometry(0, 30, 180, 180)
        self.logoLabel.clicked.connect(self.logoClick)

        menuBar = self.menuBar()
        helpMenu = QMenu("&Help", self)
        statMenu = QMenu("&Statistics", self)
        statOpen = QAction("Open", self)
        statMenu.addAction(statOpen)
        # statOpen.triggered(self.sub_window.show)
        helpContent = QAction("&Help_Content", self)
        helpContent.triggered.connect(self.helpDis)
        aboutContent = QAction("&About", self)
        aboutContent.triggered.connect(self.aboutDis)
        helpMenu.addAction(helpContent)
        helpMenu.addAction(aboutContent)
        menuBar.addMenu(helpMenu)
        menuBar.addMenu(statMenu)
        menuBar.setStyleSheet(
            "font-size: 14px; background-color: #01a4c3; border-style: solid; border-color: #000000; border-width: 3px;")
        helpMenu.setStyleSheet("font-size: 14px; background-color: #01a4c3")
        statMenu.setStyleSheet("font-size: 14px; background-color: #01a4c3")

    def takeInputScanComputer(self):
        userIpAddressSingleComputer, done1 = QtWidgets.QInputDialog.getText(
            self, "Single Verbose", "Enter an IP Address: ")
       # print(userIpAddressSingleComputer)
       # print("Successful Input 1")
        if(userIpAddressSingleComputer != ""):
            runComputerScan(userIpAddressSingleComputer)

    def takeInputScanNetwork(self):
        userIpAddressNetwork, done2 = QtWidgets.QInputDialog.getText(
            self, "Host Discovery", "Enter Network IP Address: ")
       # print("Successful Input 2")
        if (userIpAddressNetwork != ""):
            scanLocalDevices(userIpAddressNetwork)

    def scanNetworkVerbose(self):
        userIpAddressNetworkVerbose, done3 = QtWidgets.QInputDialog.getText(
            self, "Network Verbose", "Enter Network IP Address: ")
        #print("Successful Input 3")
        if(userIpAddressNetworkVerbose != ""):
            networkScanVerbose(userIpAddressNetworkVerbose)
# MENU BAR FUNCTIONS NO TOUCH

    def helpDis(self):
        helpF = open("netBoxHelp.txt", "r")
        helpBox = QMessageBox()
        helpBox.setWindowIcon(QtGui.QIcon("Logo.png"))
        helpBox.setStyleSheet(
            "color:white;background:#01a4c3;font-size: 20px;")
        helpBox.about(helpBox, "Help", helpF.read())
        helpF.close()

    def aboutDis(self):
        aboutF = open("netBox_About.txt", "r")
        aboutBox = QMessageBox()
        aboutBox.setStyleSheet(
            "color:white;background:#01a4c3;font-size: 20px;")
        aboutBox.setWindowIcon(QtGui.QIcon("Logo.png"))
        aboutBox.about(aboutBox, "About netBox", aboutF.read())

    def logoClick(self):
        webbrowser.open_new('https://github.com/illusion173/SE300_Metasploits')

class createSystem(QWidget):
    def __init__(self, LoginSystem):
        QWidget.__init__(self)

class LoginSystem(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('NetBox Login')
        self.resize(480, 100)
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

        # Show Password Button
        self.showBox = QPushButton('Show', self)
        self.showBox.clicked.connect(self.showPass)
        pageLayout.addWidget(self.showBox, 1, 3, 1, 2)
        pageLayout.setRowMinimumHeight(2, 75)
        # Drop Down Box
        self.combobox = qtw.QComboBox(self)
        self.combobox.addItems(['Regular', 'Administrator'])
        pageLayout.addWidget(self.combobox, 2, 0)
        self.label = QLabel(self)

        # Login Button
        self.button_login = QPushButton('Login', self)
        self.button_login.clicked.connect(self.adminUser)
        pageLayout.addWidget(self.button_login, 3, 0, 1, 2)
        pageLayout.setRowMinimumHeight(2, 75)
        self.combobox.resize(20, 1)
        self.setLayout(pageLayout)

    # File Writer Function
        self.fileWriter()

    # Show Password Function
    def showPass(self):
        #print("Password has been shown")
        self.placeHolderPassword.setEchoMode(QLineEdit.EchoMode.Normal)

    # Write Files For Demonstration Purposes
    # Normal User
    def fileWriter(self):
        normalUser = [['Jack', '123'],
                      ['Joe', '456'],
                      ['Frank', '789'],
                      ['Bob', '321']]
        with open("Normal_Users.csv", 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(normalUser)

    # Administrators
        adminUser = [['Adam', '123'],
                     ['Haskell', '456'],
                     ['Jeremiah', '789'],
                     ['Ryan', '321']]
        with open("Admin_Users.csv", 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(adminUser)

    # Display success when admin user logs in
    def adminUser(self):
        # print(self.combobox.currentText())
        if self.combobox.currentText() == "Administrator":
            adminInfo = []
            msg = QMessageBox()
        # Read File
            with open("Admin_Users.csv") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    adminInfo.append(row)
            # print(adminInfo)

            username = str(self.placeHolderUsername.text())
           # print(username)

            password = str(self.placeHolderPassword.text())
           # print(password)

            column1 = [col[0] for col in adminInfo]
            column2 = [col[1] for col in adminInfo]

            if username in column1 and password in column2:
                for checkUsers in range(0, len(column1)):
                    if column1[checkUsers] == username and column2[checkUsers] == password:
                       # print("Admin Access Granted")
                       # print("Success")
                        msg.setText("Welcome Admin")
                        msg.exec_()
                        checkedLogin = 1
                        self.newDashboard = Dashboard()
                        self.newDashboard.show()
                        self.hide()
            else:
                # print("Incorrect")
                msg.setText("Username/Password does not exist")
                msg.exec_()
                self.placeHolderPassword.clear()
    # Normal User Function
        self.normUser()

    # Display success when user logs in
    def normUser(self):
        if self.combobox.currentText() == "Regular":
            #print("Normal Access")
            normInfo = []
            msg = QMessageBox()
            # Read File
            with open("Normal_Users.csv") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    normInfo.append(row)
                # print(normInfo)

                username = str(self.placeHolderUsername.text())
                # print(username)

                password = str(self.placeHolderPassword.text())
               # print(password)

                column1 = [col[0] for col in normInfo]
                column2 = [col[1] for col in normInfo]

                if username in column1 and password in column2:
                    for checkUsers in range(0, len(column1)):
                        if column1[checkUsers] == username and column2[checkUsers] == password:
                           # print("Success")
                            msg.setText("Welcome")
                            msg.exec_()
                else:
                   # print("Incorrect")
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
