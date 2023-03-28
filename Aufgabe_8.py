# Aufgabe 8


def round_to_05(number):
    return round(number * 20) / 20  # (Gerundete) Anzahl benötigter 5 Räppler berechnen und zurückgeben


x = float(input('Gib eine zu rundende Zahl mit Nachkommastellen ein: '))
print(f'Die auf 0.05 gerundete Zahl {x} ist {round_to_05(x)}')


