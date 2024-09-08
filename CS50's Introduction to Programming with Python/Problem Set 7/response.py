import validators

if validators.email(input("What's your email adress? ")):
    print("Valid")
else:
    print("Invalid")
