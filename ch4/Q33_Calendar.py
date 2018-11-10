# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QLabel
from PyQt5.QtCore import QDate


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)

        self.cal = QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1980, 1, 1))
        self.cal.setMaximumDate(QDate(3000, 1, 1))
        self.cal.setGridVisible(True)
        self.cal.move(20, 20)
        self.cal.clicked[QDate].connect(self.showDate)

        self.lb = QLabel(self)
        date = self.cal.selectedDate()
        self.lb.setText(date.toString('yyyy-MM-dd dddd'))
        self.lb.move(20, 300)

        self.setGeometry(100, 100, 600, 350)
        self.setWindowTitle('Calendar')

    def showDate(self, date):
        self.lb.setText(date.toString('yyyy-MM-dd dddd'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
