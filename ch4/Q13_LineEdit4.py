# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont
from PyQt5.QtCore import Qt


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        self.setWindowTitle('QLineEdit範例')

        flo = QFormLayout()
        e1 = QLineEdit()
        e2 = QLineEdit()
        e3 = QLineEdit()
        e4 = QLineEdit()
        e5 = QLineEdit()
        e6 = QLineEdit()

        e1.setValidator(QIntValidator())
        e1.setMaxLength(4)
        e1.setAlignment(Qt.AlignRight)
        e1.setFont(QFont('Arial', 20))
        e2.setValidator(QDoubleValidator(0.99, 99.99, 2))
        e3.setInputMask('+99_9999_999999')
        e4.textChanged.connect(self.textchanged)
        e5.setEchoMode(QLineEdit.Password)
        e5.editingFinished.connect(self.enterPress)
        e6.setReadOnly(True)

        flo.addRow('Integer Validator', e1)
        flo.addRow('Double Validator', e2)
        flo.addRow('Input Mask', e3)
        flo.addRow('Text Changed', e4)
        flo.addRow('Password', e5)
        flo.addRow('Read Only', e6)

        self.setLayout(flo)

    def textchanged(self, text):
        print('輸入的內容為' + text)

    def enterPress(self):
        print('唯讀')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
