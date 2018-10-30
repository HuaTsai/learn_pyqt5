# Ch4 PyQt5 Basic Widgets

## Table of Contents
- [Ch4 PyQt5 Basic Widgets](#ch4-pyqt5-basic-widgets)
    - [Table of Contents](#table-of-contents)
    - [QMainWindow](#qmainwindow)
    - [QWidget](#qwidget)
    - [QLabel](#qlabel)
    - [QLineEdit](#qlineedit)
    - [QTextEdit](#qtextedit)
    - [QAbstractButton](#qabstractbutton)
    - [QPushButton](#qpushbutton)
    - [QRadioButton](#qradiobutton)
    - [QCheckBox](#qcheckbox)
    - [QComboBox](#qcombobox)
    - [QSpinBox/QDoubleSpinBox](#qspinboxqdoublespinbox)
    - [QSlider](#qslider)
    - [QDialog](#qdialog)
    - [QMessageBox](#qmessagebox)
    - [QInputDialog](#qinputdialog)
    - [QFontDialog](#qfontdialog)
    - [QFileDialog](#qfiledialog)

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
* [Q13_LineEdit4.py](Q13_LineEdit4.py)

## QTextEdit
* methods
    * setPlainText()
    * toPlainText()
    * setHtml()
    * toHtml()
    * clear()
* [Q14_TextEdit.py](Q14_TextEdit.py)

## QAbstractButton
* methods
    * isdown()
    * isChecked()
    * isEnable()
    * isCheckAble()
    * setAutoRepeat()
* signal
    * Pressed
    * Released
    * Clicked
    * Toggled

## QPushButton
* mothods
    * setCheckable()
    * toggle()
    * setIcon()
    * setEnabled()
    * isChecked()
    * setDefault()
    * setText()
    * text()
* [Q15_PushButton.py](Q15_PushButton.py)

## QRadioButton
* methods
    * setCheckable()
    * isChecked()
    * setText()
    * text()
* [Q16_RadioButton.py](Q16_RadioButton.py)

## QCheckBox
* methods
    * setChecked()
    * setText()
    * text()
    * isChecked()
    * setTriState()
        * Qt.Checked: 2
        * Qt.PartiallyChecked: 1
        * Qt.Unchecked: 0
* [Q17_CheckBox.py](Q17_CheckBox.py)
    * QGroupBox()

## QComboBox
* methods
    * addItem()
    * addItems()
    * clear()
    * count()
    * currentText()
    * itemText()
    * currentIndex()
    * setItemText()
* signal
    * Activated
    * currentIndexChanged
    * highlighted
* [Q18_ComboBox.py](Q18_ComboBox.py)

## QSpinBox/QDoubleSpinBox
* methods
    * setMinimum()
    * setMaximum()
    * setRange()
    * setValue()
    * Value()
    * singleStep()
* signal
    * valueChanged
* [Q19_SpinBox.py](Q19_SpinBox.py)

## QSlider
* methods
    * setMinimum()
    * setMaximum()
    * setSingleStep()
    * setValue()
    * value()
    * setTickInterval()
    * setTickPosition()
        * QSlider.NoTicks
        * QSlider.TicksBothSides
        * QSlider.TicksAbove
        * QSlider.TicksBelow
        * QSlider.TicksLeft
        * QSlider.TicksRight
* signal
    * valueChanged
    * sliderPressed
    * sliderMoved
    * sliderReleased
* [Q20_Slider.py](Q20_Slider.py)

## QDialog
* methods
    * setWindowTitle()
    * setWindowModality()
        * Qt.NonModal
        * Qt.WindowModal
        * Qt.ApplicationModal
* [Q21_Dialog.py](Q21_Dialog.py)

## QMessageBox
* methods
    * information()
    * question()
    * warning()
    * critical()
    * about()
    * setTitle()
    * setText()
    * setIcon()
* standard buttons
    * QMessage.OK
    * QMessage.Cancel
    * QMessage.Yes
    * QMessage.No
    * QMessage.Abort
    * QMessage.Retry
    * QMessage.Ignore
* [Q22_MessageBox.py](Q22_MessageBox.py)

## QInputDialog
* methods
    * getInt()
    * getDouble()
    * getText()
    * getItem()
* [Q23_InputDialog.py](Q23_InputDialog.py)

## QFontDialog
* methods
    * getFont()
* [Q24_FontDialog.py](Q24_FontDialog.py)

## QFileDialog
* methods
    * getOpenFileName()
    * getSaveFileName()
    * setFileMode()
        * QFileDialog.AnyFile
        * QFileDialog.ExistingFile
        * QFileDialog.Directory
        * QFileDialog.ExistingFiles
    * setFilter()
    * selectedFiles()
* [Q25_FileDialog.py](Q25_FileDialog.py)
    * QFileDialog().setFilter(QDir.Files)