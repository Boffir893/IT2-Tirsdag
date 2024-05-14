# Lag en str-metode som returnerer navnet på en pokemon og minst en annen egenskap (eks: HP).

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

    def __str__(self):
        return f"{self._name} - HP: {self.get_hp()}"
