import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Main_Window(QWidget):    
    def __init__(self):
        super(Main_Window, self).__init__()
        self.mainUI()
    
    def mainUI(self):
        self.setWindowTitle("Window Title")
        self.setFixedSize(500,400)
        self.setWindowIcon(QIcon('icon.png')) # Set Window Icon to 'icon.png' file
        self.show()
        

def StartGUI():
    app = QApplication(sys.argv)
    temp = Main_Window()
    sys.exit(app.exec_())

if __name__=='__main__':
    StartGUI()
