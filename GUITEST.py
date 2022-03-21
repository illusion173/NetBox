import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 240))    
        self.setWindowTitle("NetBox Login") 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('UserName:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)
        
        self.passLabel = QLabel(self)
        self.passLabel.setText('Password:')
        self.passline = QLineEdit(self)

        self.passline.move(80, 80)
        self.passline.resize(200, 32)
        self.passLabel.move(20, 80)

        pybutton = QPushButton('Login', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 120)        

    def clickMethod(self):
       #Write File
        write_lines = ['Username: '+str(self.line.text()), 'Password: '+str(self.passline.text())]
        with open('test.xml','w')as file:
            for line in write_lines:
                file.write(line)
                file.write('\n')
        
        #Read File
        with open('test.xml') as file:
            rlines = file.readlines()
  
        print(rlines)
        self.secondWindow = ToolBox()
        self.secondWindow.show()
        MainWindow.close(self)
        
class ToolBox(QMainWindow):
    def __init__(self):
            QMainWindow.__init__(self)

            self.setMinimumSize(QSize(420, 240))    
            self.setWindowTitle("NetBox Tool Page")
            
            
            button_wireShark = QPushButton('WireShark', self)
            button_wireShark.resize(100,32)
            button_wireShark.move(80, 120)
            
            button_meta = QPushButton('Metaspliot', self)
            button_meta.resize(100,32)
            button_meta.move(260, 120)
            
            
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec() )