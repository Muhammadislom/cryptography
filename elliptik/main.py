################## 1

class Elliptic:
    def __init__(self, coordinates_p, coordinates_q, p_mod):
        self.p, self.q, self.mod_p, self.lamb, self.r = [coordinates_p, coordinates_q, p_mod, 0, [0, 0]]

    def lam(self):
        self.lamb = (int(self.q[1]) - int(self.p[1])) / (int(self.q[0]) - int(self.p[0]))
        if self.lamb % 1 == 0:
            self.lamb = self.lamb % self.mod_p
        else:
            for i in range(1, 130):
                if ((int(self.q[1]) - int(self.p[1])) % self.mod_p) == \
                        (((int(self.q[0]) - int(self.p[0])) * i) % self.mod_p):
                    self.lamb = i
                    print(f"lambda = {self.lamb}")
                    break
                else:
                    print("self.lamb = ишется")
                    continue

    def p_plus_q(self):
        self.r[0] = ((self.lamb ** 2) - int(self.p[0]) - int(self.q[0])) % self.mod_p
        self.r[1] = (self.lamb * (int(self.p[0]) - self.r[0]) - int(self.p[1])) % self.mod_p
        print(self.r)
        return self.r


#
# class Ellipticmulti:
#     def __init__(self, coordinates_p, p_mod, n):
#         self.p, self.mod_p, self.lamb, self.r, self.a = [coordinates_p, p_mod, 0, [0, 0], 1]
#         self.n = n
#
#     def lam(self):
#         self.lamb = (3 * (int(self.p[0])) ** 2 + self.a) / (2 * int(self.p[1]))
#         if self.lamb % 1 == 0:
#             self.lamb = self.lamb % self.mod_p
#         else:
#             for i in range(1, 130):
#                 if ((3 * (int(self.p[0])) ** 2 + self.a) % self.mod_p) == \
#                         (((2 * int(self.p[1])) * i) % self.mod_p):
#                     self.lamb = i
#                     print(f"lambda = {self.lamb}")
#                     break
#                 else:
#                     print("self.lamb = ишется")
#                     continue
#
#     def p_multi_q(self):
#         for i in range(0, n):
#             print(i)
#
#


if __name__ == "__main__":
    p = input("Кординаты x и y  через запятую p = ").split(',')
    q = input("Кординаты x и y  через запятую q = ").split(',')
    mod_p = int(input("mod_p = "))
    test = Elliptic(p, q, mod_p)
    test.lam()
    test.p_plus_q()

################## 2

from collections import namedtuple

Point = namedtuple("Point", "x y")

O = 'Origin'

p = 15733
a = 1
b = 3


def valid(P):
    if P == O:
        return True
    else:
        return (
                (P.y ** 2 - (P.x ** 3 + a * P.x + b)) % p == 0 and
                0 <= P.x < p and 0 <= P.y < p)


def inv_mod_p(x):
    if x % p == 0:
        raise ZeroDivisionError("Impossible inverse")
    return pow(x, p - 2, p)


def ec_inv(P):
    if P == O:
        return P
    return Point(P.x, (-P.y) % p)


def ec_add(P, Q):
    if not (valid(P) and valid(Q)):
        raise ValueError("Invalid inputs")

    if P == O:
        result = Q
    elif Q == O:
        result = P
    elif Q == ec_inv(P):
        result = O
    else:
        if P == Q:
            dydx = (3 * P.x ** 2 + a) * inv_mod_p(2 * P.y)
        else:
            dydx = (Q.y - P.y) * inv_mod_p(Q.x - P.x)
        x = (dydx ** 2 - P.x - Q.x) % p
        y = (dydx * (P.x - x) - P.y) % p
        result = Point(x, y)

    assert valid(result)
    return result
