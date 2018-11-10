# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QDateTimeEdit, QPushButton
from PyQt5.QtCore import QDate, QTime, QDateTime


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)

        layout = QVBoxLayout(self)

        self.dateEdit = QDateTimeEdit(QDateTime.currentDateTime(), self)
        self.dateEdit.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        self.dateEdit.setMinimumDate(QDate.currentDate().addDays(-365))
        self.dateEdit.setMaximumDate(QDate.currentDate().addDays(365))
        self.dateEdit.setCalendarPopup(True)

        self.dateEdit.dateChanged.connect(self.onDateChanged)
        self.dateEdit.dateTimeChanged.connect(self.onDateTimeChanged)
        self.dateEdit.timeChanged.connect(self.onTimeChanged)

        self.btn = QPushButton('取得日期和時間')
        self.btn.clicked.connect(self.onButtonClick)

        layout.addWidget(self.dateEdit)
        layout.addWidget(self.btn)
        
        self.resize(300, 90)
        self.setWindowTitle('DateTimeEdit2')

    def onDateChanged(self, date):
        print(date)

    def onDateTimeChanged(self, dateTime):
        print(dateTime)

    def onTimeChanged(self, time):
        print(time)

    def onButtonClick(self):
        dateTime = self.dateEdit.dateTime()
        maxDate = self.dateEdit.maximumDate()
        maxDateTime = self.dateEdit.maximumDateTime()
        maxTime = self.dateEdit.maximumTime()
        minDate = self.dateEdit.minimumDate()
        minDateTime = self.dateEdit.minimumDateTime()
        minTime = self.dateEdit.minimumTime()
        print('\n選擇的日期時間')
        print('dateTime = %s')
        print('maxDate = %s' % str(maxDate))
        print('maxDateTime = %s' % str(maxDateTime))
        print('maxTime = %s' % str(maxTime))
        print('minDate = %s' % str(minDate))
        print('minDateTime = %s' % str(minDateTime))
        print('minTime = %s' % str(minTime))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
