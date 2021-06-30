import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox

class Main_Window(QWidget):    
    def __init__(self):
        super(Main_Window, self).__init__()
        self.mainUI()
    
    def mainUI(self):
        self.setFixedSize(500,200)
        self.selected_option = QLabel('Option1', self)
        self.selected_option.move(50, 150)
        self.selected_option.setGeometry(200,10,150,40)
        self.selected_option.setStyleSheet('border:1px solid black;')


        self.combo_box = QComboBox(self)
        self.combo_box.addItem('Red')
        self.combo_box.addItem('Orange')
        self.combo_box.addItem('Yellow')
        self.combo_box.addItem('Green')
        self.combo_box.addItem('Blue')
        self.combo_box.setGeometry(10,10,150,30)

        self.combo_box.activated[str].connect(self.selected_combo_function)
        
        self.show()
        
    def selected_combo_function(self, text):
        self.selected_option.setText(text)
        self.selected_option.setStyleSheet(f"border:1px solid {text}")
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    temp = Main_Window()
    sys.exit(app.exec_())
