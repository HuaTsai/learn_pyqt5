# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        self.setWindowTitle('QLineEdit範例')

        flo = QFormLayout()
        pNormalLineEdit = QLineEdit()
        pNoEchoLineEdit = QLineEdit()
        pPasswordLineEdit = QLineEdit()
        pPasswordEchoOnEditLineEdit = QLineEdit() 

        flo.addRow('Normal', pNormalLineEdit)
        flo.addRow('NoEcho', pNoEchoLineEdit)
        flo.addRow('Password', pPasswordLineEdit)
        flo.addRow('PasswordEchoOnEdit', pPasswordEchoOnEditLineEdit)

        pNormalLineEdit.setPlaceholderText('Normal')
        pNoEchoLineEdit.setPlaceholderText('NoEcho')
        pPasswordLineEdit.setPlaceholderText('Password')
        pPasswordEchoOnEditLineEdit.setPlaceholderText('PasswordEchoOnEdit')

        pNormalLineEdit.setEchoMode(QLineEdit.Normal)
        pNoEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        pPasswordLineEdit.setEchoMode(QLineEdit.Password)
        pPasswordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(flo)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
