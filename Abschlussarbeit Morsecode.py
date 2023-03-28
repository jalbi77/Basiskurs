# Aufgabe: Schreiben Sie ein Programm, das einen beliebigen Text als Morsecode ausgibt. Und natürlich soll Ihr
# Programm auch einen Morsecode «empfangen» können und die gemorste Nachricht wiedergeben.

# *****************************************************************************************************

# Dieses Programm definiert zwei Funktionen, "text_to_morse" und "morse_to_text", die es ermöglichen,
# einen eingegebenen beliebigen Text in Morsecode umzuwandeln und umgekehrt.
#
# Die Morse-Codierung ist in einem Dictionary namens "MORSE_CODE" definiert, das die Zuordnung von Buchstaben,
# Zahlen und Satzzeichen zu ihren entsprechenden Morse-Code-Darstellungen enthält.
#
# Die "text_to_morse" Funktion iteriert über jeden Buchstaben des eingegebenen Textes und überprüft,
# ob er im MORSE_CODE-Dictionary vorhanden ist. Wenn dies der Fall ist, fügt die Funktion den entsprechenden
# Morsecode hinzu, sonst wird der Buchstabe selbst beibehalten.
#
# Die "morse_to_text" Funktion verwendet die Trennung von Wörtern durch ' ' (zwei aufeinanderfolgende Leerzeichen)
# und die Trennung von Buchstaben durch ein einzelnes Leerzeichen. Sie iteriert über jedes Wort im Morsecode-Text,
# zerlegt es in seine Buchstaben und überprüft, ob der Buchstaben-Morsecode im MORSE_CODE-Dictionary vorhanden ist.
# Wenn dies der Fall ist, fügt die Funktion den entsprechenden Buchstaben hinzu, sonst wird der Morsecode beibehalten.
#
# Der Code verwendet dann eine Eingabeaufforderung, um einen Text oder Morsecode vom Benutzer zu erhalten,
# wandelt ihn mit der entsprechenden Funktion um und gibt das Ergebnis aus. Umlaute müssen umgeschrieben werden.

# *****************************************************************************************************

# Definition des Morse-Codes in einem dict
MORSE_CODE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..',
              '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.'}

def text_to_morse(text):
    morse_code = ''
    # iteriere über jeden Buchstaben des eingegebenen Textes
    for char in text:
        # prüfe ob (Gross-)Buchstabe im MORSE_CODE-Dictionary vorhanden ist
        if char.upper() in MORSE_CODE:
            # Wenn ja, füge den entsprechenden Morsecode hinzu
            morse_code += MORSE_CODE[char.upper()] + ' '
        else:
            # ansonsten Buchstabe beibehalten (z.B. Umlaute, Sonderzeichen)
            morse_code += char
    return morse_code

def morse_to_text(morse_code):
    text = ''
    # Trennung von Wörtern
    words = morse_code.split('  ')
    # iteriere über jedes Wort im Morsecode-Text
    for word in words:
        # Trennung von Buchstaben
        chars = word.split(' ')
        # iteriere über jeden Buchstaben
        for char in chars:
            # prüfe ob MORSE_CODE im Dictionary vorhanden ist
            if char in MORSE_CODE.values():
                # Wenn ja, füge den entsprechenden Buchstaben dem text hinzu: Erhalte Liste aller Schlüssel (Buchstaben)
                # im Dictionary, erhalte Liste aller Werte (Morsecode (=char)) und finde Index des Morsecode-Charakters.
                # Der gefundene Index wird dann verwendet, um das entsprechende Buchstaben-Äquivalent aus der Liste
                # der Schlüssel zu erhalten.
                text += list(MORSE_CODE.keys())[list(MORSE_CODE.values()).index(char)]
            else:
                # ansonsten Morsecode beibehalten
                text += char
        # Leerzeichen nach jeder Iteration einfügen
        text += ' '
    # Rückgabe durch entfernen führender und nachfolgender Leerzeichen
    return text.strip()

# Eingabeaufforderung: Text in Morsecode umwandeln
text = str(input('Geben Sie einen Textein, der zum Morsecode umgewandelt werden soll: '))
# Funktionsaufruf mit eingegebenen Text als Argument
morse_code = text_to_morse(text)
print(morse_code)

# Eingabeaufforderung: Morsecode in Text umwandeln
morse_code = str(input('Geben Sie einen Morsecode ein, der in lesbaren Text umgewandelt werden soll: '))
# Funktionsaufruf mit eingegebenen Morsecode als Argument
text = morse_to_text(morse_code)
print(text)
