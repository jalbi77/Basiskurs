# Aufgabe 4 Tetraeder

# Modul math importieren.
import math

# Funktion tetraeder
def tetraeder(a):
    """
    Berechnet Inkugelradius, Umkugelradius und Pyramidenhöhe eines
    regelmässigen Tetraeders mit Kantenlänge a.
    """
    # Inkugelradius.
    inkugelradius = a/12 * math.sqrt(6)

    # Umkugelradius.
    umkugelradius = 3 * inkugelradius

    # Pyramidenhöhe.
    pyramidenhoehe = inkugelradius + umkugelradius

    # Berechnete Grössen zurückgeben.
    return (inkugelradius, umkugelradius, pyramidenhoehe)


# Kantenlänge eingeben.
kantenlaenge = float(input('Geben Sie die Kantenlänge eines Tetraeders ein: '))

# Inkugelradius rho, Umkugelradius R, Pyramidenhöhe k berechnen.
(rho, R, k) = tetraeder(kantenlaenge)

# Berechnete Grössen ausgeben.
print(f'Tetraeder mit Kantenlänge {kantenlaenge}')
print(f'Inkugelradius: {rho:8.2f}')
print(f'Umkugelradius: {R:8.2f}')
print(f'Pyramidenhöhe: {k:8.2f}')
