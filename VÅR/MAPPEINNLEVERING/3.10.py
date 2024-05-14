# Implementer menyvalget 2. Se treneroversikt. Hvis brukeren velger dette valget skal en liste over alle trenerne vises i terminalen.

# Implementasjon av menyvalg 2
def vis_trenere():
    print("Oversikt over trenere:")
    for index, trener in enumerate(trenere, start=1):
        print(f"{index}. {trener}")

# Eksempel på bruk
vis_trenere()
