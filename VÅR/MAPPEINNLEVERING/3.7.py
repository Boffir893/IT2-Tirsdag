# Implementer menyvalget 1. Se pokemonoversikt. Hvis brukeren velger dette valget skal en liste over alle pokemon-ene vises i terminalen.

def vis_pokemonoversikt(pokemon_liste):
    print("Pokémonoversikt:")
    for pokemon in pokemon_liste:
        print(pokemon)

# Anta at pokemon_liste allerede er opprettet og fylt med Pokémon-objekter

# Implementering av menyvalg
valg = input("Velg et alternativ:\n1. Se pokemonoversikt\n2. ... (andre alternativer)\nValg: ")

if valg == '1':
    vis_pokemonoversikt(pokemon_liste)
elif valg == '2':
    # Implementer andre alternativer her
    pass
else:
    print("Ugyldig valg")
