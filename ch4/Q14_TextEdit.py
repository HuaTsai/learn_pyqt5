# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QVBoxLayout, QPushButton


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        self.textEdit = QTextEdit()
        self.btnPress1 = QPushButton('顯示文字')
        self.btnPress2 = QPushButton('顯示HTML')
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)
        self.setLayout(layout)
        self.btnPress1.clicked.connect(self.Press1)
        self.btnPress2.clicked.connect(self.Press2)

        self.resize(350, 270)
        self.setWindowTitle('QTextEdit範例')

    def Press1(self):
        self.textEdit.setPlainText('Hello PyQt5!\n點擊按鈕')

    def Press2(self):
        self.textEdit.setHtml(
            "<font color='red' size='6'><red>Hello PyQt5!\n點擊按鈕</font>")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
