# Ch4 PyQt5 Basic Widgets

## QMainWindow
* methods
    * addToolBar()
    * centralWidget()
    * menuBar()
    * setCentralWidget()
    * setStatusBar()
    * statusBar()
* [Q01_MainWin.py](Q01_MainWin.py)
* [Q02_MainCenter.py](Q02_MainCenter.py)
    * QDesktopWidget().screenGeometry()
* [Q03_CloseMainWin.py](Q03_CloseMainWin.py)
    * layout = QHBoxLayout()
    * layout.addWidget()
    * self.sender()
    * QWidget().setLayout(layout)
    * QApplication.instance().quit()

## QWidget
* methods
    * x(), y(), pos()
    * geometry(), geometry().x(), geometry().y()
    * width() = geometry().width()
    * height() = geometry().height()
    * frameGeometry().width(), frameGeometry().height()
    * resize(int width, int height)
    * resize(QSize size)
    * setFixedWidth(int width)
    * setFixedHeight(int height)
    * setFixedSize(int width, int height)
    * setFixedSize(QSize size)
    * setGeometry(int x, int y, int width, int height)
    * setGeometry(QRect rect)
    * move(int x, int y)
    * move(QPoint point)
* [Q04_WidgetGeometry.py](Q04_WidgetGeometry.py)
* [Q05_MainWin2.py](Q05_MainWin2.py)
* [Q06_Icon.py](Q06_Icon.py)
* [Q07_ToolTip.py](Q07_ToolTip.py)
    * QToolTip.setFont(QFont font)
    * QWidget().setToolTip(string)

## QLabel
* inherit from QFrame
* methods
    * setAlignment()
        * Qt.AlignLeft
        * Qt.AlignRight
        * Qt.AlignCenter
        * Qt.AlignJustify
        * Qt.AlignTop
        * Qt.AlignBottom
        * Qt.AlignVCenter
    * setIndent()
    * setPixmap()
    * text()
    * setText()
    * selectedText()
    * setBuddy()
    * setWordWrap()
* signal
    * linkActivated
    * linkHovered
* [Q08_Label.py](Q08_Label.py)
    * label().setAutoFillBackground(True)
    * QPalette().setColor(QPalette.Window, Qt.blue)
    * QLabel().setPalette()
    * label().setTextInteractionFlags(Qt.TextSelectableByMouse)
    * QVBoxLayout().addStretch()
* [Q09_Label2.py](Q09_Label2.py)

## QLineEdit
* methods
    * setAlignment()
        * Qt.AlignLeft
        * Qt.AlignRight
        * Qt.AlignCenter
        * Qt.AlignJustify
        * Qt.AlignTop
        * Qt.AlignBottom
        * Qt.AlignVCenter
    * clear()
    * setEchoMode()
        * QLineEdit.Normal
        * QLineEdit.NoEcho
        * QLineEdit.Password
        * QLineEdit.PasswordEchoOnEdit
    * setPlaceholderText()
    * setMaxLength()
    * setReadOnly()
    * setText()
    * Text()
    * setDragEnabled()
    * selectAll()
    * setFocus()
    * setInputMask()
    * setValidator()
        * QIntValidator
        * QDoubleValidator
        * QRegexpValidator
* masks
    * A: ASCII alphabetic character required. A-Z, a-z.
    * a: ASCII alphabetic character permitted but not required.
    * N: ASCII alphanumeric character required. A-Z, a-z, 0-9.
    * n: ASCII alphanumeric character permitted but not required.
    * X: Any character required.
    * x: Any character permitted but not required.
    * 9: ASCII digit required. 0-9.
    * 0: ASCII digit permitted but not required.
    * D: ASCII digit required. 1-9.
    * d: ASCII digit permitted but not required (1-9).
    * #: ASCII digit or plus/minus sign permitted but not required.
    * H: Hexadecimal character required. A-F, a-f, 0-9.
    * h: Hexadecimal character permitted but not required.
    * B: Binary character required. 0-1.
    * b: Binary character permitted but not required.
    * \>: All following alphabetic characters are uppercased.
    * <: All following alphabetic characters are lowercased.
    * !: Switch off case conversion.
    * \[ \] \{ \}:	Reserved.
    * \[ \]: \\ Use \\ to escape the special characters listed above to use them as separators.
* signal
    * selectionChanged
    * textChanged
    * editingFinished
* [Q10_LineEdit.py](Q10_LineEdit.py)
    * QFormLayout().addRow()
* [Q11_LineEdit2.py](Q11_LineEdit2.py)
    * IntValidator().setRange(1, 99)
    * DoubleValidator().setRange(-360, 360)
    * DoubleValidator().setNotation(QDoubleValidator.StandardNotation)
    * DoubleValidator().setDecimals(2)
    * reg = QRegExp('[a-zA-Z0-9]+$')
    * QRegExpValidator().setRegExp(reg)
* [Q12_LineEdit3.py](Q12_LineEdit3.py)