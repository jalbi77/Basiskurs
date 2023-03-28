# # Aufgabe 22: Ausladung s berechnen
#
# # Funktion Ausladung
# def ausladung(anzahl, laenge):
#     """ Ausladung... """
#
#     # Ausladung s initialisieren
#     s = 0
#
#     # Schleife für die angegebene Anzahl Planken
#     for i in range(2, anzahl * 2 + 1, 2):
#
#         # Zur Gesamt-Ausladung die mögliche Ausladung dazuzählen
#         s = s + laenge/i
#
#     # Ausladung zurückgeben
#     return s
#
# # Hauptprogramm
# # Eingabe
# anzahl = int(input('Anzahl der Planken: '))
# laenge = float(input('Länge einer Planke: '))
#
# # Verarbeitung
# print(f'Mit {anzahl} Planken der Länge {laenge} m erzielen wir \
# eine Ausladung von {ausladung(anzahl, laenge):.3f} m')

# *********************************************************************************

# # Aufgabe 25: Binomialkoeffizient, auf wieviele verschiedene Arten man k Objekte aus einer Menge von
# # verschiedenen Objekte auswählen kann (z.B. CH-Zahlenlotto, 6 aus 45)
#
# # Funktion Bin..
# def binomialkoeffizient(n, k):
#     """ Binomialkoeffizient """
#
#     # Binomialkoeffizienten b initialisieren
#     b = 1 # Wenn 0, wird immer 0*irgendwas berechnet
#
#     # Schleifen für die k Faktoren
#     for i in range(1, k + 1):
#
#         # Aktuellen Fakti dazu multiplizieren
#         b = b * ((n - (i - 1)) / i)
#
#     return int(b)
#
# # Hauptprogramm
# print(f'6 aus 45: {binomialkoeffizient(45, 6)} Möglichkeiten beim CH-Lotto')
# print(f'6 aus 49: {binomialkoeffizient(49, 6)} Möglichkeiten beim D-Lotto')
# print(f'1 aus 6: {binomialkoeffizient(6, 1)} Möglichkeiten beim Würfeln')

# *********************************************************************************

# # Aufgabe 29 Würfelspiel "Eins"
# # Implementieren Sie ein weiteres Würfelspiel, bei dem Sie solange würfeln und die Augenzahlen zusammenzählen, bis Sie eine 1
# # gewürfelt haben. Geben Sie neben der Gesamtaugenzahl auch die Anzahl Würfe zurück, die Sie machen konnten, bis Sie die 1 gewürfelt haben.
# # Zur Erinnerung: Würfeln können Sie mit random.randint(1, 6) Erstellen Sie auch eine Variante des Spiels, bei der die 1 beim letzten
# # Wurf ebenfalls zur Gesamtaugenzahl und zur Anzahl Würfe addiert wird!
#
# import random
#
# # Initialisieren
# summe = 0
# anzahl = 0
#
# # Ein erstes Mal würfeln!
# wuerfel = random.randint(1, 6)
#
# # Weiterwürfeln solange keine 1 gewürfelt wurde
# while wuerfel != 1:
#
#     # Es wurde keine 1 gewürfelt!
#     # Gesamtaugenzahl erhöhen
#     summe = summe + wuerfel
#
#     # Anzahl Würfe erhöhen
#     anzahl += 1  # anzahl = anzahl + 1
#
#     # Ein weiteres Mal würfeln!
#     wuerfel = random.randint(1, 6)
#
# # Ausgabe ohne die 1 und letzter Wurf
# print('Anzahl Würfe: ', anzahl, ' Summe der Augen: ', summe)
#
# # Ausgabe inkl. die 1 und letzter Wurf
# print('Anzahl Würfe: ', anzahl + 1, ' Summe der Augen: ', summe + 1)

# *********************************************************************************

# # Aufgabe 30 Collatz-Folge
# # 1 Wähle eine natürliche Startzahl n
# # 2 Wenn n = 1 ist, dann stoppe
# # 3 Wenn n eine gerade Zahl ist, ersetze n durch n/2 und gehe zu 2
# # 4 Wenn n eine ungerade Zahl ist, ersetze n durch 3 ⋅ n + 1 /2 und gehe zu 2
# # Alle so erzeugten Zahlenfolgen werden immer bei 1 enden.
# # Das ist allerdings noch nicht bewiesen, die Collatz-Vermutung gehört noch
# # immer zu den ungelösten Problemen der Mathematik.
#
# # Anzahl durchgänge
# anzahl = 0
#
# zahl = int(input('Zahl: '))
# print(zahl)
#
# # 1 noch nicht erreicht? Nächste Zahl berechnen bis die 1 erreicht ist
# while zahl != 1:
#
#     # Zahl prüfen ob sie gerade ist
#     if zahl % 2 == 0:
#         # Gerade Zahl
#         zahl = zahl / 2
#
#     else:
#         # Ungerade Zahl
#         zahl = (3 * zahl + 1) / 2
#
#     # Zahl ausgeben
#     print(int(zahl))
#
#     # Anzahl erhöhen
#     anzahl = anzahl + 1
#
# print('Anzahl Durchläufe: ', anzahl)

# *********************************************************************************

# Aufgabe 33 Tetraederzahlen
# Entwickeln Sie eine Funktion, die in Abhängigkeit einer Zahl n die ersten n Tetraederzahlen ausgibt.
# Tetraederzahlen beziffern die Anzahlen von Kugeln, die benötigt werden, um ein Tetraeder Schicht für Schicht
# zu bilden. Die nebenstehende Abbildung illustriert die vierte Tetraederzahl, wo das Tetraeder aus vier Schichten
# besteht und total 20 Kugeln benötigt werden.

# Anzahl Schichten
n = int(input('n: '))

# Tetraederzahl initialisieren
t = 1
print(t)

# Schleife von 2 bis n, um die nächsten Tetraederzahlen zu berechnen
for i in range(2, n + 1):

    # Nächste T.zahl berechnen
    # Zur bisherigen T.zahl wird ein Summand addiert

    # Aktuellen Summanden initialisieren
    s = 0

    # Innere Schleife um den aktuellen Summanden zu berechnen
    for j in range(1, i + 1):

        # Aktuellen Summanden berechnen
        s = s + j

    # Zur bisherigen T.zahl wird der Summand addiert
    t = t + s

    print(t)
