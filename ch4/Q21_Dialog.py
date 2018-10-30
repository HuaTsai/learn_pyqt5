# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog
from PyQt5.QtCore import Qt


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)

        self.btn = QPushButton(self)
        self.btn.setText('彈出對話視窗')
        self.btn.move(50, 50)
        self.btn.clicked.connect(self.showdialog)

        self.resize(350, 300)
        self.setWindowTitle('Dialog')

    def showdialog(self):
        dialog = QDialog()
        btn = QPushButton('ok', dialog)
        btn.move(50, 50)
        dialog.setWindowTitle('Dialog')
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
