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

