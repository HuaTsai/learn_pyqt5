# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)

        self.btn = QPushButton(self)
        self.btn.setText('點擊彈出訊息對話視窗')
        self.btn.move(25, 25)
        self.btn.clicked.connect(self.msg)

        self.resize(300, 100)
        self.setWindowTitle('MessageBox')

    def msg(self):
        reply = QMessageBox.information(
            self, '標題', '訊息文字', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        print(reply)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
