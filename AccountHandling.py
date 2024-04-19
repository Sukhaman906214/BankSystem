
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
from AccountManagement.CreateAccount import CreateAccountWidget
from AccountManagement.UpdateAccount import  UpdateAccountWidget
from AccountManagement.DeleteAccount import DeleteAccountWidget
import sys



class AccountWindow(QWidget):
    go_back = pyqtSignal()
    create_account_signal = pyqtSignal()
    update_account_signal = pyqtSignal()
    delete_account_signal = pyqtSignal()
    edit_account_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Account Management System")
        self.setGeometry(100, 100, 400, 300)

        
        self.button_layout = QVBoxLayout()

        self.create_account_button = QPushButton("Create Account", self)
       self.create_account_button.clicked.connect(self.create_account_signal.emit)
        
        self.update_account_button = QPushButton("Update Account", self)
       
        self.update_account_button.clicked.connect(self.update_account_signal.emit)
        
        self.delete_account_button = QPushButton("Delete Account", self)
        self.delete_account_button.clicked.connect(self.delete_account_signal.emit)

        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.go_back_to_main_menu)
    def go_back_to_main_menu(self):
        self.go_back.emit()
        self.close()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AccountWindow()
    window.show()
    sys.exit(app.exec_())
