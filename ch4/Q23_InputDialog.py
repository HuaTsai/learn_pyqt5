# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QPushButton, QLineEdit, QInputDialog


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)

        layout = QFormLayout()
        self.btn1 = QPushButton('取得清單裡的選項')
        self.btn1.clicked.connect(self.getItem)
        self.le1 = QLineEdit()
        layout.addRow(self.btn1, self.le1)

        self.btn2 = QPushButton('取得字串')
        self.btn2.clicked.connect(self.getText)
        self.le2 = QLineEdit()
        layout.addRow(self.btn2, self.le2)

        self.btn3 = QPushButton('取得整數')
        self.btn3.clicked.connect(self.getInt)
        self.le3 = QLineEdit()
        layout.addRow(self.btn3, self.le3)

        self.setLayout(layout)
        self.setWindowTitle('Input Dialog')

    def getItem(self):
        items = ('C', 'C++', 'Java', 'Python')
        item, ok = QInputDialog.getItem(
            self, 'Select Input Dialog', '語言清單', items, 0, False)
        if ok and item:
            self.le1.setText(item)

    def getText(self):
        text, ok = QInputDialog.getText(
            self, 'Text Input Dialog', '輸入姓名')
        if ok:
            self.le2.setText(str(text))

    def getInt(self):
        num, ok = QInputDialog.getInt(self, 'Integer Input Dialog', '輸入數字')
        if ok:
            self.le3.setText(str(num))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
