# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
win = QWidget()
win.resize(300, 200)
win.move(250, 150)
win.setWindowTitle('Hello PyQt5')
win.show()
sys.exit(app.exec_())