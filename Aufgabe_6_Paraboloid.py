# Aufgabe 6 Paraboloid

# Modul math importieren.
import math

# Funktion paraboloid
def paraboloid(r, h):
    """
    Berechnet Volumen und Mantelfläche eines 
    Paraboloiden mit Radius r und Höhe h.
    """
    # Volumen.
    volumen = math.pi/2 * r**2 * h

    # Mantelfläche.
    mantelflaeche = (math.pi * r)/(6 * h**2) * (math.sqrt((r**2 + 4 * h**2)**3) - r**3)

    # Volumen und Mantelfläche zurückgeben.
    return (volumen, mantelflaeche)


# Radius eingeben.
radius = float(input('Geben Sie den Radius eines Paraboloiden ein: '))

# Höhe eingeben.
hoehe = float(input('Geben Sie die Höhe des Paraboloiden ein: '))

# Volumen und Mantelfläche des Paraboloiden berechnen.
(volumen, mantelflaeche) = paraboloid(radius, hoehe)

# Berechnete Grössen ausgeben.
print(f'Paraboloid mit Radius {radius} und Höhe {hoehe}')
print(f'Volumen:      {volumen:8.2f}')
print(f'Mantelfläche: {round(mantelflaeche, 2):8}')
