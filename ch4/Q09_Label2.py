# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QGridLayout, QWidget


class MainWin(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QLabel範例')
        name_lb1 = QLabel('&Name', self)
        name_ed1 = QLineEdit(self)
        name_lb1.setBuddy(name_ed1)

        name_lb2 = QLabel('&Password', self)
        name_ed2 = QLineEdit(self)
        name_lb2.setBuddy(name_ed2)

        btn_ok = QPushButton('&OK')
        btn_cancel = QPushButton('&Cancel')
        layout = QGridLayout(self)
        layout.addWidget(name_lb1, 0, 0)
        layout.addWidget(name_ed1, 0, 1, 1, 2)
        layout.addWidget(name_lb2, 1, 0)
        layout.addWidget(name_ed2, 1, 1, 1, 2)
        layout.addWidget(btn_ok, 2, 1)
        layout.addWidget(btn_cancel, 2, 2)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()    
    win.show()
    sys.exit(app.exec_())
