# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
import sys
from scanComputer import *
from scanNetworkVerbose import *
from scanNetwork import *
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QHBoxLayout, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QMovie
import webbrowser
class StatWindow(QWidget):
    def __init__(self):
         super(StatWindow, self).__init__()
         self.resize(400, 300)
         self.label = QLabel(self)
         self.label.setGeometry(0, 0, 400, 300)
         self.label.setText('Stat Window Goes Here')
         self.label.setStyleSheet('font-size:40px')
    
class HelpWindow(QWidget):

     def __init__(self):
         super(HelpWindow, self).__init__()
         self.resize(400, 300)

         # Label
         movie = QMovie('i-will-send-you-to-jesus-angry.gif')
         #pixMap = QPixmap('Trollface_non-free.png')
         self.label = QLabel(self)
         self.label.setGeometry(0, 0, 400, 300)
         self.label.setText('There IS No Help Here')
         self.label.setStyleSheet('font-size:40px')
         #self.label.setPixmap(pixMap)
         self.label.setMovie(movie)
         movie.start()
     


class Window(QMainWindow):

     def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("NetBox")
        self.setFixedSize(1600, 900)
        self.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, stop: .5 #01a4c3, stop: 1 #FDE799);")
        self.buttonTitle = QLabel("      Scans Available", self)
        self.buttonTitle.setGeometry(1400, 25, 150, 25)
        self.buttonTitle.setStyleSheet("font-size: 14px; background-color: #01a4c3;border-style: solid; border-color: #000000; border-width: 3px; ")
        #window icon
        self.setWindowIcon(QtGui.QIcon("Logo.png"))
        

       # Assemble Buttons
        self.pushButtonScanComputer = QPushButton("Scan Computer", self)
        self.pushButtonScanComputer.setGeometry(1400, 50, 150, 50)
        self.pushButtonScanComputer.setStyleSheet("font-size: 14px; background-color: #01a4c3; border-style: solid; border-color: #000000; border-width: 3px;")
        self.pushButtonScanNetwork = QPushButton("Scan Network", self)
        self.pushButtonScanNetwork.setGeometry(1400, 100, 150, 50)
        self.pushButtonScanNetwork.setStyleSheet("font-size: 14px; background-color: #01a4c3; border-style: solid; border-color: #000000; border-width: 3px;")
        self.pushButtonScanNetworkVerbose = QPushButton("Scan Network Verbose", self)
        self.pushButtonScanNetworkVerbose.setGeometry(1400, 150, 150, 50)
        self.pushButtonScanNetworkVerbose.setStyleSheet("font-size: 14px; background-color: #01a4c3; border-style: solid; border-color: #000000; border-width: 3px;")
        self.pushButtonHelp = QPushButton("DON'T PRESS", self)
        self.pushButtonHelp.setGeometry(1400, 200, 150, 50)
        self.pushButtonHelp.setStyleSheet("font-size: 14px; background-color: #01a4c3; border-style: solid; border-color: #000000; border-width: 3px;")
        #menu bar & menus
        menuBar = self.menuBar()
        helpMenu = QMenu("&Help", self)
        statMenu = QMenu("&Statistics", self)
        statOpen = QAction("Open", self)
        statMenu.addAction(statOpen)
        #statOpen.triggered(self.sub_window.show)
        helpContent = QAction("&Help_Content" , self)
        helpContent.triggered.connect(self.helpDis)
        aboutContent = QAction("&About", self)
        aboutContent.triggered.connect(self.aboutDis)
        helpMenu.addAction(helpContent)
        helpMenu.addAction(aboutContent)
        menuBar.addMenu(helpMenu)
        menuBar.addMenu(statMenu)
        menuBar.setStyleSheet("font-size: 14px; background-color: #01a4c3; border-style: solid; border-color: #000000; border-width: 3px;")
        helpMenu.setStyleSheet("font-size: 14px; background-color: #01a4c3")
        statMenu.setStyleSheet("font-size: 14px; background-color: #01a4c3")
        
       
        
        #Logo addition
        self.logoLabel = QPushButton("" ,self)
        self.logoLabel.setStyleSheet("background-image : url(Logo_15.png); border-style: solid; border-color: #000000; border-width: 3px;")
        self.logoLabel.setGeometry(0, 30, 180, 180)
        self.logoLabel.clicked.connect(self.logoClick)
        
        # Assign Functions to buttons
        self.pushButtonScanComputer.clicked.connect(self.takeInputScanComputer)
        self.pushButtonScanNetwork.clicked.connect(self.takeInputScanNetwork)
        self.pushButtonScanNetworkVerbose.clicked.connect(self.scanNetworkVerbose)
        
        self.sub_window = HelpWindow()
        self.pushButtonHelp.clicked.connect(self.sub_window.show) 

        # show all the widgets
        self.show()

     # main Functions here
     def takeInputScanComputer(self):
          userIpAddressSingleComputer, done1 = QtWidgets.QInputDialog.getText(self, "Single Verbose", "Enter an IP Address: ")
          print(userIpAddressSingleComputer)
          print("Successful Input 1")
          if(userIpAddressSingleComputer != ""):
               runComputerScan(userIpAddressSingleComputer)
          
     def takeInputScanNetwork(self):
          userIpAddressNetwork, done2 = QtWidgets.QInputDialog.getText(self, "Host Discovery", "Enter Network IP Address: ")
          print("Successful Input 2")
          if (userIpAddressNetwork != ""):
               scanLocalDevices(userIpAddressNetwork)

     def scanNetworkVerbose(self):
          userIpAddressNetworkVerbose, done3 = QtWidgets.QInputDialog.getText(self, "Network Verbose", "Enter Network IP Address: ")
          print("Successful Input 3")
          if(userIpAddressNetworkVerbose != ""):
                    networkScanVerbose(userIpAddressNetworkVerbose)

     def helpDis (self):
        helpF = open("netBoxHelp.txt", "r")
        helpBox = QMessageBox()
        helpBox.setWindowIcon(QtGui.QIcon("Logo.png"))
        helpBox.setStyleSheet("color:white;background:#01a4c3;font-size: 20px;")
        helpBox.about(helpBox, "Help", helpF.read())
        
        helpF.close()

     def aboutDis (self):
        aboutF = open("netBox_About.txt", "r")
        aboutBox= QMessageBox()
        aboutBox.setStyleSheet("color:white;background:#01a4c3;font-size: 20px;")
        aboutBox.setWindowIcon(QtGui.QIcon("Logo.png"))
        aboutBox.about(aboutBox, "About netBox", aboutF.read())
        
     def logoClick (self):
        webbrowser.open_new('https://github.com/illusion173/SE300_Metasploits')


if __name__ == "__main__":
     # create pyqt5 app
     App = QApplication(sys.argv)
     # create the instance of our Window
     window = Window()
     # start the app
     sys.exit(App.exec())
