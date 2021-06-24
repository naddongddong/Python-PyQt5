import sys
from Values import GlobalValue as GV
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMessageBox, QTabWidget
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, Qt
from time import sleep

class BackWork(QThread):
    emitdata = pyqtSignal(int)
    
    def __init__(self, parent=None):
        super().__init__()
        self.isloop = True           
           
    def run(self):
        print(GV.start_num)
        self.count_work()
        
    def count_work(self):
        self.num = GV.start_num
        while(self.isloop):
            self.emitdata.emit(self.num)
            self.num += 1
            sleep(0.1)
            
    @pyqtSlot(int, int)
    def stop_BW(self, i, saved_num):
        if i == 1:
            self.isloop = False
            self.quit()
            self.wait(5000)
        GV.start_num = saved_num
            
class Window(QWidget):
    stop_signal_BW = pyqtSignal(int, int)
    
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Window title")
        self.setGeometry(650,350,500,400)
        self.setFixedSize(500,400)
        
        self.Main_Widget()
        self.Sec_Widget()
        self.show()

        
    def Main_Widget(self):
        self.main_widget = QWidget(self)
        self.main_widget.setGeometry(0,0,500,400)
        self.main_widget.setStyleSheet('background-color: white;')
        
        self.widget_btn_1 = QWidget(self.main_widget)
        self.widget_btn_1.setGeometry(0,60,500,70)
        self.widget_btn_1.setStyleSheet('background-color: white; border-bottom:2px solid black; ')

        self.pb = []
        for i in range(0, 4):
            self.pb.append(QPushButton(self.widget_btn_1))
            self.pb[i].setGeometry(10 + 90*i, 10,80,40)
            #self.pb[i].setStyleSheet('background-color: white; border:1px solid black; color: black;')
            self.pb[i].clicked.connect(lambda _, num=i: self.button_function(num+1))
            #self.pb[i].clicked.connect(lambda num: self.button_function(i+1))  ##wrong
        self.pb[0].setText('Start')
        self.pb[1].setText('Stop')
        self.pb[1].setEnabled(False)
        self.pb[2].setText('Reset')
        self.pb[3].setText('close')
        
        self.widget_label_1 = QWidget(self.main_widget)
        self.widget_label_1.setGeometry(0,0,500,60)
        self.widget_label_1.setStyleSheet('background-color: white;')
        
        self.label_1 = QLabel(self.widget_label_1)
        self.label_1.setGeometry(10,20,150, 30)
        self.label_1.setStyleSheet('background-color: white; border:1px solid black;')
        self.label_1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_1.setText('0')
        
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        
        self.tabs = QTabWidget(self.main_widget)
        self.tabs.setGeometry(0,150,500,200)
        #self.tabs.setTabBar()
        a = str('''
            QTabWidget::pane {
                border: 2px solid blue;
                border-radius: 6px;
            }
            QTabWidget::tab-bar {
                width:200px;
                border:1px solid black;
            }
        ''')
        self.tabs.setStyleSheet(a)
        self.tabs.addTab(self.tab1, "Tab1")
        self.tabs.addTab(self.tab2, "Tab2")
        
        self.tab1_label = QLabel(self.tab1)
        self.tab1_label.setGeometry(10,10,200,20)
        self.tab1_label.setText('Select Graph Button')
        
        self.tab1_btn_1 = QPushButton("Graph 1", self.tab1)
        self.tab1_btn_1.setGeometry(10,50,200,30)
        self.tab1_btn_1.setStyleSheet("background-color: #DFDFDF; border:1px solid black;")
        self.tab1_btn_1.clicked.connect(lambda _, num=1: self.show_graph(num))
        
        self.tab1_btn_2 = QPushButton("Graph 2", self.tab1)
        self.tab1_btn_2.setGeometry(220,50,200,30)
        self.tab1_btn_2.setStyleSheet("background-color: #DFDFDF; border:1px solid black;")
        self.tab1_btn_2.clicked.connect(lambda _, num=2: self.show_graph(num))
        
    def show_graph(self, n):
        print(n)
        if n == 1:
            self.main_widget.hide()
            self.sec_widget.show()
            #self.hide()
        
    def button_function(self, i):
        if i == 1:
            self.BW = BackWork()
            self.BW.emitdata.connect(self.label_1_count_num)
            self.stop_signal_BW.connect(self.BW.stop_BW)
            self.BW.start()
            self.pb[0].setEnabled(False)
            self.pb[1].setEnabled(True)
            self.pb[2].setEnabled(False)
        elif i == 2:
            self.stop_signal_BW.emit(1, int(self.label_1.text()))
            self.pb[0].setEnabled(True)
            self.pb[1].setEnabled(False)
            self.pb[2].setEnabled(True)
        elif i == 3:
            GV.start_num = 0
            self.label_1.setText(str(GV.start_num))
        elif i == 4:
            reply = QMessageBox.question(self, " ", "Are you sure to want to close?", QMessageBox.No|QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                self.close()
            elif reply == QMessageBox.No:
                msg = QMessageBox()
                msg.setWindowTitle(" ")
                msg.setText("Cancel")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                
    def Sec_Widget(self):
        self.sec_widget = QWidget(self)
        self.sec_widget.setGeometry(0,0,500,400)
        self.sec_widget.setStyleSheet('background-color: white;')
        self.sec_widget.hide()
        
    @pyqtSlot(int)
    def label_1_count_num(self, num):
        self.label_1.setText(str(num))

if __name__=='__main__':
    app = QApplication(sys.argv)
    temp = Window()
    sys.exit(app.exec_())
