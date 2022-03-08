from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
import sys
from scanComputer import *
from scanNetworkVerbose import *
from scanNetwork import *
#Note use this for testing scanme.nmap.org
class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(1600, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
    
        #Button Title
        self.buttonTitle = QLabel(self.centralwidget)
        self.buttonTitle.setGeometry(QtCore.QRect(1407, 25, 300, 30))
        self.buttonTitle.setFont(QFont('Arial', 15))
        self.buttonTitle.setText("Scans Available")

        #Assemble Buttons
        self.pushButtonScanComputer = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonScanComputer.setGeometry(QtCore.QRect(1400, 50, 150, 50))
        self.pushButtonScanNetwork = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonScanNetwork.setGeometry(QtCore.QRect(1400, 100, 150, 50))
        self.pushButtonScanNetworkVerbose= QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonScanNetworkVerbose.setGeometry(QtCore.QRect(1400, 150, 150, 50))

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("NetBox Dashboard", "NetBox"))
        
        self.pushButtonScanComputer.setText(_translate("MainWindow", "Computer Verbose"))
        self.pushButtonScanNetwork.setText(_translate("MainWindow", "Host Scan"))
        self.pushButtonScanNetworkVerbose.setText(_translate("MainWindow", "Network Verbose"))
        self.pushButtonScanComputer.clicked.connect(self.takeInputScanComputer)
        self.pushButtonScanNetwork.clicked.connect(self.takeInputScanNetwork)
        self.pushButtonScanNetworkVerbose.clicked.connect(self.scanNetworkVerbose)
         
    def takeInputScanComputer(self):
        userIpAddressSingleComputer, done1 = QtWidgets.QInputDialog.getText(self, "Single Verbose", "Enter an IP Address: ")
        print(userIpAddressSingleComputer)
        print("Successful Input 1")
        runComputerScan(userIpAddressSingleComputer)
        
    def takeInputScanNetwork(self):
        userIpAddressNetwork, done2 = QtWidgets.QInputDialog.getText(self, "Host Discovery", "Enter Network IP Address: ")
        print("Successful Input 2")
        scanLocalDevices(userIpAddressNetwork)

    def scanNetworkVerbose(self):
        userIpAddressNetworkVerbose, done3 = QtWidgets.QInputDialog.getText(self, "Network Verbose", "Enter Network IP Address: ")
        print("Successful Input 3")
        networkScanVerbose(userIpAddressNetworkVerbose)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())