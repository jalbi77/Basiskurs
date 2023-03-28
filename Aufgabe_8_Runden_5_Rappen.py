# Aufgabe 8 Runden auf 5 Rappen

# Modul math importieren.
import math

# Funktion gerundeter_betrag.
def gerundeter_betrag(betrag):
    """
    Rundet einen Betrag auf 5 Rappen (oder Cent).
    """
    # (Gerundete) Anzahl benötigter 5 Räppler berechnen.
    anzahl_5_raeppler = round(betrag * 20)

    # Gerundeter Betrag zurückgeben.
    return anzahl_5_raeppler/20


# Betrag eingeben.
betrag = float(input('Geben Sie einen Betrag ein: '))

# Resultat ausgeben.
print(f'Der Betrag {betrag} wird auf den Betrag {gerundeter_betrag(betrag):.2f} gerundet.')
