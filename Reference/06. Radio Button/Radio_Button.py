import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.move(500, 300)
        
        self.radio_button = []
        for i in range(0,10):
            self.radio_button.append(QRadioButton('Button'+str(i+1), self))
            self.radio_button[i].move(50,30*i+10)
            if i == 0:
                self.radio_button[i].setChecked(True)
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
