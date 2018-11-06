# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QLineEdit, QFormLayout


class Combo(QComboBox):
    def __init__(self, title, parent):
        super(Combo, self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.addItem(e.mimeData().text())


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        layout = QFormLayout()
        layout.addRow(QLabel('請把左邊的文字拖曳到右邊的下拉式清單中'))
        ed = QLineEdit()
        ed.setDragEnabled(True)
        com = Combo('Button', self)
        layout.addRow(ed, com)
        self.setLayout(layout)
        self.setWindowTitle('Drag')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
