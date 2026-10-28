# Test Plan

## parse_time(time_text)
Eingabeformat:
- 2 Numerische Teile von 1 oder 2 Ziffern, ein Doppelpunkt dazwischen
- Führende Nullen sind erlaubt
- 0 <= Stunden <= 23, 0 <= Minuten <= 59
- ValueError bei falschem Wert

Speziell:
- Eine Stelle nur "0" (-> wird erkannt)
- Drei Ziffern, die erste eine 0?
- Einmal komplett leer


## parse_measurement(line)

- line: String, 3 geteilt durch ;, Leerzeichen am Anfang und Ende entfernen
-> ValueError
- Stadtname nicht leer, Uhrzeit mit parse_time, Temperatur mit parse Float
-> ValueEror

Speziell:
- negative Temperaturen
- Temperaturen ohne Nachkommazahl/mit , als Trennzeichen


## filter_by_temperature(measurements, lower, upper)

- Grenzen Testen
- Bestehende Reihenfolgen, Liste wird nicht verändert
- Doppelte
- lower > upper -> ValueError
- Egebnis ist auch eine Liste

speziell:
- Leere Liste?
- Kein Ergebnis?
- Lower und Upper gleich?


## average_temperature(measurements, city)

- Städtenamen: Verlgeich, Case Sensitive
- Mittelwert
- keine Messungen -> ValueError
- Eingabedaten nicht verändert

Speziell:
- Leerzeichen in Stadtnamen
- Kein Treffer
- 1 Treffer
- Falsche Eingabe


## hottest_measurement(measurements)

- Rückgabe: Höchste/Früheste/Erste
- Leer -> ValueError
- Eingabedaten nicht verändern





