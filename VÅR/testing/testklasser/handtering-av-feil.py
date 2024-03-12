# et program som finner fødselår basert på alder

år = 2024 # Oppretter en variabel år som får verdien 2024
try: 
  alder = int(input("hvor gammel blir du i år?"))
  fødselår = år - alder
  print(f"Du er født i {fødselår}")
except:
  print("Ugyldig input. input må være en tall.")

print("Koden fortsetter...")

# Et annet eksempel

try:
  tall = int(input("Skriv et tall: "))
except:
  print("Ugyldig input. setter 'tall' til 10 ")
  tall = 10

print(tall) # tall er 10 hvia brukeren ikke skriver inn ett tall i input
