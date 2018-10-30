# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette


class MainWin(QWidget):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)

        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText('這是一個文字標籤')
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>歡迎使用Python GUI應用程式</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('這是一個圖片標籤')
        label3.setPixmap(QPixmap('../images/python.jpg'))

        label4.setText("<a href='https://www.google.com/'>歡迎來到Google</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('這是一個超連結標籤')

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)

        label1.setOpenExternalLinks(True)
        label4.setOpenExternalLinks(True)

        label4.linkActivated.connect(link_clicked)
        label2.linkHovered.connect(link_hovered)
        label1.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel範例')


def link_hovered():
    print('當滑鼠滑過label-2標籤時 觸發事件')


def link_clicked():
    print('當滑鼠點擊label-4標籤時 觸發事件')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
