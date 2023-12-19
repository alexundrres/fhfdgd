from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QComboBox, QMessageBox
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

class BankApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.add_client_window = None

        self.setWindowTitle("Авторизация")

        self.login_label = QLabel("Логин:")
        self.login_entry = QLineEdit()
        self.password_label = QLabel("Пароль:")
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Войти", self)
        self.login_button.clicked.connect(self.login)

        layout = QVBoxLayout()
        layout.addWidget(self.login_label)
        layout.addWidget(self.login_entry)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_entry)
        layout.addWidget(self.login_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.create_clients_table()

    def create_clients_table(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("bank_app.db")
        if not db.open():
            print("Cannot open database")
            return False

        query = QSqlQuery()
        query.exec('''CREATE TABLE IF NOT EXISTS clients (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        fio TEXT,
                        passport_series TEXT,
                        passport_number TEXT,
                        inn TEXT,
                        account_type TEXT)''')


    def login(self):
        valid_login = self.login_entry.text() == "user"
        valid_password = self.password_entry.text() == "password"

        if valid_login and valid_password:
            self.show_clients_window()
            self.close()
        else:
            QMessageBox.critical(self, "Ошибка", "Неправильный логин или пароль")

    def show_clients_window(self):
        self.clients_window = QMainWindow()
        self.clients_window.setWindowTitle("КЛИЕНТЫ БАНКА")

        self.clients_table = QTableWidget()
        self.clients_table.setColumnCount(6)
        self.clients_table.setHorizontalHeaderLabels(["ID", "ФИО", "Серия паспорта", "Номер паспорта", "ИНН", "Вид счета"])

        add_button = QPushButton("Добавить клиента", self)
        add_button.clicked.connect(self.add_client_window)

        delete_button = QPushButton("Удалить клиента", self)
        delete_button.clicked.connect(self.delete_client)

        exit_button = QPushButton("Выход", self)
        exit_button.clicked.connect(self.confirm_exit)

        layout = QVBoxLayout()
        layout.addWidget(self.clients_table)
        layout.addWidget(add_button)
        layout.addWidget(delete_button)
        layout.addWidget(exit_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.clients_window.setCentralWidget(central_widget)

        self.update_clients_table()

        self.clients_window.show()

    def add_client_window(self):
        self.add_client_window = QMainWindow()
        self.add_client_window.setWindowTitle("Добавление клиента")

        fio_label = QLabel("ФИО:")
        self.fio_entry = QLineEdit()

        passport_series_label = QLabel("Серия паспорта:")
        self.passport_series_entry = QLineEdit()

        passport_number_label = QLabel("Номер паспорта:")
        self.passport_number_entry = QLineEdit()

        inn_label = QLabel("ИНН:")
        self.inn_entry = QLineEdit()

        account_type_label = QLabel("Желаемый счет:")
        self.account_type_combobox = QComboBox()
        self.account_type_combobox.addItems(["Расчетный", "Бюджетный", "Текущий"])

        save_button = QPushButton("Сохранить", self)
        save_button.clicked.connect(self.save_client)


        layout = QVBoxLayout()
        layout.addWidget(fio_label)
        layout.addWidget(self.fio_entry)
        layout.addWidget(passport_series_label)
        layout.addWidget(self.passport_series_entry)
        layout.addWidget(passport_number_label)
        layout.addWidget(self.passport_number_entry)
        layout.addWidget(inn_label)
        layout.addWidget(self.inn_entry)
        layout.addWidget(account_type_label)
        layout.addWidget(self.account_type_combobox)
        layout.addWidget(save_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.add_client_window.setCentralWidget(central_widget)

        self.add_client_window.show()

    def save_client(self):
        db = QSqlDatabase.database()
        if not db.open():
            print("Cannot open database")
            return

        query = QSqlQuery()
        query.prepare(
            'INSERT INTO clients (fio, passport_series, passport_number, inn, account_type) VALUES (?, ?, ?, ?, ?)')
        query.addBindValue(self.fio_entry.text())
        query.addBindValue(self.passport_series_entry.text())
        query.addBindValue(self.passport_number_entry.text())
        query.addBindValue(self.inn_entry.text())
        query.addBindValue(self.account_type_combobox.currentText())
        query.exec()

        # Добавьте следующую строку для сохранения изменений
        db.commit()

        self.update_clients_table()
        QMessageBox.information(self, "Успех", "Клиент добавлен успешно")

        # Закрытие окна после сохранения
        if self.add_client_window:
            self.add_client_window.close()


    def delete_client(self):
        selected_row = self.clients_table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Предупреждение", "Выберите клиента для удаления.")
            return

        db = QSqlDatabase.database()
        if not db.open():
            print("Cannot open database")
            return

        query = QSqlQuery()
        query.prepare('DELETE FROM clients WHERE id = ?')
        query.addBindValue(self.clients_table.item(selected_row, 0).text())
        query.exec()

        self.update_clients_table()
        QMessageBox.information(self, "Успех", "Клиент успешно удален.")

    def confirm_exit(self):
        exit_button = QMessageBox.question(self, 'Подтверждение выхода', 'Вы точно хотите завершить сессию?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if exit_button == QMessageBox.StandardButton.Yes:
            self.clients_window.close()  # Закрываем окно КЛИЕНТЫ БАНКА
            self.close()  # Закрываем главное окно
        else:
            pass

    def update_clients_table(self):
        db = QSqlDatabase.database()
        if not db.open():
            print("Cannot open database")
            return

        query = QSqlQuery()
        query.exec('SELECT * FROM clients')

        self.clients_table.setRowCount(0)

        while query.next():
            row_position = self.clients_table.rowCount()
            self.clients_table.insertRow(row_position)

            for column in range(6):
                item = QTableWidgetItem(str(query.value(column)))
                self.clients_table.setItem(row_position, column, item)

if __name__ == "main":
    app = QApplication([])
    window = BankApp()
    window.show()
    app.exec()