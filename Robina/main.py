# Muhammadislom

class Robina():
    def __init__(self, openText, p, q):
        self.openText, self.p, self.q, self.closeText = [openText, p, q, ""]

    def IsPrime(self, n):
        d = 2
        while n % d != 0:
            d += 1
        return bool(d == n)

    def validation(self):
        while True:
            if self.p % 4 == 3 and q % 4 == 3 and self.IsPrime(self.p) == True and self.IsPrime(self.q) == True:
                self.openKey = self.p * self.q
                break
            elif self.p % 4 != 3 or self.IsPrime(self.p) == False:
                self.p = int(input("p не верное значени попробуйте сново p = "))
                continue
            elif self.q % 4 != 3 or self.IsPrime(self.q) == False:
                self.p = int(input("q не верное значени попробуйте сново q = "))
                continue

    def encriptions(self):
        for i in self.openText:
            self.closeText = self.closeText + str((ord(i) ** 2) % self.openKey)
            print(f'closeText = {i} = {ord(i)} -> {ord(i)}^2 mod {self.openKey} = {self.closeText[-1]}')
        print(f"Закрытый текст = {self.closeText}")


if __name__ == "__main__":
    p = int(input("p = "))
    q = int(input("q = "))
    string = input("Открытый текст -> ")
    test = Robina(string, p, q)
    test.validation()
    test.encriptions()
