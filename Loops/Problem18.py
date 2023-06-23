#Write a Python Program to get different between the sum of odd 
#numbers and sum of even numbers.

# a = [1,2,3,4,5]
# odd number  =  1+3+5 = 9
# even number = 2+4 = 6

# diff - 9-6 = 3

a = [1,2,3,4,5]
sum_even = 0
sum_odd=0
for i in a:
    if i%2==0:
        sum_even+=i
    else:
        sum_odd+=i 

print(sum_odd-sum_even)