day = input("Enter a Day")
Month = input("Enter Month")
if day=="Sunday":
    print("Hurrah Today is Sunday")
    if Month in ["Jan","Feb","Mar","June","Jul","Aug","Sep","Oct","Nov","Dec"]:
        print("Today I will Go to Play Cricket")
    else:
        print("Oh this is April month I need to Study for Exams")

elif day=="Monday":
    print("Oh Today is Monday")
    if Month in ["Jan","Feb","Mar","April","Jul","Aug","Sep","Oct","Nov"]:
        print("Oh I need to Go to School")
    else:
        print("Hurrah It's Vacation Time")