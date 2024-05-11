import json

with open("sykkelturer.json") as fil:
    data = fil.read()


def nest_høyest(liste: list[int]):
  høyest = float('-inf')
  nest_høyest = float('-inf')
  for tall in liste:
    if tall > høyest:
      nest_høyest = høyest
      høyest = tall
    elif tall > nest_høyest:
      nest_høyest = tall
  return nest_høyest

print(nest_høyest(...))

# Fikk ikke med meg at vi skulle levere hel og ikke 14:40 så fikk plutselig 40 minutter mindre en jeg trodde.
# Så gikk skeis i planleggingen der. 