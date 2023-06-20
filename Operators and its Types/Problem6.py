# Python Program to find simple interest

# Explaination:

# Take Three values as an input(P,R,T) and reflect
# simple interest based on those values.

#Formula of S_I = (P*R*T)//100

principle = float(input("Enter Principle : "))
rate = float(input("Enter Rate of Interest :"))
time = float(input("Enter Time :"))

S_I = (principle*rate*time)/100
print("The Simple Interest is :",S_I)
