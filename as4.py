user = int(input("Enter the year in yyyy format..."))
if user % 4 == 0 or user % 100 == 0 :
    print(f"{user} The given year is leap year")
else :
    print(f"{user} The given year is not leap year")