import sys
import json
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                             QApplication, QPushButton)

class MainWindow(QMainWindow): 
    def __init__(self):
        super().__init__()
                
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.lay = QVBoxLayout(self.centralwidget)
                
        with open("HostDiscovery.json") as file:
            data = json.load(file)
            
        ipAddress = []
    
        def count(storage, value):
            try:
                storage[value] = storage[value] +1
            except KeyError as e:
                storage[value] = 1
            return
            
        for k,v in data.items():
            for port in v['status']['state']:
                ipAddress.append(port)
            
            if(v['status']['state'] == 'up'):
                self.btn = QPushButton(k, self) 
                button_Text = self.btn.text()
                self.btn.clicked.connect(lambda check, text=button_Text : print("\nclicked Button {}".format(text)))
                self.lay.addWidget(self.btn)    
                print(k)
                print("Up")
            else:
                pass
                print("Down")
           
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()                                           
    main.show()
    sys.exit( app.exec_() )