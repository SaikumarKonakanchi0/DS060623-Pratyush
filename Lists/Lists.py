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

# l=[]
# num = int(input("Enter the Number of Elements :")) #5
# for i in range(1,num+1): #1,2,3,4,5
#     ele  = str(input(f"Enter {i} Element : ")) #10  20
#     l.append(ele)
# print(l)

#insert Function  --> Insert function is used to add an element into
#                      the given index of the list.

# Syntax:
      
#       list_name.insert(index_value,data)

# Example:

# x=[10,20,30,40,50]
# x.insert(2,"Python")
# print(x) #[10,20,"Python",30,40,50]

# x=["Python","Java","C","C++","JavaScript","Kotlin","R"]
# index = 4 
# data = "Swift"
# x.insert(4,"Swift")
# print(x) #['Python', 'Java', 'C', 'C++', 'Swift', 'JavaScript', 'Kotlin', 'R']

# x=["Python","Java","C","C++","JavaScript","Kotlin","R"]
# x.insert(200,"Swift")
# print(x)#['Python', 'Java', 'C', 'C++', 'JavaScript', 'Kotlin', 'R', 'Swift']

# x=["Python","Java","C","C++","JavaScript","Kotlin","R"]
# x.insert(-200,"Swift")
# print(x)#['Swift', 'Python', 'Java', 'C', 'C++', 'JavaScript', 'Kotlin', 'R']


# x=["Python","Java","C","C++","JavaScript","Kotlin","R"]
# x.insert(0,(10,20,30)) 
# print(x)#[(10, 20, 30), 'Python', 'Java', 'C', 'C++', 'JavaScript', 'Kotlin', 'R']

#Note --> If the given index value is not present then :
    #   --> If the index value is positive then the data will be added 
    #       at last position.
    #   --> if the index value is negative then the data will be added 
    #       at the first position.

# Extend Function --> This function is used to add multiple elements 
#                     of the sequence into a list.
#                 --> Extend function will always take sequence as an input.

# Syntax:
   
#    list_name.extend(sequence)

# Example:

# x = [10,20,30,40,50]
# y = [50,60,70,80]
# x.extend(y)
# print(x) #10, 20, 30, 40, 50, 50, 60, 70, 80]


# x = [10,20,30,40,50]
# y = (50,60,70,80)
# x.extend(y)
# print(x) #[10, 20, 30, 40, 50, 50, 60, 70, 80]


# x = [10,20,30,40,50]
# y = {50,60,70,80}
# x.extend(y)
# print(x) #[10, 20, 30, 40, 50, 50, 60, 70, 80]

# x = [10,20,30,40,50]
# y = {50:10,60:30,70:50,80:90}
# x.extend(y)
# print(x) #[10, 20, 30, 40, 50, 50, 60, 70, 80]

# x = [10,20,30,40]
# x.extend(10)
# print(x) #TypeError: 'int' object is not iterable

# x = [10,20,30,40]
# x.extend("Python")
# print(x) #[10, 20, 30, 40, 'P', 'y', 't', 'h', 'o', 'n']

# Difference Between Extend,Append and Insert Function

# Append --> Adding the object at the last position.
# Insert --> Adding the object at given position
# extend --> Will take sequence as an input and based on that 
#            sequence the elements will be added at last

# Practice Question:

# Which of the following syntax is invalid?

# 1.x.append(10,20,30) #Invalid
# 2.x.append([10,20,30]) #Valid
# 3.x.append([10]) #Valid
# 4.x.append(40) #Valid
# 5.x.extend(10,20) #Invalid
# 6.x.extend([10,30,40]) #Valid
# 7.x.extend((10,20)) #Valid
# 8.x.extend("Python") #Valid
# 9.x.append(("Python")) #Valid
# 10.x.insert(1,"Java") #valid

# Deletion Functions of Lists:

# In List we are having three function for deletions:

# 1.Pop() without argument
# 2.Pop(index) with argument
# 3.remove() Function

# Note --> In pop function if the list is empty you will get an error.

# Pop Function without Arguments --> This function will delete the last
# object of the list and also return the deleted object

# Example:

# x=[10,20,30,40,50,60,70]
# print(x.pop()) #70
# print(x)#[10,20,30,40,50,60]

# x=[]
# print(x.pop()) #IndexError: pop from empty list


#Pop Function With Argument --> This function will delete the 
# object that is present at the given index of the list and 
# also return the deleted object.

# x = []
# print(x.pop(2))#IndexError: pop from empty list

# x=[10,20,30,40,50,60,70]
# print(x.pop(4)) #50
# print(x)#[10,20,30,40,60,70]


# x=[10,20,30,40,50,60,70]
# print(x.pop(400)) #Error

# Remove Function --> Delete a specified element.

# Example:

# x=[10,20,30,40,50,60,10,20]
# x.remove(20)
# print(x) #[10, 30, 40, 50, 60, 10, 20]


# x=[10,20,30,40,50,60,10,20]
# x.remove(200)
# print(x) #Error

# Difference Between Deletion Function

