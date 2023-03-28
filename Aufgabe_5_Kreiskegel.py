# Aufgabe 5 Kreiskegel

# Modul math importieren.
import math

# Funktion kreiskegel
def kreiskegel(r, h):
    """
    Berechnet Volumen und Oberfläche eines geraden
    Kreiskegels mit Radius r und Höhe h.
    """
    # Volumen.
    volumen = 1/3 * math.pi * r**2 * h

    # Oberfläche.
    oberflaeche = math.pi * r**2 + math.pi * r * math.sqrt(r**2 + h**2)

    # Volumen und Oberfläche zurückgeben.
    return (volumen, oberflaeche)


# Radius eingeben.
radius = float(input('Geben Sie den Radius der Grundfläche eines Kreiskegels ein: '))

# Höhe eingeben.
hoehe = float(input('Geben Sie die Höhe des Kreiskegels ein: '))

# Volumen und Oberfläche des Kreiskegels berechnen.
volumen_oberflaeche = kreiskegel(radius, hoehe)

# Berechnete Grössen ausgeben.
print(f'Kreiskegel mit Radius {radius} und Höhe {hoehe}')
print(f'Volumen:    {volumen_oberflaeche[0]:8.2f}')
print(f'Oberfläche: {round(volumen_oberflaeche[1], 2):8}')
