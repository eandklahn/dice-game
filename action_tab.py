import numpy as np

"""Using matplotlib with PyQt5: https://matplotlib.org/3.1.1/gallery/user_interfaces/embedding_in_qt_sgskip.html"""
from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
from matplotlib.figure import Figure
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QVBoxLayout, QLabel, QPushButton

class ActionTab(QWidget):

    def __init__(self):
    
        super().__init__()
        self.init_own()
        
    def init_own(self):
        
        self.ndice = 2
        self.rolled_numbers = []
        
        self.layout = QVBoxLayout()
        
        self.fig = Figure(figsize=(5,3))
        self.canvas = FigureCanvas(self.fig)
        self.tools = NavigationToolbar(self.canvas, self)
        self.ax = self.fig.subplots()
        self.init_axes()
        
        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.tools)
        
        self.setLayout(self.layout)    
    
    def init_axes(self):
    
        self.ax.grid()
        self.ax.set_xlim(-10,0)
        self.ax.set_xticklabels([x for x in range(-10,0,2)]+['Current'])
        self.ax.set_ylim(0,6*self.ndice+1)
        
    def plot_rolls(self):
        
        self.ax.clear()
        self.init_axes()
        
        if len(self.rolled_numbers)>=11:
            rolls = self.rolled_numbers[-11:]
        else:
            rolls = [0]*(11-len(self.rolled_numbers))+self.rolled_numbers
            
        self.ax.plot([x for x in range(-10,1)], rolls)
        self.fig.suptitle('{} ({})'.format(rolls[-1], len(self.rolled_numbers)))
        self.canvas.draw()
    
    def roll_dice(self):
        
        roll = np.random.randint(low=1,
                                 high=7,
                                 size=self.ndice).sum()
        self.rolled_numbers.append(roll)
        self.plot_rolls()