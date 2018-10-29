# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QComboBox


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)

        layout = QVBoxLayout()
        self.cb = QComboBox()
        self.cb.addItem('C')
        self.cb.addItem('C++')
        self.cb.addItems(['Java', 'C#', 'Python'])
        self.cb.currentIndexChanged.connect(self.selectionchange)
        layout.addWidget(self.cb)

        self.lb = QLabel('')
        layout.addWidget(self.lb)

        self.setLayout(layout)
        self.resize(300, 90)
        self.setWindowTitle('ComboBox')

    def selectionchange(self, idx):
        self.lb.setText(self.cb.currentText())
        print('Items in the list are: ')
        for i in range(self.cb.count()):
            print('item {} = {}'.format(i, self.cb.itemText(i)))
        print('Current index', idx, 'selection changed', self.cb.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
