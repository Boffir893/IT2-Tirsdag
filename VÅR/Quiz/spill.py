import os
import platform
 
def rens_terminal():
    if platform.system == "Windows":
        os.system("cls")
    else:
        os.system("clear")
 
 
while True:
    rens_terminal()
    print("-- Hvilket tall er partall? --")  
    print("A: 5")
    print("B: 2")
    print("C: 3")
    print("D: 7")
    brukervalg = input("SVAR:")
 
    if brukervalg == "A":
        print("Feil")
        input("Trykk enter for å gå tilbake ")
    elif brukervalg == "B":
        print("Korrekt")
        input("Trykk enter for å gå tilbake ")
    elif brukervalg == "C":
        print("Feil")
        input("Trykk enter for å gå tilbake ")
    elif brukervalg == "D":
        print("Feil")
        input("Trykk enter for å gå tilbake ")
    else:
        print("Ugyldig valg")
        break