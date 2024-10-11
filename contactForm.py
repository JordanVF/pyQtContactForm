import sys
from PyQt6.QtWidgets import QWidget,QApplication,QLabel,QLineEdit,QFormLayout,QComboBox,QTextEdit,QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("QForm Layout")
        self.setGeometry(100,100,400,300)

        form_layout = QFormLayout()
        self.setLayout(form_layout)

        #Contact Information
        self.name_edit = QLineEdit()
        self.phone_edit = QLineEdit()
        self.email_edit = QLineEdit()

        #Subject
        self.subject_combo = QComboBox()
        self.subject_combo.addItems(["Select Subject","Personal","Business"])

        #Message
        self.message_edit = QTextEdit()

        #Submit
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit_clicked)

        #region Form
        form_layout.addRow(QLabel("Name:"),self.name_edit)
        form_layout.addRow(QLabel("Email:"),self.email_edit)
        form_layout.addRow(QLabel("Cell No.:"),self.phone_edit)
        form_layout.addRow(QLabel("Subject:"),self.subject_combo)
        form_layout.addRow(QLabel("Message:"),self.message_edit)
        form_layout.addRow(submit_button)
        #endregion

    def submit_clicked(self):
        name = self.name_edit.text()
        email = self.email_edit.text()
        phone = self.phone_edit.text()
        subject = self.subject_combo.currentText()
        message = self.message_edit.toPlainText()

        print(f"Name: {name}\nEmail: {email}\nPhone: {phone}\nSubject: {subject}\nMessage: {message}")

        # Reset after submit
        self.name_edit.setText("")
        self.email_edit.setText("")
        self.phone_edit.setText("")
        self.subject_combo.setCurrentIndex(0)
        self.message_edit.setText("")



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())