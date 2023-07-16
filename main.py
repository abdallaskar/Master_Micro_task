'''
 Author  : Abdalla Sakr
 Data    : 15 July 2023
 Version : 1.0
'''


import PySide2, sys
from function_plotter import FunctionPlotter

if __name__ == "__main__":
    app = PySide2.QtWidgets.QApplication(sys.argv)
    window = FunctionPlotter()
    window.show()
    sys.exit(app.exec_())
