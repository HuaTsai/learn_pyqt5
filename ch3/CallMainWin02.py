import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from MainForm2 import Ui_MainWindow
from ChildrenForm2 import Ui_Form

class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.child = ChildrenForm()
        self.fileCloseAction.triggered.connect(self.close)
        self.fileOpenAction.triggered.connect(self.openMsg)
        self.addWinAction.triggered.connect(self.childShow)

    def childShow(self):
        self.MaingridLayout.addWidget(self.child)
        self.child.show()

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "開啟", "/home", "All Files (*);;Text Files (*.txt)")
        self.statusbar.showMessage(file)

class ChildrenForm(QWidget, Ui_Form):
    def __init__(self):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())