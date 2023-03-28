# Implementieren Sie ein kleines Glückspiel für zwei Spieler, die je einen Tipp abgeben für eine Zufallszahl zwischen 1
#     und 100. Dann wird diese Zufallszahl ermittelt, der Spieler, der mit seinem Tipp näher bei der Zufallszahl liegt, gewinnt
#     das Spiel. Liegen beide Spieler gleich weit entfernt mit ihrem Tipp, gibt’s ein Unentschieden.

import random


def closest_number(num1, num2):
    """ Berechnet die Zahl, welche nächer bei der Zufallszahl liegt"""

    # Zufallszahl
    random_number = random.randint(1, 100)
    print(f'Die Zufallszahl ist {random_number}!')

    # Prüfung
    if abs(num1 - random_number) < abs(num2 - random_number):
      return num1
    elif abs(num1 - random_number) > abs(num2 - random_number):
      return num2
    else:
      return num1 + num2


# Input
num1 = int(input("Spieler 1, geben Sie eine ganze Zahl zwischen 1 und 100 ein: "))
num2 = int(input("Spieler 2, geben Sie eine ganze Zahl zwischen 1 und 100 ein: "))

# Funktionsaufruf mit Inputs als Argumente. Zuweisung des Resultats an eine Variable
closer_num = closest_number(num1, num2)

# Prüfung des Resultats und entsprechende Ausgabe
if closer_num == num1 + num2:
    print('Beide Nummern haben gewonnen, es ist unentschieden')
else:
    print("Gewonnen hat die Nummer: ", closer_num)

