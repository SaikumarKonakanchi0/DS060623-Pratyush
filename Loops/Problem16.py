#Python Program to print sum of cube of N natural Number Using for loop

# n=5
# 1**3 + 2**3+ 3**3 + 4**3 + 5**3 = 3+8+27+64+125 = 

# 1+2+3+4+5

# num = int(input("Enter a number :"))
# sum = 0
# for i in range(1,num+1):
#     sum=sum+i**3
# print(sum)

#Python Program to print sum of cube of N natural Number Using while loop

num = int(input("Enter a Number :"))
i=1
sum=0
while i<num+1:
    sum=sum+i**3 
    i=i+1 
print(sum)


