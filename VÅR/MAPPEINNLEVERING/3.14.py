# Lag et program som genrerer mailadresser fra fornavn og etternavn. Mailen skal bestå av hele det første fornavnet og 
# første bokstav i etternavnet etterfulgt av @afk.no. For eksempel skal Thor Christian Coward bli thorc@afk.no. Som input 
# til programmet må brukeren skrive inn minst to navn (fornavn og etternavn), hvis ikke skal brukeren få en feilmelding og få 
# lov til å skrive input på nytt.

while True:
    try:
        first_name, last_name = input("Enter your first and last name: ").split()
        if len(first_name) == 0 or len(last_name) == 0:
            raise ValueError()
        break
    except ValueError:
        print("Please enter a valid first and last name, separated by a space.")

email = f"{first_name.lower()}@{last_name[0].lower()}.afk.no".strip()

print(f"Your email address is: {email}")

