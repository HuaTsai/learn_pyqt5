# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class MainWin(QMainWindow):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        self.resize(400, 200)
        self.status = self.statusBar()
        self.status.showMessage('這是狀態列提示', 5000)
        self.setWindowTitle('PyQt MainWindow範例')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../images/cartoon1.ico'))
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
