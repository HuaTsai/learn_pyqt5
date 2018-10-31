# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        self.resize(300, 200)
        self.setWindowTitle('Draw Text')
        self.text = '歡迎學習 PyQt5'

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('SimSun', 20))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
