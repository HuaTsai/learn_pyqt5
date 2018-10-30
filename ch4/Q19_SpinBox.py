# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QSpinBox
from PyQt5.QtCore import Qt


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)

        layout = QVBoxLayout()
        self.lb = QLabel('目前值: ')
        self.lb.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.lb)

        self.sp = QSpinBox()
        self.sp.valueChanged.connect(self.valuechange)
        layout.addWidget(self.sp)

        self.setLayout(layout)
        self.resize(300, 100)
        self.setWindowTitle('SpinBox')

    def valuechange(self, idx):
        self.lb.setText('目前值: ' + str(self.sp.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
