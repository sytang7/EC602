# Copyright 2017 Siyuan Tang sytang7@bu.edu
"My own Polynomial"

class Polynomial(object):
    "my Polynomial class"
    def __init__(self, coefficience=None):
        """
        D = {}
        if(isinstance(coefficience,list)):
                coeff = coefficience[:]
        if(isinstance(coefficience,tuple))
                coeff
                for ind, val in enumerate(coeff):
                        if val != 0:
                                D[len(coefficience) - ind - 1] = val
                self.coeff = D
        """
        if isinstance(coefficience, dict):
            self.coeff = coefficience
        else:
            if coefficience is None:
                coefficience = [0]
            coeff = list(coefficience)
            if len(coeff) != 1:
                self.coeff = {len(coeff) - ind - 1: val for ind,
                              val in enumerate(coeff) if val != 0}
            else:
                self.coeff = {0: coeff[0]}

    def __add__(self, other):
        if self.coeff and other.coeff:
            res = {k: self.coeff.get(k, 0) + other.coeff.get(k, 0)
                   for k in set(self.coeff) | set(other.coeff)}
            return Polynomial(res)

    def __sub__(self, other):
        if self.coeff and other.coeff:
            res = {k: self.coeff.get(k, 0) - other.coeff.get(k, 0)
                   for k in set(self.coeff) | set(other.coeff)}
            return Polynomial(res)

    def __mul__(self, other):
        if self.coeff and other.coeff:
            res = {}
            for __k1, __v1 in self.coeff.items():
                for __k2, __v2 in other.coeff.items():
                    tmp = {__k1 + __k2: __v1 * __v2}
                    res = {k: tmp.get(k, 0) + res.get(k, 0)
                           for k in set(tmp) | set(res)}
            return Polynomial(res)

    def __eq__(self, other):
        if self.coeff and other.coeff:
            return self.coeff == other.coeff

    def eval(self, val):
        "evaluation of certain Polynomial"
        if self.coeff:
            res = 0
            for __k, __v in self.coeff.items():
                res += __v * val**__k
            return res

    def __getitem__(self, key):
        if self.coeff.get(key):
            res = self.coeff.get(key)
        else:
            res = 0
        return res

    def __setitem__(self, ind, val):
        tmp = {ind: val}
        self.coeff.update(tmp)
        if len(self.coeff) != 1:
            self.coeff = {k: v for k, v in self.coeff.items() if v != 0}

    def deriv(self):
        "derivation of Polynomial"
        tmp = {k - 1: k * v for k, v in self.coeff.items()}
        res = {k: v for k, v in tmp.items() if v != 0}
        return Polynomial(res)

    def __str__(self):
        res = ""
        for __k, __v in sorted(self.coeff.items(), reverse=True):
            sign = "+" if __v > 0 else "-" if __v < 0 else ""
            coeff = "" if abs(__v) == 1 and __k != 0 else str(abs(__v))
            unknow = "X" if __k != 0 else ""
            power = "" if __k == 0 or __k == 1 else "^" + str(__k)
            res += "{}{}{}{}".format(sign, coeff, unknow, power)
        if res[0] == "+":
            return res[1:]
        return res
