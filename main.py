import PySide2.QtWidgets
import sys
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class FunctionPlotter(PySide2.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Function Plotter")
        self.setGeometry(100, 100, 800, 600)

        self.function_label = PySide2.QtWidgets.QLabel("Enter your function:")
        self.function_input = PySide2.QtWidgets.QLineEdit()
        self.min_label = PySide2.QtWidgets.QLabel("Enter minimum value:")
        self.min_input = PySide2.QtWidgets.QLineEdit()
        self.max_label = PySide2.QtWidgets.QLabel("Enter maximum value:")
        self.max_input = PySide2.QtWidgets.QLineEdit()
        self.plot_button = PySide2.QtWidgets.QPushButton("Plot")
        self.plot_button.clicked.connect(self.plot_function)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.layout = PySide2.QtWidgets.QVBoxLayout()

        # Create a QHBoxLayout for the input labels and fields
        input_layout = PySide2.QtWidgets.QHBoxLayout()
        input_layout.addWidget(self.function_label)
        input_layout.addWidget(self.function_input)

        # Create a QHBoxLayout for the min labels and max
        min_layout = PySide2.QtWidgets.QHBoxLayout()
        min_layout.addWidget(self.min_label)
        min_layout.addWidget(self.min_input)
        min_layout.addWidget(self.max_label)
        min_layout.addWidget(self.max_input)

        # Set the font size for the labels and input fields
        font = PySide2.QtGui.QFont()
        font.setPointSize(14)
        self.function_label.setFont(font)
        self.function_input.setFont(font)
        self.min_label.setFont(font)
        self.min_input.setFont(font)
        self.max_label.setFont(font)
        self.max_input.setFont(font)

        # Add margin between the labels and input fields
        input_layout.setContentsMargins(10, 30, 15, 30)
        min_layout.setContentsMargins(10, 15, 30, 30)

        # Change the size and color of the button
        button_font = PySide2.QtGui.QFont()
        button_font.setPointSize(12)
        self.plot_button.setFont(button_font)
        self.plot_button.setStyleSheet("background-color: #ffcc00; color: #000000;")
        self.plot_button.setFixedWidth(100)

        # Create a QHBoxLayout for the button with centered alignment
        button_layout = PySide2.QtWidgets.QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(self.plot_button)
        button_layout.addStretch(1)

        # Add the input layout, button layout, and other widgets to the main layout
        self.layout.addLayout(input_layout)
        self.layout.addLayout(min_layout)
        self.layout.addLayout(button_layout)
        self.layout.addWidget(self.canvas)

        self.central_widget = PySide2.QtWidgets.QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def plot_function(self):

        input_function = self.function_input.text()
        min_input_text = self.min_input.text()
        max_input_text = self.max_input.text()

        # Check if either min or max value is empty

        valid_function = self.validate_input(input_function)
        valid_min_max = self.validate_min_max(min_input_text, max_input_text)

        if valid_function and valid_min_max:

            min_value = eval(min_input_text)
            max_value = eval(max_input_text)

            x = sp.symbols('x')
            expression = sp.sympify(input_function)

            # Generate x values using NumPy's linspace
            x_values = np.linspace(min_value, max_value, 500)
            y_values = [expression.subs(x, val) for val in x_values]

            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(x_values, y_values)

            self.canvas.draw()

        elif not valid_function:
            self.show_invalid_input_function()
        elif not valid_min_max:
            self.show_min_max_error()



    def validate_input(self, input_check):
        try:
            x = sp.symbols('x')
            expression = sp.sympify(input_check)
            expression.subs(x, 0)  # Evaluate the expression at x=0
            return True
        except (sp.SympifyError, TypeError):
            return False

    def validate_min_max(self, min_input_text, max_input_text):
        if not min_input_text or not max_input_text:
            return False

        try:
            min_value = float(min_input_text)
            max_value = float(max_input_text)
            return True
        except ValueError:
            return False

    def show_min_max_error(self):
        error_message = "Your minimum and maximum value is not valid. Please enter a valid input values."
        message_box = PySide2.QtWidgets.QMessageBox(self)
        message_box.setIcon(PySide2.QtWidgets.QMessageBox.Critical)
        message_box.setWindowTitle("Error")
        message_box.setText(error_message)
        message_box.addButton(PySide2.QtWidgets.QMessageBox.Ok)
        message_box.exec_()
        return

    def show_invalid_input_function(self):
        error_message = "Your function is not valid. Please enter a valid input function."
        message_box = PySide2.QtWidgets.QMessageBox(self)
        message_box.setIcon(PySide2.QtWidgets.QMessageBox.Critical)
        message_box.setWindowTitle("Error")
        message_box.setText(error_message)
        message_box.addButton(PySide2.QtWidgets.QMessageBox.Ok)
        message_box.exec_()
        return


if __name__ == "__main__":
    app = PySide2.QtWidgets.QApplication(sys.argv)
    window = FunctionPlotter()
    window.show()
    sys.exit(app.exec_())
