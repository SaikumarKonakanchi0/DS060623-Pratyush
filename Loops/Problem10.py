#Python Program to find Factorial of a Number 

# n=5 
# 5*4*3*2*1 = 120

# 1*2*3*4*5 =120

#Generate Number from 1 to n
#Multiply the previous number with curr number
# and assign it to a variable fact.

num = int(input("Enter a Number :"))
fact = 1 
for i in range(1,num+1):
    fact=fact*i 
print("Factorial Value is ",fact)