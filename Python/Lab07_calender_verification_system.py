
year=int(input("enter the year"))
if year<=0:
    print("invalid year")
else:
    if year%4!=0:
        print ("not a leap year,not divisible by 4")
    else:
        if year%100!=0:
            print("leap year")
        else:
            if year%400==0:
                print ("leap year")
            else:
                print("common year")


            