import numpy as np
from scipy.stats import chisquare
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

"""Using matplotlib with PyQt5: https://matplotlib.org/3.1.1/gallery/user_interfaces/embedding_in_qt_sgskip.html"""
from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
from matplotlib.figure import Figure
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar

class StatisticsTab(QWidget):

    def __init__(self):
        
        super().__init__()
        self.init_own()
        
    def init_own(self):
    
        self.ndice = 2
        self.prob = np.array([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])
        
        self.f_exp = []
        self.f_obs = []
        self.chisq = 0
        self.p_val = 0
        
        self.layout = QVBoxLayout()
        
        self.fig = Figure(figsize=(5,3))
        self.canvas = FigureCanvas(self.fig)
        self.tools = NavigationToolbar(self.canvas, self)
        self.ax = self.fig.subplots()
        
        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.tools)
        
        self.setLayout(self.layout)
    
    def determine_fairness(self):
    
        if self.p_val > 0.05: return True
        else: return False
    
    def update(self, rolls):
        
        self.ax.clear()
        
        self.f_obs = self.ax.hist(rolls, bins=[x+0.5 for x in range(self.ndice-1,6*self.ndice+1)])[0]
        self.f_exp = self.prob/self.prob.sum()*len(rolls)
        
        #self.ax.plot([x for x in range(self.ndice,6*self.ndice+1)], self.f_exp, 'k-')
        self.chisq, self.p_val = chisquare(self.f_obs, self.f_exp)
        self.fig.suptitle('{} ({})'.format(rolls[-1], len(rolls)))
        
        self.canvas.draw()
        