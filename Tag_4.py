# # Schreiben Sie eine Prozedur, die einen String als Argument übernimmt,
# # und die Zeichen "rückwärts" ausgibt, eines pro Zeile.
#
# def wort_rückwärts_ausgeben(wort):
#     """ Gibt ein Wort rückwärts aus."""
#     # Länge des Wortes
#     laenge = len(wort)
#     # Index initialisieren
#     index = -1
#
#     # while-Schleife, um das Wort rückwärts zu durchlaufen
#     while index >= -laenge:
#         # Zeichen ausgeben
#         print(wort[index])
#         # Nächster Index
#         index = index - 1
#
# wort = str(input('Geben Sie ein Wort ein: '))
# wort_rückwärts_ausgeben(wort)
#
# # ***************************************************
#
# # Beispiel Entchen
# # In Robert McCloskeys Buch "Make Way for Ducklings" gibt's Entchen
# # mit den Namen Jack, Kack, Lack, Mack, Nack, Ouack, Pack und Quack.
# # Schreiben Sie ein kleines Programm, das die Namen der Entchen
# # ausgibt. (Natürlich mit einer for-Schleife!)
#
# # Erste Buchstaben
# erste_buchstaben = 'JKLMNOPQ'
#
# # anhang
# anhang = 'ack'
#
# # Schleife
# for zeichen in erste_buchstaben:
#     # Zeichen prüfen
#     if zeichen == 'O' or zeichen == 'Q':
#         # Namen ausgeben
#         print(zeichen + 'u' + anhang)
#     else:
#         # Namen ausgeben
#         print(zeichen + anhang)
#
# # ***************************************************
#
# # Aufgabe 37 Anzahl Zeichen
# # Schreiben Sie eine Funktion anzahl(wort, zeichen), die zurückgibt,
# # wie oft das Zeichen im Wort vorkommt.
#
# def anzahl(wort, zeichen):
#     """ Gibt zurück, wie oft Zeichen im Wort vorkommen"""
#     # Anzahl initialisieren
#     anzahl = 0
#
#     # Schleife durch das Wort
#     for aktuelles_zeichen in wort:
#         # aktuelles_zeichen prüfen
#         if aktuelles_zeichen == zeichen:
#             # Zeichen gefunden, Anzahl erhöhen
#             anzahl += 1
#     # anzahl zurückgeben
#     return anzahl
#
# wort = input('Wort: ')
# zeichen = input('Zeichen: ')
#
# print(anzahl(wort, zeichen=zeichen))
#
# # ***************************************************

# Aufgabe 38 Zeichen in beiden Strings
# Schreiben Sie eine (sehr einfache) Funktion, die für zwei Wörter alle
# Zeichen ausgibt, die in beiden Wörtern vorkommen.
#
# def in_beiden_ausgeben(wort1, wort2):
#     # Schleife durch das erste Wort
#     for zeichen in wort1:
#
#         # Prüfen, ob zeichen (vom ersten Wort) im zweiten wort vorkommt.
#         if zeichen in wort2:
#             print(zeichen)
#
# wort1 = input('Wort 1: ')
# wort2 = input('Wort 2: ')
#
# in_beiden_ausgeben(wort1, wort2)

# # ***************************************************

# # Aufgabe 42 Sternzahlen
# # Entwickeln Sie eine Funktion sternzahlen(n), welche eine Liste mit
# # den ersten n Zahlen der Folge der Zahlen des Vierecksterns berechnet.
# # Bei den Vierecksternen wird aus einem Quadrat und vier Dreiecken ein
# # vierzackiger Stern gebildet. Die Zahlenfolge gibt an, wie viele Kreise
# # benötigt werden, um den Stern zu bilden.
#
# def sternzahlen(n):
#
#     # Sternzahl initialisieren
#     sternzahl = 1
#     # Liste mit sternzahlen initialisieren
#     sternzahlen = [sternzahl]
#
#     # Schleife für die Berechnung der nächsten Sternzahlen
#     for i in range(2, n+1):
#         # Sternzahl berechnen
#         sternzahl = sternzahl + (i - 1) * 6 + 1
#
#         # Berechnete Sternzahl der Liste anhängen
#         sternzahlen.append(sternzahl)
#
#     # Sternzahlen zurückgeben
#     return sternzahlen
#
# print('Sternzahlen: ', sternzahlen(10))

# # ***************************************************

# Aufgabe 43 Lottozahlen
# Entwickeln Sie eine Funktion, die Ihnen die Lottozahlen ausrechnet!
# Und zwar eine allgemeine Funktion, bei der Sie angeben können,
# wie viele Gewinnzahlen aus wie vielen Zahlen zu wählen sind!
# (CH: 6 aus 45, D: 6 aus 49, A: 6 aus 45)
# Eine bereits gezogene Zahl darf nicht erneut gezogen werden!

import random


def lottozahlen(n, k):
    """ Gibt die Lottozahlen zurück, also k aus n """

    # Liste initialisieren
    lottozahlen = []

    # Schleife für Berechnung der k Lottozahlen
    for i in range(k):
        # Zahl ziehen
        zahl = random.randint(1, n)

        # Prüfen, ob diese Zahl bereits in der Liste vorhanden ist
        while zahl in lottozahlen:
            # Neue Zahl ziehen
            zahl = random.randint(1, n)

        # Zahl den Lottozahlen hinzufügen
        lottozahlen.append(zahl)

    # Sortieren
    lottozahlen.sort()

    return lottozahlen

print('Schweizer Lottozahlen', lottozahlen(45, 6))

