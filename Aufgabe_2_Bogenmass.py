
# Aufgabe 2 Bogenmass

# Modul math importieren.
import math

# Funktion bogenmass.
def bogenmass(winkel_gradmass):
    """
    Rechnet einen Winkel vom Gradmass um ins Bogenmass.
    """
    # Winkel umrechnen vom Gradmass ins Bogenmass.
    winkel_bogenmass = (2 * math.pi * winkel_gradmass) / 360

    # Berechneter Winkel im Bogenmass zurückgeben.
    return winkel_bogenmass


# Winkel eingeben.
winkel_grad = float(input('Geben Sie einen Winkel (Gradmass) ein: '))

# Winkel im Bogenmass ausgeben.
print(f'{winkel_grad} Grad sind im Bogenmass: {bogenmass(winkel_grad):.4f}')

# Sinus vom Winkel berechnen und ausgeben.
print(f'Der Sinus von {winkel_grad} Grad ist {math.sin(bogenmass(winkel_grad)):.3f}')
