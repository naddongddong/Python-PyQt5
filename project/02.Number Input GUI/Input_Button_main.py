import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QDialog
from PyQt5.QtCore import Qt
from Input_Button_UI import Ui_NumInput

class Main_Window(QWidget):    
    def __init__(self):
        super(Main_Window, self).__init__()
        self.mainUI()
        self.numui = Ui_NumInput()
        
    def mainUI(self):
        self.setWindowTitle("Window Title")
        self.setFixedSize(500,400)
        
        self.Edit = QLineEdit("Click to input number",self)
        self.Edit.setGeometry(160,160,200,30)
        self.Edit.setAlignment(Qt.AlignCenter)
        self.Edit.mousePressEvent = self.call_num_input
        self.show()
        
    def call_num_input(self, event):
        self.input_num_widget = QWidget()
        self.input_num_widget.setWindowFlags(Qt.FramelessWindowHint)
        self.input_num_widget.setStyleSheet('background-color: white; border:1px solid black;')
        self.input_num_widget.setWindowModality(2)
        
        self.numui.setupUi(self.input_num_widget)
        if self.Edit.text() != "Click to input number":
            self.numui.le_num.setText(self.Edit.text())
        
        self.numui.button[3][3].clicked.connect(self.exit)
        self.numui.button[2][3].clicked.connect(self.enter)
        
        self.input_num_widget.show()
        
    def exit(self):
        self.input_num_widget.close()
    
    def enter(self):
        if self.numui.le_num.text() == '0.':
            self.numui.le_num.setText('0')
        self.Edit.setText(self.numui.le_num.text())
        self.input_num_widget.close()
        
def StartGUI():
    app = QApplication(sys.argv)
    temp = Main_Window()
    sys.exit(app.exec_())

if __name__=='__main__':
    StartGUI()
