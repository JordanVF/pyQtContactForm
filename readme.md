# PyQt Contact Form

## Description
This is a simple contact form application built using `PyQt6`. The form collects the user's name, email, phone number, subject of the message, and the message itself. When the user submits the form, the entered information is printed to the console, and the form resets for further input.

## Installation 
1. Clone the repository:
   ```bash
   git clone https://github.com/JordanVF/pyQtContactForm.git
2. Navigate to the project directory: 
```bash
cd pyQtContactForm
```
3. Install the required dependencies:
```bash
pip install PyQt6
```
 
## Usage
1. Run the application
2. Fill out the contact form by entering the following details:
   - Name: Your full name
   - Email: Your email address
   - Phone: Your contact number
   - Subject: Select the subject type (Personal or Business)
   - Message: Enter your message
3. Click the Submit button. After submitting, the entered information will be printed to the console, and the form will reset.

## How it works
- PyQt6 Widgets: The form is built using several PyQt6 widgets: 
   - QLineEdit for text input fields (Name, Email, and Phone)
   - QComboBox for selecting the subject
   - QTextEdit for multi-line message input
   - QPushButton for the submit button
- Form Submission: When the submit button is clicked, the entered information is gathered and printed to the console. After submission, the form fields are cleared, allowing for new input.
- Form Layout: A QFormLayout is used to structure the form with labels and their corresponding input fields.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

