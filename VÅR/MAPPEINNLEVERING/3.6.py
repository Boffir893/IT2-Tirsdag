# Lag en tom liste i programmet ditt, og fyll listen med pokemon-objekter (objekter av klassen Pokemon),

# Opprett en tom liste for Pokémon-objekter
pokemon_liste = []

# Fyll listen med Pokémon-objekter
for pokemon_info in pokemon_data:
    pokemon_id = pokemon_info['id']
    name = pokemon_info['name']['english']
    pokemon_type = pokemon_info['type']
    base_stats = pokemon_info['base']

    # Opprett et Pokémon-objekt og legg det til i listen
    pokemon = Pokemon(pokemon_id, name, pokemon_type, base_stats)
    pokemon_liste.append(pokemon)
