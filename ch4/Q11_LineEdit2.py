# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)

        flo = QFormLayout()
        pIntLineEdit = QLineEdit()
        pDoubleLineEdit = QLineEdit()
        pValidatorLineEdit = QLineEdit()

        flo.addRow('整數', pIntLineEdit)
        flo.addRow('浮點數', pDoubleLineEdit)
        flo.addRow('字母和數字', pValidatorLineEdit)

        pIntLineEdit.setPlaceholderText('整數')
        pDoubleLineEdit.setPlaceholderText('浮點數')
        pValidatorLineEdit.setPlaceholderText('字母和數字')

        pIntValidator = QIntValidator(self)
        pIntValidator.setRange(1, 99)

        pDoubleValidator = QDoubleValidator(self)
        pDoubleValidator.setRange(-360, 360)
        pDoubleValidator.setNotation(QDoubleValidator.StandardNotation)
        pDoubleValidator.setDecimals(2)

        reg = QRegExp('[a-zA-Z0-9]+$')
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)

        pIntLineEdit.setValidator(pIntValidator)
        pDoubleLineEdit.setValidator(pDoubleValidator)
        pValidatorLineEdit.setValidator(pValidator)

        self.setLayout(flo)
        self.setWindowTitle('QLineEdit範例')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
