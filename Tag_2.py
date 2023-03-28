# # Programm zur Berechnung des BMI
#
# def bmi(m, l):
#     """Berechnet den BMI"""
#     return m / l**2
#
#
# m = float(input('Geben Sie Ihr Gewicht in [kg] ein: '))
# l = float(input('Geben Sie Ihre Körpergrösse in [m] ein: '))
#
# if bmi(m, l) < 18.5:
#     print(f'Ihr BMI beträgt {bmi(m, l):.1f}, Sie gelten als Untergewichtig')
# elif bmi(m, l) > 25:
#     print(f'Ihr BMI beträgt {bmi(m, l):.1f}, Sie gelten als Übergewichtig')
# elif 18.5 < bmi(m, l) < 25:
#     print(f'Ihr BMI beträgt {bmi(m, l):.1f}, Sie gelten als Normalgewichtig')

# ************************************************************

# # Quadratische Gleichung
#
# import math
#
# # loesung
# def loesung(a, b, c):
#     """ Lösungen der quadratischen Gleichung """
#     # Diskriminante berechnen
#     d = b**2 - 4*a*c
#
#     # Erste Lösung berechnen
#     x1 = (-b + math.sqrt(d)) / (2*a)
#
#     # Zweite Lösung berechnen
#     x2 = (-b - math.sqrt(d)) / (2*a)
#
#     # Lösungen zurückgeben
#     return (x1, x2)
#
#
# # Hauptprogramm
#
#
# # Gleichung -2x^2 - 4x + 6 = 0
#
#
# # Verarbeitung
# lsg = loesung(-2, -4, 6)
#
# print('Lösung x1:', lsg[0], ', Lösung x2:', lsg[1])

# ************************************************************

# Würfelspiel

def wuerfelspiel ():
    """
    Würfelspiel, bei dem mit zwei Würfeln gewürfelt wir und je nach Gegebenheit das Ergebnis angepasst wird
    Zwei gleiche augenzahlen --> Verdoppeln; Ein Würfel zeigt eine 1 --> 10 addieren, Geamtaugenzahl 11 --> Resultat = 1
    """
    # Modul random importieren
    import random

    # Zweimal würfeln
    w1 = random.randint(1, 6)
    w2 = random.randint(1, 6)

    # Prüfen
    if w1 == w2:
        # Zwei gleiche augenzahlen --> Verdoppeln
        ergebnis = (w1 + w2) * 2

    elif w1 == 1 or w2 == 1:
        # Ein Würfel zeigt eine 1 --> 10 addieren
        ergebnis = (w1 + w2) + 10

    elif w1 + w2 == 11:
        # Gesamtaugenzahl 11 --> Resultat = 1
        ergebnis = 1

    else:
        # Summe ausgeben
        ergebnis = w1 + w2

    print(f'Würfel eins zeigt {w1}, und Würfel zwei zeigt {w2}, Dein Ergebnis ist: {ergebnis}')

# Funktionsaufruf
wuerfelspiel()
