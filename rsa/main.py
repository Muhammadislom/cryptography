from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from rsa_ui import *

import math


def is_coprime(x, y):
    return math.gcd(x, y) == 1


class mainRsa(QMainWindow):
    def __init__(self):
        super(mainRsa, self).__init__()
        self.main = Ui_RSA()
        self.main.setupUi(self)
        self.main.pnq_button.clicked.connect(self.validation)
        self.show()

    def validation(self):
        if bool(self.main.inp_val_p.text()) == False or bool(self.main.inp_val_q.text()) == False or \
                bool(self.main.inp_val_e.text()) == False:
            self.main.consolLable.setText("Заполгите все значения (p, q, e)")
        elif self.main.inp_val_p.text().isdigit() == False or self.main.inp_val_q.text().isdigit() == False or \
                self.main.inp_val_e.text().isdigit() == False:
            self.main.consolLable.setText("Введите челое число !")
        elif is_coprime(int(self.main.inp_val_p.text()), int(self.main.inp_val_q.text())) == False or is_coprime(
                int(self.main.inp_val_p.text()), int(self.main.inp_val_e.text())) == False or \
                is_coprime(int(self.main.inp_val_q.text()), int(self.main.inp_val_e.text())) == False:
            self.main.consolLable.setText("Значения чисел (p, q, e) не евляются взаимно простыми")
        else:
            self.main.consolLable.setText("Всё отлично")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainRsa()
    sys.exit(app.exec_())
