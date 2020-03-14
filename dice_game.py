import sys
from action_tab import ActionTab
from stats_tab import StatisticsTab

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QVBoxLayout, QLabel, QPushButton


class DiceGame(QMainWindow):

    def __init__(self):
    
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.setWindowTitle('Roll the dice...')
        self.setWindowIcon(QIcon(r'images\Robinweatherall-Cashino-Dice.ico'))
        
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.layout = QVBoxLayout()
        self.tab_container = QTabWidget()
        
        self.action_tab = ActionTab()
        self.tab_container.addTab(self.action_tab, "&Latest rolls")
        
        self.stats_tab = StatisticsTab()
        self.tab_container.addTab(self.stats_tab, "&Statistics")
        
        self.roll_btn = QPushButton('&Roll...')
        self.roll_btn.clicked.connect(self.roll_dice)
        
        self.fair_lbl = QLabel('Fairness')
        self.fair_lbl.setAlignment(Qt.AlignCenter)
        
        self.layout.addWidget(self.tab_container)
        self.layout.addWidget(self.roll_btn)
        self.layout.addWidget(self.fair_lbl)
        self.main_widget.setLayout(self.layout)
        
        self.show()
        
    def roll_dice(self):
        
        self.action_tab.roll_dice()
        self.stats_tab.update(self.action_tab.rolled_numbers)
        self.update_fairness_label()
        
    def update_fairness_label(self):
    
        if self.stats_tab.determine_fairness():
            self.fair_lbl.setStyleSheet('background-color: green')
        else:
            self.fair_lbl.setStyleSheet('background-color: red')
            
if __name__ == '__main__':

    app = QApplication(sys.argv)
    GUI = DiceGame()
    sys.exit(app.exec_())
