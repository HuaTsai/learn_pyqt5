# -*- coding: utf-8 -*-
import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        self.resize(300, 200)
        self.setWindowTitle('Draw Points')

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.begin(self)
        self.drawPoints(event, qp)
        qp.end()

    def drawPoints(self, event, qp):
        qp.setPen(Qt.red)
        size = self.size()
        for i in range(1000):
            x = 100 * (-1 + 2.0 * i / 1000) + size.width() / 2.0
            y = -50 * math.sin((x - size.width() / 2.0) *
                               math.pi / 50) + size.height() / 2.0
            qp.drawPoint(x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
