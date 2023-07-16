import pytest
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMessageBox
from function_plotter import FunctionPlotter, function_error_message, min_max_error_message


def test_plot_function_valid_input(qtbot):
    """
    Test the plot_function method with valid input.
    """
    window = FunctionPlotter()
    window.function_input.setText("x**2")
    window.min_input.setText("0")
    window.max_input.setText("10")

    qtbot.mouseClick(window.plot_button, Qt.LeftButton)

    # Check if the plot is generated
    assert len(window.figure.axes) == 1

    # Check if no error message box is displayed
    assert window.message_box.isHidden()


