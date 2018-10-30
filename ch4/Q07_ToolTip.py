# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip
from PyQt5.QtGui import QFont


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        self.initUi()

    def initUi(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('這是一個<b>氣泡提示</b>')
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('氣泡提示demo')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
