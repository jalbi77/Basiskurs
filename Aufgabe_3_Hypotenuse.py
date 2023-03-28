# Aufgabe 3 Hypotenuse

# Modul math importieren.
import math

# Funktion hypotenuse
def hypotenuse(a, b):
    """
    Berechnet aus den beiden Katheten a und b die Hypotenuse c.
    """
    # Hypotenuse berechnen.
    c = math.sqrt(a**2 + b**2) 

    # Berechnete Hypotenuse zurückgeben.
    return c


# Berechnung Hypotenuse für a = 3, b = 4.
c = hypotenuse(3, 4)

# Berechnete Hypotenuse ausgeben.
print(c)

# Weitere Möglichkeiten der Verwendung der Funktion mit Benennung der Argumente: 
# c = hypotenuse(a = 3, b = 4)
# c = hypotenuse(b = 4, a = 3)
