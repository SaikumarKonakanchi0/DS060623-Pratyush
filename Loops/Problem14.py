#Python program to print factorial of a Number using for loop

# num = int(input("Enter a Number :"))
# fact=1
# #5 --> 1*2*3*4*5
# for i in range(1,num+1):
#     fact=fact*(i)
# print(fact)


# Python Program to Print Factorial Of a Number Using While Loop

num = int(input("Enter a Number :"))
i=1
fact=1
while i<num+1:
    fact=fact*i
    i=i+1
print(fact)
