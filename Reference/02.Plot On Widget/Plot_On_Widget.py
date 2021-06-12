import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
import pandas as pd
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Main_Window(QWidget):    
    def __init__(self):
        super(Main_Window, self).__init__()
        self.mainUI()
        
        self.show()
    
    def mainUI(self):
        self.setWindowTitle("Graph Widget")
        self.setFixedSize(600,400)
        
        self.main_widget = QWidget(self)
        self.main_widget.setGeometry(0,0,600,400)
        
        canvas = FigureCanvas(Figure(figsize=(6,4)))
        vbox = QVBoxLayout(self.main_widget)
        vbox.addWidget(canvas)
        
        raw = pd.read_csv('data.txt', header=None, sep='\t')
        self.fs = 2000
        dt = 1/self.fs
        start_time, length = 0, 8
        raw_data = raw.iloc[:,0]
        self.Sig = self.cut_segment(raw_data, start_time, self.fs, length)
        print(self.Sig)
        
        self.ax = canvas.figure.subplots()
        self.draw_graph(self.Sig, self.fs)
        
    def draw_graph(self, signal, sf):
        N = len(signal)
        nx = np.linspace(0, N/sf, N)
        self.ax.plot(nx, signal)
    
    def cut_segment(self, sn, start_position_second, sampling_rate, length_sec):
        nx = int(start_position_second * sampling_rate)
        ny = int(length_sec * sampling_rate)
        return sn[nx:nx+ny] 
    
if __name__=='__main__':
    app = QApplication(sys.argv)
    temp = Main_Window()
    sys.exit(app.exec_())
