#Python Program to check weather a given number
#is a leap year or not

# Condition:
# 1.The Year is a multiple of 400
# 2.The year is multiple of 4 but not multiple of 100

#Nested If else

year = int(input("Enter an Year :"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("True")
        else:
            print("True")
    else:
        print(False)
else:
    print(False)
