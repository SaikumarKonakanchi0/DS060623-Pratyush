#Python Program to check weather
# a number is divisible by 7 and 11 or not.

#Without Nested Conditional Statements
n=int(input("Enter a Number :"))
if n%7==0 and n%11==0:
    print("Number is divisble by 7 and 11")


#With Nested Conditional Statements

if n%7==0:
    if n%11==0:
        print("Number is Divisble by 7 and 11")
    else:
        print("Number is only divisble by 7 not 11")

else:
    print("Number is not divisble by 7")