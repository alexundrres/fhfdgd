import openpyxl
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_prepodavatel(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 597)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.btn_exit = QtWidgets.QPushButton(parent=self.frame)
        self.btn_exit.setGeometry(QtCore.QRect(730, 0, 75, 23))
        self.btn_exit.setObjectName("btn_exit")
        self.btn_spravka = QtWidgets.QPushButton(parent=self.frame)
        self.btn_spravka.setGeometry(QtCore.QRect(660, 0, 75, 23))
        self.btn_spravka.setObjectName("btn_spravka")
        self.tableView_prep = QtWidgets.QTableView(parent=self.frame)
        self.tableView_prep.setGeometry(QtCore.QRect(60, 150, 671, 381))
        self.tableView_prep.setObjectName("tableView_prep")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(60, 110, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_excel = QtWidgets.QPushButton(parent=self.frame)
        self.btn_excel.setGeometry(QtCore.QRect(60, 550, 75, 23))
        self.btn_excel.setObjectName("btn_excel")
        self.btn_delit = QtWidgets.QPushButton(parent=self.frame)
        self.btn_delit.setGeometry(QtCore.QRect(650, 120, 81, 31))
        self.btn_delit.setObjectName("btn_delit")
        self.btn_add = QtWidgets.QPushButton(parent=self.frame)
        self.btn_add.setGeometry(QtCore.QRect(570, 120, 81, 31))
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn_exit.clicked.connect(self.exit_button_clicked)
        self.btn_spravka.clicked.connect(self.spravka_button_clicked)
        self.btn_excel.clicked.connect(self.export_to_excel)
        self.btn_delit.clicked.connect(self.delete_record)
        self.btn_add.clicked.connect(self.add_record)

    def exit_button_clicked(self):
        self.frame.close()


    def spravka_button_clicked(self):
        QtWidgets.QMessageBox.information(self.frame, "Справка", "Это справочная информация.")


    def export_to_excel(self):
        workbook = openpyxl.Workbook()
        sheet = workbook.active

        # Пример: Запись данных из таблицы в Excel
        for row in range(self.tableView_prep.model().rowCount()):
            for column in range(self.tableView_prep.model().columnCount()):
                item = self.tableView_prep.model().item(row, column)
                sheet.cell(row=row + 1, column=column + 1, value=str(item.text()))


    def delete_record(self):
        selected_row = self.tableView_prep.selectionModel().currentIndex().row()
        self.tableView_prep.model().removeRow(selected_row)
        self.tableView_prep.model().submitAll()

    def add_record(self):
        row_position = self.tableView_prep.model().rowCount()
        self.tableView_prep.model().insertRow(row_position)
        self.tableView_prep.model().setData(self.tableView_prep.model().index(row_position, 0), "Новая запись")
        self.tableView_prep.model().submitAll()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_exit.setText(_translate("MainWindow", "Выход"))
        self.btn_spravka.setText(_translate("MainWindow", "Справка"))
        self.label.setText(_translate("MainWindow", "Отметки:"))
        self.btn_excel.setText(_translate("MainWindow", "Вывод в Excel"))
        self.btn_delit.setText(_translate("MainWindow", "Удалить"))
        self.btn_add.setText(_translate("MainWindow", "Добавить"))
