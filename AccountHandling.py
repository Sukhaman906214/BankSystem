
# gui.py
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
)
import sys



class AccountManagementApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Account Management")
        self.setGeometry(100, 100, 400, 300)

        # Initialize GUI components
        self.create_account_label = QLabel("Create New Account:")
        self.account_number_label = QLabel("Account Number:")
        self.account_number_input = QLineEdit()
        self.account_type_label = QLabel("Account Type:")
        self.account_type_input = QLineEdit()
        self.create_account_button = QPushButton("Create Account")

        # Layout for create account form
        self.create_account_layout = QVBoxLayout()
        self.create_account_layout.addWidget(self.create_account_label)
        self.create_account_layout.addWidget(self.account_number_label)
        self.create_account_layout.addWidget(self.account_number_input)
        self.create_account_layout.addWidget(self.account_type_label)
        self.create_account_layout.addWidget(self.account_type_input)
        self.create_account_layout.addWidget(self.create_account_button)

        self.setLayout(self.create_account_layout)
       
        self.create_account_button.clicked.connect()

            def create_account(self):
        # Get account number and type from input fields
        account_number = self.account_number_input.text()
        account_type = self.account_type_input.text()
       
   

    

       

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AccountManagementApp()
    window.show()
    sys.exit(app.exec_())
