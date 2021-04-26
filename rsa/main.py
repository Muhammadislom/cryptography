from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from rsa_ui import *


class mainRsa(QMainWindow):
    def __init__(self):
        super(mainRsa, self).__init__()
        self.main = Ui_RSA()
        self.main.setupUi(self)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainRsa()
    sys.exit(app.exec_())
