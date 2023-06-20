# Python Program to Find Compound Interest

# Formula of Compound Interest:

# Amount = p*(1+r/100)**t
# Compount_Interest = Amount-p

principle = float(input("Enter Principle :"))
rate = float(input("Enter Rate:"))
time = float(input("Enter Time"))
amount = principle*(1+rate/100)**time 
C_I = amount-principle
print("The Compound Interest is ",C_I)