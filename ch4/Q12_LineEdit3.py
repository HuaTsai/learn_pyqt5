# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        self.setWindowTitle('QLineEdit的輸入遮罩範例')

        flo = QFormLayout()
        pIPLineEdit = QLineEdit()
        pMACLineEdit = QLineEdit()
        pDateLineEdit = QLineEdit()
        pLicenseLineEdit = QLineEdit()

        pIPLineEdit.setInputMask('000.000.000.000;_')
        pMACLineEdit.setInputMask('HH:HH:HH:HH:HH:HH;_')
        pDateLineEdit.setInputMask('0000-00-00')
        pLicenseLineEdit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')

        flo.addRow('數字遮罩', pIPLineEdit)
        flo.addRow('MAC遮罩', pMACLineEdit)
        flo.addRow('日期遮罩', pDateLineEdit)
        flo.addRow('許可證遮罩', pLicenseLineEdit)

        self.setLayout(flo)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
