# Et program som fortsetter helt til brukeren har skrevet riktig input

år = 2024

while True:
    try:
        alder = int(input("Hvor gammel blir du i år?"))
        break
    except: 
        print("Ugyldig input. input må være et tall")