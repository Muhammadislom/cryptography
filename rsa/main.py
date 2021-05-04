from PyQt5.QtWidgets import QApplication, QMainWindow
from math import sqrt
from itertools import count, islice
from rsa_ui import *
import sys
import math

clousea = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm',
           14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y',
           26: 'z'}
opena = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
         'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
         'z': 26}
openText = ''
clouseText = ''


def isPrime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


def is_coprime(x, y):
    return math.gcd(x, y) == 1


class MainRsa(QMainWindow):
    def __init__(self):
        super(MainRsa, self).__init__()
        self.main = Ui_RSA()
        self.main.setupUi(self)
        self.main.pnq_button.clicked.connect(self.validation)
        self.main.shifrButton.clicked.connect(self.encryption)
        self.main.deshifrButton.clicked.connect(self.decription)

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
        for i in range(1, 100):
            if (i * int(self.main.inp_val_e.text())) % self.Fn == 1:
                self.d = i
                self.main.np_d_number.setText(str(self.d))
            else:
                continue
            if i == 99:
                self.main.consolLable.setText("Значение d не было найденно")
                break

        self.main.consolLable.setText("Можете продолжать")

    def encryption(self):
        global openText
        self.main.clousText.setText(" ")
        for i in self.main.openText.toPlainText():
            openText = str(openText) + str(
                clousea[(opena[i] ** int(self.main.inp_val_e.text())) % int(self.main.val_n_number.text())])
        self.main.clousText.setText(openText)

    def decription(self):
        print(self.main.clousText.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainRsa()
    sys.exit(app.exec_())
