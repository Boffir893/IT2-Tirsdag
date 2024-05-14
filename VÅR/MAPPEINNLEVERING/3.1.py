#  3.1 - Hovedmeny
#  Lag en hovedmeny i terminalen med valgene:

#  1. Se pokemonoversikt
#  2. Se treneroversikt
#  3. Lag trener
#  4. Avslutt

import os
import platform
 
def rens_terminal():
    if platform.system == "Windows":
        os.system("cls")
    else:
        os.system("clear")
 
 
while True:
    rens_terminal()
    print("-- Pokemone go --")  
    print("1: Se Pokemoneoversikt ")
    print("2: Se treneroversikt")
    print("3: Lag trener")
    print("4: Avslutt")
    brukervalg = input(">")
 
    if brukervalg == "1":
        print("-- Se Pokemoneoversikt --")
        input("Trykk enter for å gå tilbake til hovedmenyen")
    elif brukervalg == "2":
        print("-- Se treneroversikt --")
        input("Trykk enter for å gå tilbake til hovedmenyen")
    elif brukervalg == "3":
        print("-- Lag trener --")
        input("Trykk enter for å gå tilbake til hovedmenyen")
    elif brukervalg == "4":
        print("Avslutter..")
        break # bryter ut av while-løkken
    else:
        print("Ugyldig valg")