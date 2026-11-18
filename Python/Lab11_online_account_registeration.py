
pasw=input("Enter password:")
containisupper=False
containislower=False
containindigit=0
for ch in pasw:
    if ch.isupper():
        containisupper=True
    elif ch.islower():
        containislower=True
    elif ch.isdigit():
        containisdigit=True
if containisupper and containislower and containisdigit and len(pasw)>=8:
    print("Valid")
else:
    print("invalid")


         

        