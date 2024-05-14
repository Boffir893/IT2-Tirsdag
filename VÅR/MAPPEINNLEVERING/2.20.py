import json

# Funksjon for å finne de 10 brukerne med flest følgere
def finn_top_10_brukere(data):
    return sorted(data, key=lambda x: x.get('followers', 0), reverse=True)[:10]

# Funksjon for å regne ut antall tweets og følgere/følger-ratio for de 10 brukerne
def beregn_og_presenter_info(top_10_brukere):
    print("\nInformasjon for de 10 brukerne med flest følgere:")
    for bruker in top_10_brukere:
        antall_tweets = bruker.get('tweets', 0)
        antall_følgere = bruker.get('followers', 0)
        antall_følgere_følger = antall_følgere / bruker.get('following', 1) if bruker.get('following', 1) != 0 else 0
        print(f"Bruker: {bruker['username']}, Antall tweets: {antall_tweets}, Følgere: {antall_følgere}, Følgere/Følger-ratio: {antall_følgere_følger:.2f}")

# Leser data fra filen
with open('twitter.json', 'r') as file:
    data = json.load(file)


top_10_brukere = finn_top_10_brukere(data)
print("Top 10 brukere med flest følgere:")
for bruker in top_10_brukere:
    print(f"Bruker: {bruker['username']}, Følgere: {bruker.get('followers', 0)}")


beregn_og_presenter_info(top_10_brukere)

