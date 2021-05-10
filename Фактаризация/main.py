""" Значени p и q может различатся местами в методах но суть не меняется значения всё равно верно"""
# Muhammadislom ;)

# Первый метод
class Ferma:
    def perfectSquare(self, x):
        return (int(x ** 0.5)) ** 2 == x

    def factorizeFerma(self, n):
        x = int(n ** 0.5) + 1
        while not self.perfectSquare(x * x - n):
            x += 1
        y = int((x * x - n) ** 0.5)
        a = x - y
        b = x + y
        return a, b


# Второй метод
class Factory:
    def __init__(self, n):
        self.n, self.x, self.y = [n, 2, 2]

    def gcd(self, a, b):
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a

    def fac_start(self):
        while True:
            fx = abs(((self.x ** 2 + 1) % self.n) - ((((((self.y ** 2) % self.n) + 1) ** 2) % self.n + 1) % self.n))
            result = self.gcd(fx, self.n)
            if result != 1:
                return result, int(self.n / result)
            else:
                self.x = (self.x ** 2 + 1) % self.n
                self.y = ((self.y ** 2 + 1) ** 2 + 1) % self.n

# Проверка
n = int(input("n = "))
test1 = Ferma()
a1, b1 = test1.factorizeFerma(n)
#################################################
test2 = Factory(n)
a2, b2 = test2.fac_start()
#################################################
print(f"По первому метода p = {a1}, q ={b1} \n"
      f"По второму методу p = {a2}, q = {b2}")
