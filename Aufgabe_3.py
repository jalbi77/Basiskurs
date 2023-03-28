# Aufgabe 3

import math


kathete_1 = float(input('Länge Kathete 1: '))
kathete_2 = float(input('Länge Kathete 2: '))


def hypotenuse():
    print(f'Die Hypotenuse im rechtwinkligen Dreieck beträgt {math.sqrt((kathete_1 ** 2) + (kathete_2 ** 2))}')


hypotenuse()
