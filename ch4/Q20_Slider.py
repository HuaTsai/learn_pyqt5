# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QSlider
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)

        layout = QVBoxLayout()
        self.lb = QLabel('Hello PyQt5')
        self.lb.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.lb)

        self.sl = QSlider(Qt.Horizontal)
        self.sl.setMinimum(10)
        self.sl.setMaximum(50)
        self.sl.setSingleStep(3)
        self.sl.setValue(20)
        self.sl.setTickPosition(QSlider.TicksBelow)
        self.sl.setTickInterval(5)
        self.sl.valueChanged.connect(self.valuechange)
        layout.addWidget(self.sl)

        self.setLayout(layout)
        self.resize(400, 150)
        self.setWindowTitle('Slider')

    def valuechange(self, idx):
        print('current slider value: ' + str(self.sl.value()))
        size = self.sl.value()
        self.lb.setFont(QFont('Arial', size))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
