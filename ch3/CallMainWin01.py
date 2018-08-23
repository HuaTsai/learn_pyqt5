import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from MainForm import Ui_MainWindow

class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        self.fileCloseAction.triggered.connect(self.close)
        self.fileOpenAction.triggered.connect(self.openMsg)

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "開啟", "/home", "All Files (*);;Text Files (*.txt)")
        self.statusbar.showMessage(file)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MainForm()
    myWin.show()
    sys.exit(app.exec_())