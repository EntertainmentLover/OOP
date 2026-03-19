import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox,
    QComboBox, QMenuBar
)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt


class BMICalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        self.setGeometry(200, 200, 420, 320)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.create_menu()
        self.create_ui()

    def create_menu(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")

        clear_action = QAction("Clear", self)
        clear_action.triggered.connect(self.clear_fields)
        file_menu.addAction(clear_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        help_menu = menu_bar.addMenu("Help")

        how_to_use_action = QAction("How to Use", self)
        how_to_use_action.triggered.connect(self.show_help)
        help_menu.addAction(how_to_use_action)

    def create_ui(self):
        main_layout = QVBoxLayout()

        title = QLabel("BMI Calculator")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 22px; font-weight: bold;")

        weight_label = QLabel("Enter Weight:")
        self.weight_input = QLineEdit()
        self.weight_input.setPlaceholderText("Example: 70")

        height_label = QLabel("Enter Height:")
        self.height_input = QLineEdit()
        self.height_input.setPlaceholderText("Example: 1.75 or 175")

        unit_label = QLabel("Select Unit System:")
        self.unit_box = QComboBox()
        self.unit_box.addItems(["Metric (kg, m)", "Metric (kg, cm)"])

        self.calc_button = QPushButton("Calculate BMI")
        self.calc_button.clicked.connect(self.calculate_bmi)

        self.result_label = QLabel("BMI: ")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setStyleSheet("font-size: 16px;")

        self.status_label = QLabel("Status: ")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet("font-size: 16px;")

        main_layout.addWidget(title)
        main_layout.addWidget(weight_label)
        main_layout.addWidget(self.weight_input)
        main_layout.addWidget(height_label)
        main_layout.addWidget(self.height_input)
        main_layout.addWidget(unit_label)
        main_layout.addWidget(self.unit_box)
        main_layout.addWidget(self.calc_button)
        main_layout.addWidget(self.result_label)
        main_layout.addWidget(self.status_label)

        self.central_widget.setLayout(main_layout)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())

            if weight <= 0 or height <= 0:
                QMessageBox.warning(self, "Input Error", "Weight and height must be greater than 0.")
                return

            unit = self.unit_box.currentText()

            if unit == "Metric (kg, cm)":
                height = height / 100

            bmi = weight / (height ** 2)
            status = self.get_bmi_status(bmi)

            self.result_label.setText(f"BMI: {bmi:.2f}")
            self.status_label.setText(f"Status: {status}")

        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numeric values.")

    def get_bmi_status(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def clear_fields(self):
        self.weight_input.clear()
        self.height_input.clear()
        self.result_label.setText("BMI: ")
        self.status_label.setText("Status: ")

    def show_help(self):
        QMessageBox.information(
            self,
            "How to Use",
            "1. Enter your weight.\n"
            "2. Enter your height.\n"
            "3. Select the correct unit system.\n"
            "4. Click 'Calculate BMI'.\n\n"
            "BMI Formula:\nWeight(kg) / Height(m)^2"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    sys.exit(app.exec())