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


def test_invalid_func(qtbot):
    window = FunctionPlotter()
    window.function_input.setText("x^3+")
    window.min_input.setText("5")
    window.max_input.setText("125")

    assert isinstance(qtbot, object)
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)

    assert len(window.figure.axes) == 0
    assert window.message_box.isEnabled()


def test_invalid_symbol(qtbot):
    window = FunctionPlotter()
    window.function_input.setText("y^3+3*y")
    window.min_input.setText("5")
    window.max_input.setText("125")

    assert isinstance(qtbot, object)
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)

    assert len(window.figure.axes) == 0
    assert window.message_box.isEnabled()


def test_invalid_min(qtbot):
    window = FunctionPlotter()
    window.function_input.setText("x^3")
    window.min_input.setText("a")
    window.max_input.setText("125")

    assert isinstance(qtbot, object)
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)

    assert len(window.figure.axes) == 0
    assert window.message_box.isEnabled()


def test_invalid_max(qtbot):
    window = FunctionPlotter()
    window.function_input.setText("x^2 + 3*x")
    window.min_input.setText("5")
    window.max_input.setText("")

    assert isinstance(qtbot, object)
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)

    assert len(window.figure.axes) == 0
    assert window.message_box.isEnabled()
