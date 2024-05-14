# Lag en metode i trenerklassen som tar inn en pokemon og fjerner pokemon-en fra pokemon-lista.

class Trener:
    def __init__(self, navn):
        self.navn = navn
        self.pokemon_liste = []

    def legg_til_pokemon(self, pokemon):
        self.pokemon_liste.append(pokemon)

    def fjern_pokemon(self, pokemon):
        if pokemon in self.pokemon_liste:
            self.pokemon_liste.remove(pokemon)
            print(f"{pokemon} er fjernet fra {self.navn}s pokemon-liste.")
        else:
            print(f"{pokemon} er ikke i {self.navn}s pokemon-liste.")

    def __str__(self):
        return f"{self.navn} ({len(self.pokemon_liste)} Pokemon)"

# Eksempel på bruk
ash = Trener("Ash Ketchum")
pikachu = Pokemon("Pikachu")
charmander = Pokemon("Charmander")
ash.legg_til_pokemon(pikachu)
ash.legg_til_pokemon(charmander)
print(ash.pokemon_liste)  # Output: [Pikachu, Charmander]
ash.fjern_pokemon(charmander)
print(ash.pokemon_liste)  # Output: [Pikachu]
