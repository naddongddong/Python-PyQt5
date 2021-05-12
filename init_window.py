import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        #self.main_window = MainWindow()
        self.setWindowTitle("Window title")
        self.setGeometry(650,350,500,400)
        
        self.SecMain()
        self.show()
        
    def SecMain(self):
        self.main_widget = QWidget(self)
        self.main_widget.setGeometry(0,0,500,400)
        #self.main_widget.setStyleSheet('background-color: white;')
            
        
        
        
def StartGUI():
    app = QApplication(sys.argv)
    temp = MainWindow()
    sys.exit(app.exec_())

if __name__=='__main__':
    StartGUI()