# pop() --> This function will delete an element from the last position of the list and return the deleted value.
# pop(index) --> This function will delete an element from the given index and also return the deleted value.
# remove(value) --> Delete the specified value.

# reverse function --> This function is used to reverse a given list and 
# it will also return the reversed list.

# Syntax:

# list_name.reverse()

# x=[10,20,30,40,50,60,70]
# x.reverse()
# print(x) #[70, 60, 50, 40, 30, 20, 10]


# Difference between reverse and slicing(x[::-1]) reverse.

# 1.When we are using reverse function then there is no any new object 
# will be created whatever reversing is there that is done only 
# in original object.

# 2.When we are using slicing for reverse then Slicing will create a  
# new object and then it will reverse the content of the list


# Demonstration:

# x=[10,20,30,40,50]
# print(id(x))
# x.reverse()
# print(id(x))


# x=[10,20,30,40,50]
# print(id(x))
# x=x[::-1]
# print(id(x))

# Output:

# 2281117652032
# 2281117652032
# 2281117576832
# 2281117652032

# sorted Function --> Sort the given data in ascending order or 
#                     descending order.

# Syntax:

# sorted(list_name)

# #for ascending order sorting
# x=[109,20,304,40,430,60]
# print(sorted(x)) #[20, 40, 60, 109, 304, 430]



# #for descending order sorting
# x=[109,20,304,40,430,60]
# print(sorted(x,reverse=True)) #[430, 304, 109, 60, 40, 20]

# sort function --> This function will sort our list in ascending or 
#                   descending order.

# Syntax:

#       list_name.sort()

# #Ascending order sorting
# x = [109,20,304,40,430,60]
# x.sort()
# print(x)

# #Descending order sorting
# x = [109,20,304,40,430,60]
# x.sort(reverse=True)
# print(x)

# Output:

# [20, 40, 60, 109, 304, 430]
# [430, 304, 109, 60, 40, 20]

# Difference between sort and sorted function

# 1.When we are using sort function then there is no any new object 
# will be created whatever sorting is there that is done only 
# in original object.

# 2.When we are using sorted for sorting then sorted function will create a  
# new object and then it will sort the content of the list


# Demostration:

# x = [109,23,53,12,85]
# print(id(x))
# x.sort()
# print(id(x))

# Output:
# 2652755979904
# 2652755979904

# x = [109,23,53,12,85]
# print(id(x))
# print(id(sorted(x)))

#Output:
# 1879167987328
# 1879168004736

# Sort --> Sorting will be done in original object
# sorted --> A new object will be created and then sorting will be done.

# Operators that we can use in list

# 1.Concatenation operator 
# 2.Reptition Operator 
# 3.Memebership operator 
# 4.Identity Operator 
# 5.Logical Operator 
# 6.Comparion and Relational Operator

# Concatenation Operator(+) --> Join Two List

# x=[10,20,30]
# y=[40,50,60]
# print(x+y)

#Note : In case of list + operator will work as a concatenation operator 
#if both the operand are of list type only.

#Repition Operator(*) --> Repeat the content of the list 


# Note --> In case of list * operator will work as repition operator 
# if one operand is of int type and second operan is of list type.


# x=[10,20,30] 
# print(x*5) #[10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30]

# Membership Operator(in and not in) --> Return True if the element is 
# the part of list else it will return False.

# x = [10,20,30,40,50,60,70]
# print(10 in x) #True
# print(100 not in x) #True

# Identity Operator(is and is not) --> return True if two list objects 
# are pointing to the same memory location else it will return False

# x=[10,20,30,40,50,60]
# y=[10,20,30,40,50,60]
# z=[10,20,30,40,50,60]
# print(x is y) #False
# print(x is not z) #True

#Logical Operators(and , or ,and not):

# [] --> means False 
# Everything is True

# x = [] and [10,20,30]
# print(x) #[]

# x = [10,20] and [40,50]
# print(x) #[40,50]

# x=[] or ["Python"]
# print(x) #["Python"]

# x=[10,20] or ["Hello"]
# print(x)#[10,20]

# x=not[]
# print(x) #True

# Comparison and Relational Operator(<,>,<=,>=,!=)

# x=[10,20,30]
# y=[10,40,50]
# print(x>y)#False

# x=["Python","Java",10,20]
# y=[10,20,30,40]
# print(x>y) #Error

#Note --> If you want to use comparison operator then element of 
# both the list must of same type


# List vs Mutability

# List is mutable in nature that means we can perform  any
# changes in it and those changes will be done into the original list 
# object only no any new object will be created for list.


# Demonstration:

# x=[10,20,30,40,50]
# print(id(x))
# x.append(100)
# print(id(x))

# Output:
# 1947355836032
# 1947355836032

# How to change/update element of a list?

# Syntax:

# list_name[index] = updated value

# x = [10,20,30,40,50]
# x[2]=500
# print(x)

# Traversal or Iteration over list

x = [10,20,30,40,50,60]
# for i in x:
#     print(i)

# for i in range(len(x)):
#     print(x[i])
i=0
while i<len(x):
    print(x[i])
    i=i+1

















    