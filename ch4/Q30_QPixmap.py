# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QWidget()
    lb = QLabel()
    lb.setPixmap(QPixmap('../images/python.jpg'))
    vbox = QVBoxLayout()
    vbox.addWidget(lb)
    win.setLayout(vbox)
    win.setWindowTitle('QPixmap')
    win.show()
    sys.exit(app.exec_())
