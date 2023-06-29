# List ==> List is nothing but a collection of dissimilar objects.
#      ==> If we want to store multiple objects as a single entity then
#          we are going to use list. 
#      ==> Indexing is very important in case of List(Ordered Collection). 
#      ==> Duplicates are allowed in case of List.
#      ==> Lists are Mutable(Changable)
#      ==> Square brackets are used to represent a list.


# Creation of List Object.

# l = []   #Empty list
# l = list()   #Empty list
# l = [10,20,30,40,50,60]


# x = []
# print(type(x))
# print(len(x))

# x = list()
# print(type(x))
# print(len(x))

#How to access an element from a list?

# 1.By Indexing
# 2.By Slicing

# Practice Questions based on List
# indexing syntax --> list_name[index_num]
# Slicing --> list_name[begin_index : end_index : step]

# x = [10,20,30,40,50]
# print(x[1:9:0]) #Error
# print(x[1]) #20
# #print(x[5]) #Error
# # print(x[80]) #Error
# print(x[-1]) #50
# print(x[::]) #Whole list
# print(x[:]) #Whole list
# print(x[::-1]) #Reverse of the list
# print(x[::-3])  #[50,20]
# print(x[10:9])  #[]
# print(x[2:9]) #[30,40,50]
# print(x[-5:-1:-2]) #Empty list
# print(x[-5:-1:2]) #[10,30]
# print(x[1:-1:-2]) #Empty List
# print(x[1:-1:2]) #[20,40]

# Note --> If step value is 0 then only slicing will give an error.

# Builtin Functions of List

# len() Function --> return the number of element of the list.

# Example:

# x=[10,20,30,40,50]
# print(len(x)) #5

# x=[]
# print(len(x)) #0

# x=list()
# print(len(x)) #0

# Count Function --> return the number of occurances of the given element.

# Syntax:
# list_name.count(element)

# x=[10,20,30,40,50,10,20,30,40,50,60,20,30,40,50,60]
# print(x.count(50)) #3

# x=[10,20,30,40,50]
# print(x.count(100)) #0

# Index Function --> is used to get the first index of element.
#                --> if the element is not present we will get value error.


# Syntax:

# list_name.index(element)

# x=[10,20,30,40,50,10,20,30,40]
# print(x.index(20)) #1


# x=[10,20,30,40,50,10,20,30,40]
# print(x.index(200)) #error

# Insertion Function of Lists

# Lists are Mutable .Mutable means we can add delete elements from list.

# In Python if you want to insert something in list we are having three functions.

# 1.Append Function 
# 2.Insert Function 
# 3.Extend Function

# Append Function --> Append function will always take a single object 
#                     as an input and add that object inside the list at last.

# Syntax:

#  list_name.append(data)

# x = []
# print(x)
# x.append(10)
# print(x)
# x.append(20)
# print(x)
# x.append("Hello")
# print(x)
# x.append([10,20,30])
# print(x) #[10,20,"Hello",[10,20,30]]

# How to Take List as an Input()

# 1.With the help of loops
# 2.With the help of eval function
# 3.With the help of list comphersion
# 4.With the help map function

# With the help of loops

l=[]
num = int(input("Enter the Number of Elements :")) #5
for i in range(1,num+1): #1,2,3,4,5
    ele  = str(input(f"Enter {i} Element : ")) #10  20
    l.append(ele)
print(l)


    