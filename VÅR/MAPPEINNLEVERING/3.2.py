# Les inn filen i et python-program og lagre innholdet i en variabel.

import json

# Åpne og les filen pokemon.json med tegnsettet utf-8
with open('pokemon.json', 'r', encoding='utf-8') as file:
    pokemon_data = json.load(file)

# Nå er innholdet av filen lagret i variabelen pokemon_data
