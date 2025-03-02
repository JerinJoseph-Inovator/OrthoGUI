import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, 
    QHBoxLayout, QRadioButton, QMessageBox, QFrame
)
from PyQt5.QtGui import QPixmap
import sqlite3


class LoginApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Orthovision - Login")
        self.setGeometry(100, 100, 700, 400)

        # Main Layout
        main_layout = QHBoxLayout()

        # Left Section - X-ray Image
        self.image_label = QLabel(self)
        pixmap = QPixmap("image.png")  # Make sure "image.png" is in the same folder
        self.image_label.setPixmap(pixmap.scaled(250, 300))
        main_layout.addWidget(self.image_label)

        # Right Section - Login Fields
        form_layout = QVBoxLayout()

        self.title_label = QLabel("Orthovision")
        self.title_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #5A6CA3;")
        form_layout.addWidget(self.title_label)

        # User Type Selection (Doctor / Patient)
        button_layout = QHBoxLayout()
        self.radio_doctor = QPushButton("Doctor")
        self.radio_patient = QPushButton("Patient")
        self.radio_doctor.setCheckable(True)
        self.radio_patient.setCheckable(True)

        self.radio_doctor.setStyleSheet(self.get_button_style())
        self.radio_patient.setStyleSheet(self.get_button_style())

        self.radio_doctor.clicked.connect(lambda: self.update_fields("Doctor"))
        self.radio_patient.clicked.connect(lambda: self.update_fields("Patient"))

        button_layout.addWidget(self.radio_doctor)
        button_layout.addWidget(self.radio_patient)
        form_layout.addLayout(button_layout)

        # Email / Number Field
        self.label_id = QLabel("Email / Number:")
        self.input_id = QLineEdit()
        self.input_id.setStyleSheet(self.get_input_style())

        # Password Field
        self.label_password = QLabel("Password:")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setStyleSheet(self.get_input_style())

        form_layout.addWidget(self.label_id)
        form_layout.addWidget(self.input_id)
        form_layout.addWidget(self.label_password)
        form_layout.addWidget(self.input_password)

        # Login Button
        self.button_login = QPushButton("Login")
        self.button_login.setStyleSheet(self.get_button_style())
        self.button_login.clicked.connect(self.authenticate)
        form_layout.addWidget(self.button_login)

        # Processing Label
        self.processing_label = QLabel("Processing data...")
        self.processing_label.setStyleSheet("color: #5A6CA3; font-style: italic;")
        self.processing_label.setVisible(False)
        form_layout.addWidget(self.processing_label)

        main_layout.addLayout(form_layout)
        self.setLayout(main_layout)

    def get_button_style(self):
        return """
            QPushButton {
                background-color: #5A6CA3; 
                color: white; 
                border-radius: 10px; 
                padding: 5px;
                font-size: 14px;
            }
            QPushButton:checked {
                background-color: #3A4A80;
            }
            QPushButton:hover {
                background-color: #3F5BA9;
            }
        """

    def get_input_style(self):
        return """
            QLineEdit {
                border: 2px solid #5A6CA3;
                border-radius: 8px;
                padding: 5px;
                font-size: 14px;
            }
        """

    def update_fields(self, user_type):
        """ Change label based on selection """
        if user_type == "Doctor":
            self.label_id.setText("Email:")
            self.radio_patient.setChecked(False)
            self.radio_doctor.setChecked(True)
        else:
            self.label_id.setText("Registered Number:")
            self.radio_doctor.setChecked(False)
            self.radio_patient.setChecked(True)

    def authenticate(self):
        """ Check credentials from SQLite database """
        user_type = "Doctor" if self.radio_doctor.isChecked() else "Patient"
        user_id = self.input_id.text()
        password = self.input_password.text()

        if not user_id or not password:
            QMessageBox.warning(self, "Login Failed", "Please enter all details!")
            return

        # Connect to database
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE UserType=? AND ID=? AND Password=?", (user_type, user_id, password))
        result = cursor.fetchone()
        conn.close()

        if result:
            QMessageBox.information(self, "Login Successful", f"Welcome, {user_type}!")
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid Credentials!")


# Run the App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec_())
