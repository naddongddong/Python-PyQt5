import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class Main_Window(QWidget):    
    def __init__(self):
        super(Main_Window, self).__init__()
        self.mainUI()
    
    def mainUI(self):
        self.setWindowTitle("Window Title")
        self.setFixedSize(500,400)
        self.setStyleSheet('background-color: white;')
        
        self.labels = []
        for i in range(8):
            self.labels.append(QLabel(str(i+1)+'번째',self))
            self.labels[i].setGeometry(50 if i%2 == 0 else 270, 50+80*(i//2), 200, 50)
            
        #1. background-color, font-color
        self.labels[0].setStyleSheet('background-color: #44546A; color: white;')

        #2. alignment
        #self.labels[1].setAlignment(Qt.AlignCenter)
        
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    temp = Main_Window()
    sys.exit(app.exec_())
