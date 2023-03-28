# Aufgabe 9 Geldautomat

# Betrag eingeben.
betrag = float(input('Geben Sie einen auszuzahlenden Betrag ein: '))

# Gewünschter Betrag ausgeben.
print("Gewünschter Betrag ", betrag)

# Auszuzahlenden Restbetrag berechnen.
# In dieser Variable wird laufend der noch auszuzahlende Restbetrag gespeichert.
# Hier, bei der Initialisierung, wird der maximal auszahlbare Betrag gespeichert.
restbetrag = (betrag // 10) * 10

# Ausbezahlter Betrag ausgeben.
print("Ausbezahlter Betrag", int(restbetrag))


# Anzahl 200er-Noten berechnen und ausgeben.
print("200er-Noten:", int(restbetrag // 200))

# Aktuellen Restbetrag berechnen.
restbetrag = restbetrag % 200


# Anzahl 100er-Noten berechnen und ausgeben.
print("100er-Noten:", int(restbetrag // 100))

# Aktuellen Restbetrag berechnen.
restbetrag = restbetrag % 100


# Anzahl 50er-Noten berechnen und ausgeben.
print(" 50er-Noten:", int(restbetrag // 50))

# Aktuellen Restbetrag berechnen.
restbetrag = restbetrag % 50


# Anzahl 20er-Noten berechnen und ausgeben.
print(" 20er-Noten:", int(restbetrag // 20))

# Aktuellen Restbetrag berechnen.
restbetrag = restbetrag % 20


# Anzahl 10er-Noten berechnen und ausgeben.
print(" 10er-Noten:", int(restbetrag // 10))
