import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem

class Main_Window(QWidget):    
    def __init__(self):
        super(Main_Window, self).__init__()
        self.mainUI()
        self.show()
    
    def mainUI(self):
        self.setFixedSize(300,300)
        
        self.listwidget = QListWidget(self)
        self.listwidget.resize(300, 300)
        #1
        self.listwidget.insertItem(0, "Dog")
        self.listwidget.insertItem(1, "Cat")
        
        #2
        self.listwidget.insertItem(2, QListWidgetItem("Pig"))
        
        #3
        item = QListWidgetItem('Rabbit')
        self.listwidget.addItem(item)

if __name__=='__main__':
    app = QApplication(sys.argv)
    temp = Main_Window()
    sys.exit(app.exec_())
