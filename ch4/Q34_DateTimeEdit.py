# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QDateTimeEdit
from PyQt5.QtCore import QDate, QTime, QDateTime


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)

        dt_ed = QDateTimeEdit(self)
        dt_ed2 = QDateTimeEdit(QDateTime.currentDateTime(), self)
        d_ed = QDateTimeEdit(QDate.currentDate(), self)
        t_ed = QDateTimeEdit(QTime.currentTime(), self)

        dt_ed.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        dt_ed2.setDisplayFormat('yyyy/MM/dd HH-mm-ss')
        d_ed.setDisplayFormat('yyyy.MM.dd')
        t_ed.setDisplayFormat('HH:mm:ss')

        dt_ed.setMinimumDate(QDate.currentDate().addDays(-365))
        dt_ed.setMaximumDate(QDate.currentDate().addDays(365))

        dt_ed.setCalendarPopup(True)

        layout = QVBoxLayout(self)
        layout.addWidget(dt_ed)
        layout.addWidget(dt_ed2)
        layout.addWidget(d_ed)
        layout.addWidget(t_ed)

        self.setGeometry(100, 100, 250, 150)
        self.setWindowTitle('DateTimeEdit')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
