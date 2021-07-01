import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem

class Main_Window(QWidget):    
    def __init__(self):
        super(Main_Window, self).__init__()
        self.mainUI()
        self.show()
    def mainUI(self):
        self.setFixedSize(500,400)
        
        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(500, 400)
        self.tableWidget.setRowCount(15)
        self.tableWidget.setColumnCount(4)
        self.setTableWidgetData()
        self.tableWidget.show()
        
    def setTableWidgetData(self):
        self.tableWidget.setItem(0, 0, QTableWidgetItem('1,1'))
        self.tableWidget.setItem(4, 3, QTableWidgetItem('5,4'))
        self.tableWidget.setItem(14, 3, QTableWidgetItem('15,4'))
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    temp = Main_Window()
    sys.exit(app.exec_())
