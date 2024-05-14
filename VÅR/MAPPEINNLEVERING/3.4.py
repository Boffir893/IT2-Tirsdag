# Lag en Pokemon-klasse som følger UML-diagrammet fra forrige oppgave.

class Pokemon:
    def __init__(self, pokemon_id, name, pokemon_type, base_stats):
        self._id = pokemon_id
        self._name = name
        self._type = pokemon_type
        self._base = base_stats

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_types(self):
        return self._type

    def get_base_stats(self):
        return self._base

    def get_hp(self):
        return self._base.get('HP', 0)

    def get_attack(self):
        return self._base.get('Attack', 0)

    def get_defense(self):
        return self._base.get('Defense', 0)

    def get_special_attack(self):
        return self._base.get('Sp. Attack', 0)

    def get_special_defense(self):
        return self._base.get('Sp. Defense', 0)

    def get_speed(self):
        return self._base.get('Speed', 0)
