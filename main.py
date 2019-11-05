from STools import STools
import sys
from PyQt5 import QtWidgets as Wid

if __name__ == '__main__':
    app = Wid.QApplication(sys.argv)
    program = STools()
    program.show()
    sys.exit(app.exec())
