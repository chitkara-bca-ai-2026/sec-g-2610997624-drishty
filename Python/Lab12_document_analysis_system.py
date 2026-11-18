pasw=input("Enter password:")
vowels=0
const=0
spaces=0
spc=0
for ch in pasw:
    if ch.isalpha():
        if ch in "aeiouAEIOU":
            vowels+=1
        else:
            const+=1    
    elif ch.isspace():
        spaces+=1
    else:
        spc+=1   
print("Vowels",vowels)
print("consonants",const)
print("spaces",spaces)
print("special characters",spc)           

            