import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout,
    QPushButton, QLineEdit, QListWidget, QHBoxLayout
)


# ===== MODEL =====
class Calculator:
    def __init__(self):
        self.expression = ""

    def add_to_expression(self, char: str):
        self.expression += char

    def remove_last_character(self):
        self.expression = self.expression[:-1]

    def clear_expression(self):
        self.expression = ""

    def calculate(self):
        try:
            result = eval(self.expression)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            return str(result)
        except ZeroDivisionError:
            return "Cannot divide by zero"
        except:
            return "Error"

    def get_expression(self):
        return self.expression


# ===== VIEW + CONTROLLER =====
class CalculatorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.calculator = Calculator()

        self.setWindowTitle("Calculator")
        self.setFixedSize(600, 540)

        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #0f172a;
            }
            QLineEdit {
                background-color: #111827;
                color: white;
                border: 2px solid #1f2937;
                border-radius: 18px;
                padding: 18px;
                font-size: 30px;
            }
            QPushButton {
                border: none;
                border-radius: 18px;
                font-size: 20px;
                font-weight: bold;
                min-height: 70px;
            }
            QPushButton#digitButton {
                background-color: #1e293b;
                color: white;
            }
            QPushButton#digitButton:hover {
                background-color: #334155;
            }
            QPushButton#operatorButton {
                background-color: #f59e0b;
                color: white;
            }
            QPushButton#operatorButton:hover {
                background-color: #fbbf24;
            }
            QPushButton#clearButton {
                background-color: #ef4444;
                color: white;
            }
            QPushButton#clearButton:hover {
                background-color: #f87171;
            }
            QPushButton#equalButton {
                background-color: #10b981;
                color: white;
            }
            QPushButton#equalButton:hover {
                background-color: #34d399;
            }
            QListWidget {
                background-color: #111827;
                color: #e5e7eb;
                border-radius: 18px;
                padding: 10px;
                font-size: 16px;
            }
        """)

        main_layout = QHBoxLayout()

        # ===== LEFT (Calculator) =====
        left_layout = QVBoxLayout()

        self.input = QLineEdit()
        self.input.setReadOnly(True)
        self.input.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.input.setFont(QFont("Arial", 20))
        left_layout.addWidget(self.input)

        grid = QGridLayout()
        grid.setSpacing(12)

        buttons = [
            ("C", 0, 0, "clear"),
            ("(", 0, 1, "digit"),
            (")", 0, 2, "digit"),
            ("/", 0, 3, "operator"),

            ("7", 1, 0, "digit"),
            ("8", 1, 1, "digit"),
            ("9", 1, 2, "digit"),
            ("*", 1, 3, "operator"),

            ("4", 2, 0, "digit"),
            ("5", 2, 1, "digit"),
            ("6", 2, 2, "digit"),
            ("-", 2, 3, "operator"),

            ("1", 3, 0, "digit"),
            ("2", 3, 1, "digit"),
            ("3", 3, 2, "digit"),
            ("+", 3, 3, "operator"),

            ("0", 4, 0, "digit"),
            (".", 4, 1, "digit"),
            ("<-", 4, 2, "digit"),
            ("=", 4, 3, "equal"),
        ]

        for text, row, col, kind in buttons:
            button = QPushButton(text)

            if kind == "digit":
                button.setObjectName("digitButton")
            elif kind == "operator":
                button.setObjectName("operatorButton")
            elif kind == "clear":
                button.setObjectName("clearButton")
            elif kind == "equal":
                button.setObjectName("equalButton")

            button.clicked.connect(self.on_button_click)
            grid.addWidget(button, row, col)

        left_layout.addLayout(grid)

        # ===== RIGHT (History) =====
        self.history = QListWidget()

        # ===== COMBINE =====
        main_layout.addLayout(left_layout, 2)
        main_layout.addWidget(self.history, 1)

        self.setLayout(main_layout)

    def on_button_click(self):
        button = self.sender()
        text = button.text()

        if text == "C":
            self.calculator.clear_expression()
            self.input.setText("")

        elif text == "<-":
            self.calculator.remove_last_character()
            self.input.setText(self.calculator.get_expression())

        elif text == "=":
            expr = self.calculator.get_expression()
            result = self.calculator.calculate()

            # добавляем в историю
            self.history.addItem(f"{expr} = {result}")

            self.input.setText(result)

            if result not in ["Error", "Cannot divide by zero"]:
                self.calculator.expression = result
            else:
                self.calculator.clear_expression()

        else:
            self.calculator.add_to_expression(text)
            self.input.setText(self.calculator.get_expression())


# ===== MAIN =====
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec())