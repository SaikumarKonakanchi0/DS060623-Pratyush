# Write a Python program to return difference between  count 
# of odd numbers and count of even numbers

# Input 1 = [10,20,30,40,50,33,23,12]

# count of odd numbers  - count of even number 
# 2-6
# -4

num = [10,20,30,40,50,33,23,12]
count_odd = 0
count_even=0
for i in num:
    if i%2==0:
        count_even+=1

    else:
        count_odd+=1
print(count_odd-count_even)



