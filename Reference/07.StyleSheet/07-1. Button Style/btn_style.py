import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Main_Window(QWidget):    
    def __init__(self):
        super(Main_Window, self).__init__()
        self.mainUI()
    
    def mainUI(self):
        self.setWindowTitle("Window Title")
        self.setFixedSize(500,400)
        self.setStyleSheet('background-color: white;')
        
        self.button = []
        for i in range(8):
            self.button.append(QPushButton(str(i+1)+'번째',self))
            self.button[i].setGeometry(50 if i%2 == 0 else 270, 50+80*(i//2), 200, 50)
            
        #1. background-color, font-color
        self.button[0].setStyleSheet('background-color: #44546A; color: white;')
        
        #2. border
        self.button[1].setStyleSheet('border:2px solid skyblue')
        
        #3. Gradient
        self.button[2].setStyleSheet('background-color:QLineargradient(y1:0.5, y2:1, stop:0 white, stop:1 lightpink); color: black;')
        
        #4. top-handed (also top, bottom, left, right)
        self.button[3].setStyleSheet('border-top:5px solid black;')
        
        #5. triangular button
        self.button[4].setStyleSheet('border-top:50px solid green; border-left:200px solid rgba(0,0,0,0.01); color:black')
        
        #6. font style
        self.button[5].setStyleSheet('color: #ffc000; font-size:20px; font-weight:bold; font-family: Tahoma;')
        
        #7. border radius
        self.button[6].setStyleSheet('border:1px solid black; border-radius: 20px; ')
        
        #8. various styles
        self.button[7].setStyleSheet("background-color: #EFECCA;"
                                     "border: 2px solid #002F2F;"
                                     "color: #002F2F;"
                                     "border-radius: 20px;"
                                     "font-weight:bold;"
                                     "font-family: Arial;"
                                     "font-size:25px;"
                                     )
        
        
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    temp = Main_Window()
    sys.exit(app.exec_())
