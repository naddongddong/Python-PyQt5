import sys
from Values import GlobalValue as GV
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMessageBox
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
        
        self.show()

        
    def Main_Widget(self):
        self.main_widget = QWidget(self)
        self.main_widget.setGeometry(0,0,500,400)
        self.main_widget.setStyleSheet('background-color: #b0b0b0;')
        
        self.widget_btn_1 = QWidget(self.main_widget)
        self.widget_btn_1.setGeometry(0,60,500,70)
        self.widget_btn_1.setStyleSheet('background-color: white; border-bottom:1px solid blue;')

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
        self.widget_label_1.setStyleSheet('background-color: skyblue;')
        
        self.label_1 = QLabel(self.widget_label_1)
        self.label_1.setGeometry(10,20,150, 30)
        self.label_1.setStyleSheet('background-color: white; border:1px solid black;')
        self.label_1.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_1.setText('0')
        
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
        
    @pyqtSlot(int)
    def label_1_count_num(self, num):
        self.label_1.setText(str(num))
        
def StartGUI():
    app = QApplication(sys.argv)
    temp = Window()
    sys.exit(app.exec_())

if __name__=='__main__':
    StartGUI()
