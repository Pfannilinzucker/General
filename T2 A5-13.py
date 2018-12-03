# OWIN-Tutoriumsaufgaben, Blatt 2, 19.11.18

# Aufgabe 5
a =  ["Python", "OWIN", "WiSe 15"]
print(a[0])
print(a[1])
print(a[2])

# Aufgabe 6
a =  ["Python", "OWIN", "WiSe 15"]
print("1 :", a[0])
print("2 :", a[1])
print("3 :", a[2])

# Aufgabe 6 (Alternative)
a =  ["Python", "OWIN", "WiSe 15"]
i = 1
for counter in a:
	print(1, ":", counter)
	i = i + 1
	
# Aufgabe 7
a =  ["Python", "OWIN", "WiSe 15"]
i = 1
for counter in a:
	ausgabe = str(i)+": "+str(counter)				# str(): wandelt in String um (Zeichen und Zahlenfolgen an sich unverknüpfbar)
	print(ausgabe)
	i = i + 1

# Aufgabe 8
Artikelliste = [1, 4, 10, 2, 7, 5]
Summe = 0
i = 0
while i <= 5:
	Summe = Summe + Artikelliste[i]
	i = i+1
print("Summe:", Summe, "EUR")

# Aufgabe 9
Artikelliste = [1, 4, 10, 2, 7, 5]
Artikelbezeichnung = ["Schrauben", "Kleber", "Säge", "Sägeblatt", "Schraubenzieher", "Zange"]
Summe = 0
i = 0
while i <= 5:
	Summe = Summe + Artikelliste[i]
	print(Artikelbezeichnung[i]+":", Artikelliste[i], "EUR")
	i = i+1
print("Summe:", Summe, "EUR")

# Aufgabe 10
Artikelliste = [1, 4, 10, 2, 7, 5]
Artikelbezeichnung = ["Schrauben", "Kleber", "Säge", "Sägeblatt", "Schraubenzieher", "Zange"]
Summe = 0
i = 0
while i <= 5:
	Summe = Summe + Artikelliste[i]
	print(Artikelbezeichnung[i]+":", Artikelliste[i], "EUR (Brutto)")
	print(Artikelbezeichnung[i]+":", round(Artikelliste[i]*1.19,2), "EUR (Netto)")
	i = i+1
print("Summe:", Summe, "EUR (Brutto)")
print("Summe:", round(Summe*1.19,2), "EUR (Netto)")

# Aufgabe 11
Artikelliste = [1, 4, 10, 2, 7, 5]
Artikelbezeichnung = ["Schrauben", "Kleber", "Säge", "Sägeblatt", "Schraubenzieher", "Zange"]
Echtpreis = [0, 0, 0, 0, 0, 0]
Summe = 0
i = 0
while i <= 5:
	Summe = Summe + Artikelliste[i]
	print(Artikelbezeichnung[i]+":", Artikelliste[i], "EUR (Brutto)")
	print(round(Artikelliste[i]*1.19,2), "EUR (Netto)")
	if round(Artikelliste[i]*1.19,2) > 2:
		Echtpreis[i] = round(Artikelliste[i]*1.19,2)
		print("Echtpreis:", Echtpreis[i], "EUR")
	else:
		Echtpreis[i] = 0
		print("Echtpreis: 0 EUR")
	i = i+1
i = 0
while i <= 5:
	Summe = Summe + Echtpreis[i]
	i = i + 1
print("Summe (netto):", Summe)

# Aufgabe 12
Artikelliste = [1, 4, 10, 2, 7, 5]
Artikelbezeichnung = ["Schrauben", "Kleber", "Säge", "Sägeblatt", "Schraubenzieher", "Zange"]
Echtpreis = [0, 0, 0, 0, 0, 0]
Summe = 0
i = 0
while i <= 5:
	Summe = Summe + Artikelliste[i]
	print(Artikelbezeichnung[i]+":", Artikelliste[i], "EUR (Brutto)")
	print(round(Artikelliste[i]*1.19,2), "EUR (Netto)")
	if round(Artikelliste[i]*1.19,2) > 2:
		Echtpreis[i] = round(Artikelliste[i]*1.19,2)
		print("Echtpreis:", Echtpreis[i], "EUR")
	else:
		Echtpreis[i] = 0
		print("Echtpreis: 0 EUR")
	i = i+1
	# Bestimmen, wie Preise ohne Echtpreis sind.
i = 0
while i <= 5:
	Summe = Summe + round(Artikelliste[i]*1.19,2)
	i = i + 1
if Summe < 30:
	print("Sie profitieren nicht von der Rabattaktion!")
	print("Summe:", Summe, "EUR")
else:
	print("Sie profitieren von der Rabattaktion!")
	i = 0
	Summe = 0
	while i <=5:
		Summe = Summe + Echtpreis[i]
		i = i + 1
	print("Summe:", Summe, "EUR")
	
# Aufgabe 13
	# Methodendefinition
def NettoGerundet(Parameter):
	return (round(Parameter*1.19,2))
	# Hauptprogramm
Artikelliste = [1, 4, 10, 2, 7, 5]
Artikelbezeichnung = ["Schrauben", "Kleber", "Säge", "Sägeblatt", "Schraubenzieher", "Zange"]
Echtpreis = [0, 0, 0, 0, 0, 0]
Summe = 0
i = 0
while i <= 5:
	Summe = Summe + Artikelliste[i]
	print(Artikelbezeichnung[i]+":", Artikelliste[i], "EUR (Brutto)")
	print(NettoGerundet(Artikelliste[i]), "EUR (Netto)")
	if round(Artikelliste[i]*1.19,2) > 2:
		Echtpreis[i] = NettoGerundet(Artikelliste[i])
		print("Echtpreis:", Echtpreis[i], "EUR")
	else:
		Echtpreis[i] = 0
		print("Echtpreis: 0 EUR")
	i = i+1
	# Bestimmen, wie Preise ohne Echtpreis sind.
i = 0
while i <= 5:
	Summe = Summe + NettoGerundet(Artikelliste[i])
	i = i + 1
if Summe < 30:
	print("Sie profitieren nicht von der Rabattaktion!")
	print("Summe:", Summe, "EUR")
else:
	print("Sie profitieren von der Rabattaktion!")
	i = 0
	Summe = 0
	while i <=5:
		Summe = Summe + Echtpreis[i]
		i = i + 1
	print("Summe:", Summe, "EUR")