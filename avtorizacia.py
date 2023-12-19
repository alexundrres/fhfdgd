from PyQt6 import QtCore, QtGui, QtWidgets
from prepodavatel import Ui_prepodavatel
from ychenik import Ui_ychenik

class Ui_avtorizacia(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 400)
        MainWindow.setMinimumSize(QtCore.QSize(350, 400))
        MainWindow.setMaximumSize(QtCore.QSize(350, 400))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 204, 153);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.frame.setFont(font)
        self.frame.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(110, 60, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton.setGeometry(QtCore.QRect(80, 340, 190, 31))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(parent=self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 190, 141, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.comboBox = QtWidgets.QComboBox(parent=self.frame)
        self.comboBox.setGeometry(QtCore.QRect(110, 130, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.comboBox.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAtBottom)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.login_button_clicked)

    def login_button_clicked(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        user_type = self.comboBox.currentText()

        # Здесь вы можете выполнить проверку логина, пароля и типа пользователя.
        # Например, запрос к базе данных или другая бизнес-логика.

        # После успешной проверки, вы можете открыть соответствующее окно.
        if user_type == "Ученик":
            self.open_ychenik_window()
        elif user_type == "Преподаватель":
            self.open_prepodavatel_window()

    def open_ychenik_window(self):
        self.ychenik_window = Ui_ychenik()
        self.ychenik_window.show()


    def open_prepodavatel_window(self):
        self.prepodavatel_window = Ui_prepodavatel()
        # Отображаем окно
        self.prepodavatel_window.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Авторизация"))
        self.pushButton.setText(_translate("MainWindow", "Войти"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Логин"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Ученик"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Преподаватель"))
