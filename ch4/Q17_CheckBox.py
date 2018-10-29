# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QCheckBox, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox
from PyQt5.QtCore import Qt


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        groupBox = QGroupBox('Checkboxes')
        groupBox.setFlat(True)

        layout = QHBoxLayout()
        self.checkBox1 = QCheckBox('&Checkbox1')
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect(
            lambda: self.btnstate(self.checkBox1))
        layout.addWidget(self.checkBox1)

        self.checkBox2 = QCheckBox('Checkbox2')
        self.checkBox2.toggled.connect(lambda: self.btnstate(self.checkBox2))
        layout.addWidget(self.checkBox2)

        self.checkBox3 = QCheckBox('Checkbox3')
        self.checkBox3.setTristate(True)
        self.checkBox3.setCheckState(Qt.PartiallyChecked)
        self.checkBox3.stateChanged.connect(
            lambda: self.btnstate(self.checkBox3))
        layout.addWidget(self.checkBox3)

        groupBox.setLayout(layout)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(groupBox)

        self.setLayout(mainLayout)
        self.setWindowTitle('CheckBox')

    def btnstate(self, btn):
        chk1Status = '{}, isChecked = {}, checkState = {}\n'.format(
            self.checkBox1.text(), self.checkBox1.isChecked(), self.checkBox1.checkState())
        chk2Status = '{}, isChecked = {}, checkState = {}\n'.format(
            self.checkBox2.text(), self.checkBox2.isChecked(), self.checkBox2.checkState())
        chk3Status = '{}, isChecked = {}, checkState = {}\n'.format(
            self.checkBox3.text(), self.checkBox3.isChecked(), self.checkBox3.checkState())
        print(chk1Status + chk2Status + chk3Status)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
