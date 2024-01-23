def høyeste(liste: list[int]):
    høyest = liste[0]
    for tall in liste:
        if tall > høyest:
            høyest = tall
    return høyest

min_liste = høyeste
print(høyeste(min_liste))



