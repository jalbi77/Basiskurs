# Implementieren Sie ein kleines Glückspiel für zwei Spieler, die je einen Tipp abgeben für eine Zufallszahl zwischen 1
#     und 100. Dann wird diese Zufallszahl ermittelt, der Spieler, der mit seinem Tipp näher bei der Zufallszahl liegt, gewinnt
#     das Spiel. Liegen beide Spieler gleich weit entfernt mit ihrem Tipp, gibt’s ein Unentschieden.
#     Zusatzaufgabe: Erweitern Sie Ihr Spiel für drei Spieler! Liegen alle drei Spieler mit ihrem Tipp gleich weit entfernt, gibt’s
#     ein Unentschieden, liegen zwei Spieler gleich weit entfernt, gewinnen sie beide das Spiel (natürlich nur, wenn sie
#     besser getippt haben als der dritte Spieler)

import random

def winner(guess1, guess2, guess3, num):
    """ Berechnung der Distanzen der Tipps zur Zufallszahl und Prüfung"""

    # Distanzberechnungen
    distance1 = abs(num - guess1)
    distance2 = abs(num - guess2)
    distance3 = abs(num - guess3)

    # Prüfung auf einzelne Gewinner
    if distance1 < distance2 and distance1 < distance3:
        return 1
    elif distance2 < distance1 and distance2 < distance3:
        return 2
    elif distance3 < distance1 and distance3 < distance2:
        return 3
    # Prüfung auf unentschieden
    elif distance1 == distance2 and distance2 == distance3:
        return 0
    # Prüfung auf zweifache Gewinner
    elif distance1 == distance2:
        return 1, 2
    elif distance1 == distance3:
        return 1, 3
    else:
        return 2, 3

def play_game():
    """ Eingabe der Tipps, Aufruf der Funktion zur Berechnung und Ausgabe des Resultats """

    # Eingabe
    player1 = int(input("Spieler 1, geben Sie eine ganze Zahl zwischen 1 und 100 ein: "))
    player2 = int(input("Spieler 2, geben Sie eine ganze Zahl zwischen 1 und 100 ein: "))
    player3 = int(input("Spieler 3, geben Sie eine ganze Zahl zwischen 1 und 100 ein: "))

    #Zufallszahl
    random_num = random.randint(1, 100)
    print("Die Zufallszahl ist:", random_num)

    # Funktionsaufruf mit Inputs als Argumente. Zuweisung des Resultats an eine Variable
    result = winner(player1, player2, player3, random_num)

    # Prüfung des Resultats und entsprechende Ausgabe
    if result == 0:
        print("Es ist unentschieden!")
    elif type(result) == tuple:
        print("Spieler", result, "gewinnen!")
    else:
        print("Spieler", result, "gewinnt!")

# Aufruf der Funktion
play_game()
