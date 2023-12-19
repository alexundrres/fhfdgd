import openpyxl
import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QPushButton, QWidget, QTableView, QMessageBox, QMainWindow
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QMetaObject, QRect
from PyQt6 import QtCore

class Ui_ychenik(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QVBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QWidget(parent=self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255); border: 1px solid black;")
        self.frame.setObjectName("frame")
        self.btn_spravka = QPushButton(parent=self.frame)
        self.btn_spravka.setGeometry(QRect(644, 0, 71, 23))
        self.btn_spravka.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_spravka.setObjectName("btn_spravka")
        self.btn_exit = QPushButton(parent=self.frame)
        self.btn_exit.setGeometry(QRect(720, 0, 75, 23))
        self.btn_exit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_exit.setObjectName("btn_exit")
        self.label = QLabel(parent=self.frame)
        self.label.setGeometry(QRect(60, 110, 91, 21))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableView = QTableView(parent=self.frame)
        self.tableView.setGeometry(QRect(60, 150, 671, 381))
        self.tableView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableView.setObjectName("tableView")
        self.btn_excel = QPushButton(parent=self.frame)
        self.btn_excel.setGeometry(QRect(60, 550, 81, 23))
        self.btn_excel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn_excel.setObjectName("btn_excel")
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn_exit.clicked.connect(self.exit_button_clicked)
        self.btn_spravka.clicked.connect(self.spravka_button_clicked)
        self.btn_excel.clicked.connect(self.export_to_excel)


class Ui_ychenikWindow(QMainWindow, Ui_ychenik):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Добавим обработчики событий для кнопок
        self.btn_exit.clicked.connect(self.exit_button_clicked)
        self.btn_spravka.clicked.connect(self.spravka_button_clicked)
        self.btn_excel.clicked.connect(self.export_to_excel)

    def exit_button_clicked(self):
        # Закрытие окна
        self.close()

    def spravka_button_clicked(self):
        # Пример: Отображение справочной информации в диалоговом окне
        QMessageBox.information(self, "Справка", "Это справочная информация.")

    def export_to_excel(self):
        # Пример: Экспорт данных в Excel с использованием библиотеки openpyxl
        import openpyxl

        workbook = openpyxl.Workbook()
        sheet = workbook.active

        # Пример: Запись данных из таблицы в Excel
        for row in range(self.tableView.model().rowCount()):
            for column in range(self.tableView.model().columnCount()):
                item = self.tableView.model().item(row, column)
                sheet.cell(row=row + 1, column=column + 1, value=str(item.text()))

        # Пример: Сохранение файла Excel
        workbook.save("exported_data.xlsx")

        QMessageBox.information(self, "Экспорт в Excel", "Данные успешно экспортированы в Excel.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ychenik_window = Ui_ychenikWindow()
    ychenik_window.show()
    sys.exit(app.exec())