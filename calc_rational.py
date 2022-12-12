from fractions import Fraction

def count(frac1, frac2, sign):
    if sign == '+':
        result = Fraction(frac1) + Fraction(frac2)
    return result