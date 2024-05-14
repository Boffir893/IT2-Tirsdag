# Lag en metode i trenerklassen som legger til en pokemon i pokemon-lista til en trener.

class Trener:
    def __init__(self, navn):
        self.navn = navn
        self.pokemon_liste = []

    def legg_til_pokemon(self, pokemon):
        self.pokemon_liste.append(pokemon)

    def __str__(self):
        return f"{self.navn} ({len(self.pokemon_liste)} Pokemon)"

# Eksempel på bruk
ash = Trener("Ash Ketchum")
pikachu = Pokemon("Pikachu")
ash.legg_til_pokemon(pikachu)
print(ash.pokemon_liste)  # Output: [Pikachu]
