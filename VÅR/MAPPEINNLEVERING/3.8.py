# En trener skal ha egenskapene navn, som er en streng, og en pokemonliste som er en med pokemon. Treneren skal også ha en metode for å legge til pokemon i pokemonlisten, og en metode for å fjerne pokemon.

# Legg til en trener-klasse i UML-diagrammet ditt.
# Lag Python-kode for trener-klassen.
# Lag en str-metode som returnerer navnet på treneren og antall pokemon treneren har.

''' 
-----------------------------------
|              Pokemon             |
-----------------------------------
| - navn: str                      |
| - type: list[str]                |
| - base: dict[str, int]           |
-----------------------------------
| + __init__(navn: str, type: list[str], base: dict[str, int]) |
| + __str__(): str                 |
-----------------------------------

-----------------------------------
|              Trener              |
-----------------------------------
| - navn: str                      |
| - pokemonliste: list[Pokemon]    |
-----------------------------------
| + __init__(navn: str)            |
| + __str__(): str                 |
| + legg_til_pokemon(pokemon: Pokemon) |
| + fjern_pokemon(pokemon: Pokemon) |
-----------------------------------
'''

class Trener:
    def __init__(self, navn):
        self.navn = navn
        self.pokemonliste = []

    def __str__(self):
        return f"Trener: {self.navn}, Antall Pokemon: {len(self.pokemonliste)}"

    def legg_til_pokemon(self, pokemon):
        self.pokemonliste.append(pokemon)

    def fjern_pokemon(self, pokemon):
        if pokemon in self.pokemonliste:
            self.pokemonliste.remove(pokemon)
            print(f"{pokemon.navn} er fjernet fra {self.navn}s pokemonliste.")
        else:
            print(f"{pokemon.navn} finnes ikke i {self.navn}s pokemonliste.")

# Eksempel på bruk
trener1 = Trener("Ash")
print(trener1)

# Legg til noen Pokémon
pokemon1 = Pokemon("Pikachu", ["Electric"], {"HP": 35, "Attack": 55, "Defense": 40})
pokemon2 = Pokemon("Charmander", ["Fire"], {"HP": 39, "Attack": 52, "Defense": 43})
trener1.legg_til_pokemon(pokemon1)
trener1.legg_til_pokemon(pokemon2)
print(trener1)

# Fjern en Pokémon
trener1.fjern_pokemon(pokemon1)
print(trener1)
