from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

        
class Ui_NumInput(object):
    def parameter(self):
        self.background_color = "#A0A0A0"
        self.button_num_color = "#333333"
        self.button_func_color = "FF9900"
        self.button_quit_color = "gray"
        
    def setupUi(self, Form):
        Form.resize(390,450)
        Form.setFixedSize(390,450)
        self.num_widget = QWidget(Form)
        self.num_widget.setGeometry(0,0,390,450)
        
        # edit box
        self.le_num = QLineEdit(self.num_widget)
        self.le_num.setGeometry(25, 20, 330, 50)
        
        self.le_num.setAlignment(Qt.AlignRight)
        self.le_num.setStyleSheet(
            'QLineEdit {background-color: white; color: black; border: 1px; border-color: black; border-style: inset;}')
        self.le_num.setText('')
        self.le_num.setFont(QFont("Tahoma", 20))
        
        self.create_buttons()
    
    def create_buttons(self):
        self.button = [['7','8','9','back'],['4','5','6','clear'],['1','2','3','enter'],['0','0','.','exit']]
        for i_1, v_1 in enumerate(self.button):
            for i_2, v_2 in enumerate(v_1):    
                if i_1 == 3 and i_2 ==  1:
                    pass
                else:
                    self.button[i_1][i_2] = QLabel(v_2, self.num_widget)
                    self.button[i_1][i_2].setGeometry(20 + 90 * i_2, 90 * (i_1 + 1), 75, 75)
                    self.button[i_1][i_2].setStyleSheet('background-color: gray; color: white; border-radius: 36px;')
                    self.button[i_1][i_2].setFont(QFont("Tahoma", 20))
                    self.button[i_1][i_2].setAlignment(Qt.AlignCenter)
                    self.button[i_1][i_2].mousePressEvent = lambda _, a = i_1, b = i_2:self.button_action(a, b)
        self.button[3][0].setGeometry(20, 360, 160, 75)
        self.pixmap = QPixmap('./back_arrow.png')
        
        self.pixmap = self.pixmap.scaledToHeight(73)
        
        self.button[0][3].setPixmap(self.pixmap)
        
    def button_action(self, i, j):
        n = self.button[i][j].text()
        if i<3 and j<3:
            if self.le_num.text() == '0':
                self.le_num.setText(str(n))
            else:
                self.le_num.setText(self.le_num.text()+str(n))
        elif i == 3 and j == 0:
            if self.le_num.text() =='0':
                pass
            else:
                self.le_num.setText(self.le_num.text()[:]+'0')
        elif i == 0 and j == 3: #back
            if self.le_num.text() == '' or len(self.le_num.text()) == 1:
                self.le_num.setText('0')
            else:
                self.le_num.setText(self.le_num.text()[:-1])
        elif i == 1 and j == 3: #clear
            self.le_num.setText('0')
        elif i == 3 and j == 2: #dot
            if self.le_num.text().count('.') >= 1:
                pass
            else:
                if self.le_num.text() == '':
                    self.le_num.setText('0.')
                else:
                    self.le_num.setText(self.le_num.text() + '.')
            