# Implementer menyvalget 3. Legg til trener. Hvis brukeren velger dette valget skal brukeren få spørsmål om navn, også skal 
# programmet opprette en ny trener med dette navnet og en tom liste med pokemon.

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

# Implementasjon av menyvalg 3
def legg_til_trener():
    navn = input("Skriv inn navnet på treneren: ")
    ny_trener = Trener(navn)
    trenere.append(ny_trener)
    print(f"{ny_trener.navn} er lagt til som en ny trener med en tom liste med Pokémon.")

# Eksempel på bruk
trenere = []

# Legge til trener
legg_til_trener()


