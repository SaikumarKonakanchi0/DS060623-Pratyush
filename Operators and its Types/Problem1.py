#Python Program to Perform all arithmetic operations

# Explaination:

# Take Two Numbers from the User and Apply all
# the Arithmetic operators on it and return Result.

#Solution:

first   = int(input("Enter a Number : "))
second  = int(input("Enter Second Number :"))
add     = first+second 
sub     = first-second 
mul     = first*second 
div     = first/second 
fdiv    = first//second 
mod     = first%second
exp     = first**second 

print("Addition of Given numbers is",add)
print("Subtraction of Given numbers is",sub)
print("Multiplication of Given numbers is",mul)
print("Division of Given numbers is",div)
print("Floor Division of Given numbers is",fdiv)
print("Modulus of Given number",mod)
print("Power of the Number is ",exp)
