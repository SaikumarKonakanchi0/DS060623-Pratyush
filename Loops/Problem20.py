#Python program to Count number of digits from a Number



#Note --> If we want to work over digits we need to use while

# while num!=0:

num = 12345
count = 0
while num!=0:
    num=num//10
    count=count+1 
print(count)

