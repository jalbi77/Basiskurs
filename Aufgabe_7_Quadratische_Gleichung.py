# Aufgabe 7 Quadratische Gleichung

# Modul math importieren.
import math

# Funktion loesung_quadratische_gleichung
def loesung_quadratische_gleichung(a, b, c):
    """ 
    Berechnet die beiden Lösungen einer quadratischen Gleichung
    a*x^2 + b*x + c = 0
    a, b, c: Koeffizienten
    x1, x2: Lösungen der quadratischen Gleichung
    (Ohne Berücksichtigung einer negativen Diskriminante)
    """

    # Diskriminante berechnen.
    d = b**2 - 4*a*c

    # Lösung x1 berechnen.
    x1 = (-b + math.sqrt(d))/(2*a)

    # Lösung x2 berechnen.
    x2 = (-b - math.sqrt(d))/(2*a)

    # Berechnete Lösungen zurückgeben.
    return (x1, x2)


# Lösungen der quadratischen Gleichung -2x^2 -4x + 6 = 0 berechnen.
x = loesung_quadratische_gleichung(a = -2, b = -4, c = 6)

# Berechnete Lösungen ausgeben.
print(f'Die beiden Lösungen der quadratischen Gleichung -2x^2 - 4x = -6 sind {x[0]:.5f} und {x[1]:.5f}')


# Ebenfalls möglich ist folgende Syntax:

# Lösungen der quadratischen Gleichung -2x^2 -4x + 6 = 0 berechnen.
(x1, x2) = loesung_quadratische_gleichung(a = -2, b = -4, c = 6)

# Berechnete Lösungen ausgeben.
print(f'Die beiden Lösungen der quadratischen Gleichung -2x^2 - 4x = -6 sind {x1:.5f} und {x2:.5f}')



# Lösungen der quadratischen Gleichung x^2 + 2x + 3 = 0 berechnen.
x = loesung_quadratische_gleichung(a = 1, b = 2, c = 3)

# Der Fehler "ValueError: math domain error" wird angezeigt, weil die Wurzel einer 
# negativen Diskriminante nicht berechnet werden kann!
# Am zweiten Kurstag wird dieser Fall berücksichtigt werden können!


