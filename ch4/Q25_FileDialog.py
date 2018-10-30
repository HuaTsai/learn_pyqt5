# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDir


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)

        layout = QVBoxLayout()
        self.btn1 = QPushButton('載入圖片')
        self.btn1.clicked.connect(self.getfile)
        layout.addWidget(self.btn1)

        self.lb = QLabel('')
        layout.addWidget(self.lb)

        self.btn2 = QPushButton('載入文字檔')
        self.btn2.clicked.connect(self.getfiles)
        layout.addWidget(self.btn2)

        self.contents = QTextEdit()
        layout.addWidget(self.contents)

        self.setLayout(layout)
        self.setWindowTitle('File Dialog')

    def getfile(self):
        fname, _ = QFileDialog.getOpenFileName(
            self, 'Open File', '..', 'Image Files (*.jpg *.gif)')
        self.lb.setPixmap(QPixmap(fname))

    def getfiles(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')
            with f:
                data = f.read()
                self.contents.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
