# Aufgabe 9: Geldauszahlungsautomat

# Notenwerte
notes = [200, 100, 50, 20, 10]

# Eingabe des gewünschten Betrags
desired_amount = float(input("Gewünschter Betrag: "))

# Ausbezahlter Betrag (gerundet auf die nächste 10er-Note)
paid_amount = round(desired_amount, -1)

# Anzeige des ausbezahlten Betrags
print("Ausbezahlter Betrag:", paid_amount)

# Berechnung der Anzahl der Noten
for note in notes:
    count = paid_amount // note
    paid_amount = paid_amount % note
    print(str(note) + "er-Noten:", count)
    print(paid_amount)
