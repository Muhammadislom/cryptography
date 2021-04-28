from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint
from math import sqrt
from itertools import count, islice
from rsa_ui import *
import sys
import math


def isPrime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


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
            return
        if self.main.inp_val_p.text().isdigit() == False or self.main.inp_val_q.text().isdigit() == False or \
                self.main.inp_val_e.text().isdigit() == False:
            self.main.consolLable.setText("Введите челое число !")
            return
        if is_coprime(int(self.main.inp_val_p.text()), int(self.main.inp_val_q.text())) == False:
            self.main.consolLable.setText("Значения чисел (p, q) не евляются взаимно простыми")
            return
        self.Fn = (int(self.main.inp_val_p.text()) - 1) * (int(self.main.inp_val_q.text()) - 1)
        self.main.val_fn_number.setText(str(self.Fn))
        self.n = int(self.main.inp_val_p.text()) * int(self.main.inp_val_q.text())
        self.main.val_n_number.setText(str(self.n))
        if is_coprime(int(self.main.inp_val_e.text()), self.Fn) == False:
            self.main.consolLable.setText("Значения чисел (e, F(n)) не евляются взаимно простыми")
            return
        if int(self.main.inp_val_e.text()) > self.Fn:
            self.main.consolLable.setText("e должно быть меньше F(n)")
            return
        if isPrime(int(self.main.inp_val_e.text())) == False:
            self.main.consolLable.setText("e не простое число")
            return
        for i in range(1, 550):
            if (i * int(self.main.inp_val_e.text())) % self.Fn == 1:
                self.d = i
                self.main.np_d_number.setText(str(self.d))
            else:
                continue
            if i == 99:
                self.main.consolLable.setText("Значение d не было найденно")
                break

        self.main.consolLable.setText("Можете продолжать")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainRsa()
    sys.exit(app.exec_())
