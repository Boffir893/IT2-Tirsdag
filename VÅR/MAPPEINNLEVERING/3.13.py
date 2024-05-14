# Kopier koden under inn i en .py- eller en .ipynb-fil, og legg til en kommentar på hver linje som forklarer hva linjene gjør.

while True:
    try:
        alder = int(input("Hvor gammel er du? "))  # Spør brukeren om alder og konverterer input til heltall
        break  # Bryter ut av løkken hvis inputen er gyldig
    except:
        print("Ugyldig input. Alder må være et tall.")  # Hvis inputen ikke er gyldig, skriv ut feilmelding

år = 2024  # Setter variabelen år til 2024
fødselsår = år - alder  # Beregner fødselsåret ved å trekke alderen fra 2024
print(f"Du er født i {fødselsår}")  # Skriver ut fødselsåret til brukeren
