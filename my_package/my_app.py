# lista di spese giornaliere
spese = [12.50, 8.90, 15.00, 3.50, 20.00]

# calcolo totale
totale = sum(spese)

# calcolo media
media = totale / len(spese)

print("Spese registrate:", spese)
print("Totale spese:", totale, "€")
print("Spesa media:", round(media, 2), "€")
