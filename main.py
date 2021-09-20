from entryPointUI import Ui_EntryPoint
from PyQt6 import QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_EntryPoint()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())