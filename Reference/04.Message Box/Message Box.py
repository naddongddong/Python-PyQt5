import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class Main_Window(QWidget):    
    def __init__(self):
        super(Main_Window, self).__init__()
        self.mainUI()
    
    def mainUI(self):
        self.setWindowTitle("Window Title")
        self.setFixedSize(500,400)
        
        self.btn = QPushButton("show message box",self)
        self.btn.setGeometry(160,160,200,30)
        self.btn.clicked.connect(self.show_message)
        
        self.show()
        
    def show_message(self):
        reply = QMessageBox.question(self, "MessageBox", "Do you want to quit this program?",
        QMessageBox.No | QMessageBox.Yes | QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            self.close()
        elif reply == QMessageBox.No:
            QMessageBox.Close
        else:
            QMessageBox.Close

if __name__=='__main__':
    app = QApplication(sys.argv)
    temp = Main_Window()
    sys.exit(app.exec_())
