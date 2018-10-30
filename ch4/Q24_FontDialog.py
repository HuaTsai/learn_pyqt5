# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFontDialog


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)

        layout = QVBoxLayout()
        self.btn = QPushButton('choose font')
        self.btn.clicked.connect(self.getFont)
        layout.addWidget(self.btn)

        self.lb = QLabel('Hello, 測試字體範例')
        layout.addWidget(self.lb)

        self.setLayout(layout)
        self.setWindowTitle('Font Dialog')

    def getFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lb.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
