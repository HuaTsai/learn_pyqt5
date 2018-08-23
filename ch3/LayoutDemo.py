import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
from UiLayoutDemo import Ui_LayoutDemo

class LayoutDemo(QMainWindow, Ui_LayoutDemo):
    def __init__(self, parent=None):
        super(LayoutDemo, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        print('收益_min', self.doubleSpinBox_min.text())
        print('收益_max', self.doubleSpinBox_max.text())
        print('最大回徹_min', self.doubleSpinBox_maxdrawdown_min.text())
        print('最大回徹_max', self.doubleSpinBox_maxdrawdown_max.text())
        print('sharp比_min', self.doubleSpinBox_sharp_min.text())
        print('sharp比_max', self.doubleSpinBox_sharp_max.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = LayoutDemo()
    ui.show()
    sys.exit(app.exec_())