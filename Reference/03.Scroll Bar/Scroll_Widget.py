import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QScrollArea, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class Main_Window(QWidget):    
    def __init__(self):
        super(Main_Window, self).__init__()
        self.mainUI()
        
        self.show()
        
    def mainUI(self):
        self.setWindowTitle("Window Title")
        self.setFixedSize(500,400)
        
        self.lay = QHBoxLayout()
        
        self.scrollwidget = QScrollArea()
        self.content_widget = QWidget()
        self.content_widget.setStyleSheet('background-color:white;')
        self.content_widget.setFixedSize(500,800)
        
        self.scrollwidget.setWidget(self.content_widget)
        self.scrollwidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        self.layout_v = QVBoxLayout(self)
        self.layout_v.addLayout(self.lay)
        self.layout_v.addWidget(self.scrollwidget)
        
        self.label = QLabel(self.content_widget)
        self.label.setGeometry(10,20,200,50)
        self.label.setStyleSheet('background-color: #EEEEEE;')
        self.label.setText('How To Creat Scroll Widget?')
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    temp = Main_Window()
    sys.exit(app.exec_())
