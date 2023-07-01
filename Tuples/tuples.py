# tuple --> Tuple is exactly same as list but the only difference 
#       between list and tuple is tuples are immutable but list are mutable.

#       --> Collection of dissimilar objects 
#       --> Parenthesis are used to represent a tuple.
#       --> Indexing is important in case of tuple(Ordered Collection) 
#       --> Duplicates are allowed in case of tuple.
#       --> Tuples are immutable.

# Creation of Tuple Object

#1. If we know the element :

# x=(10,20,30,40,50)
# print(type(x)) #<class 'tuple'>

#2.If we want to create empty tuple
# x=tuple()
# print(type(x)) #<class 'tuple'>

#3 Single element tuple
# x=(10,)
# print(type(x)) #<class 'tuple'>

# Note -> if we want to create a single object tuple then we 
# need to put comma at end

# Tuple Packing:

# If we are not giving any brackets and we are storing multiple 
# objects into a variable then that will be considered as a tuple 
# and this concept is known as Tuple packing

# x=10,20,"Python",50
# print(type(x))
# print(x)

#Output:

# <class 'tuple'>
# (10, 20, 'Python', 50)

#Tuple Unpacking 

# x,y,z,a = 10,20,30,40
# print(x,y,z) #10 20 30 40

# How to we can access the elements of a Tuple?
# 1.By INDEXING 
# 2.By Slicing

# Practice Questions:

# indexing --> tuple_name[index_value]
# slicing --> tuple_name[begim_index:end_index:step]

# x=(10,20,30,40,50)
# print(x[1])#20
# #print(x[5]) Error
# print(x[:]) #Whole tuple 
# #print(x[80]) #Error
# print(x[2:9])#(30,40,50)
# print(x[::-1])#Reverse Tuple
# print(x[::-4])#(50,10)
# print(x[10::9])#Empty Tuple
# #print(x[1:9:0])#Error 
# print(x[-1:1:-1]) #(50,40,30)
# print(x[10:1:4]) #Empty Tuple
# print(x[-3:1:-2]) #(30,)
# print(x[-1:-1:-1]) #Empty Tuple
# print(x[8:4:2])#Empty Tuple

# start value and end value both cannot same --> ()
# start value is greater than end value --> ()


# #Note --> There is no any type of insertion and deletion 
# function in case of tuple because tuples are immutable that means once 
# we will create tuple we cannot perform any changes in it.

# Tuple vs Immutability

# x=(10,20,30,40,50,60)
# print(id(x))
# x[2]=500
# print(id(x))

# Output:
# x[2]=500
# TypeError: 'tuple' object does not support item assignment  

# Note --> Tuples are immutable that means once we have created a 
# tuple object then we cannot perform any changes in that tuple 
# object.If we are trying to perform any changes then tuple 
# will raise an error.


# Operators that are used in Tuple:

# 1.Concatenation Operator(+)
# 2.Repition Operator(*)
# 3.Membership Operator(in and not in)
# 4.Identity Operator(is and is not)
# 5.Logical Operator(and or and not)
# 6.Comparison operator

# 1.Concatenation Operator(+) --> Join Two Tuples

# x=(10,20,30)
# y=(50,60,70)
# z=(80,90,10)
# print(x+y+z) #(10, 20, 30, 50, 60, 70,80,90,10)

# Note --> If we are using concatenation operator with tuple then 
# it is mandatory that both the operands are of tuple type.


# 2.Repition Operator(*) --> Repeat the elements of the tuple.

# x=(10,20,30)
# print(x*5) #(10,20,30,10,20,30,10,20,30,10,20,30,10,20,30)

# y = (40,50,"Python","Java")
# print(y*3) #(40, 50, 'Python', 'Java', 40, 50, 'Python', 'Java', 40, 50, 'Python', 'Java')
#Note --> If you are using repitition operator with tuple then it is  
# mandatory that one operand is of tuple type and second will be of 
# int type.

# 3.MemberShip Operator --> Return True if the given element is a part 
# of the tuple else it will return False 

# in and not in Operators

# x=(10,20,30,40,"Python","Java")
# print(10 in x)#True
# print("C++" not in x)#True

# 4.Identity Operator --> return True if two tuple objects are 
# pointing to same memeory location else it will return False.

# is and is not Operators

# x=(10,20,30)
# y=(10,20,30)
# print(x is y) #True


# x=(10,20,30,50,60)
# y=(10,20,30)
# print(x is y) #False

# 4.Logical Operator(and , or , not):

# () --> False 
# other than this --> True

# x=() and (10,20,30)
# print(x) #()

# x=(10,20) and (50,60)
# print(x) #(50,60)

# x = () or ("Python","Java")
# print(x)#("Python","Java")

# x=("C++","c") or (10,20,30)
# print(x) #("C++","c")

# x = not()
# print(x) #True

# Relational and Comparison Operator

# x=(10,20,30)
# y=(40,50,60)
# print(x>y) #False 

# x=(10,20,30)
# y=(10,30,50)
# print(y>x)#True

# Max and Min Function --> This function will work in every sequence 
# datatype.


# max function --> Return Maximum value from the sequence(Tuple,list,Set)
# min Function --> Return Minimum value from the sequence(Tuple,list,Set)


# x = [10,20,30,40,50,100,23,134,2,535]
# print(max(x))#535

# x = [10,20,30,40,50,100,23,134,2,535]
# print(min(x))#2

# x = (10,20,30,40,50,100,23,134,2,535)
# print(max(x))#535

# x = (10,20,30,40,50,100,23,134,2,535)
# print(min(x))#2

# x = {10,20,30,40,50,100,23,134,2,535}
# print(max(x))#535

# x = {10,20,30,40,50,100,23,134,2,535}
# print(min(x))#2

# Sorted Function --> Sort the elements of a tuple in ascending or descending order.

# #ascending order sorting
# x=(89,45,24,256,122,62,7,3)
# print(sorted(x)) #[3, 7, 24, 45, 62, 89, 122, 256]

# #descending order sorting
# x=(89,45,24,256,122,62,7,3)
# print(sorted(x,reverse=True)) #[256, 122, 89, 62, 45, 24, 7, 3]

# list_name.function(value)  #Specific To that object 

# x.append(10)
# len(x)

# sorted(list)  --> string,list,tuple,set
# len()  --> string,list,tuple,set 
# append() --> list 
# max --> tuple,list,set

# List vs Tuple

# 1.List is represented with the help of square brackets. 
# 1.Tuple is  represneted with the help of parenthesis

# 2.List is mutable.
# 2.Tuple is Immutable.

# 3.List is slower then Tuple 
# 3.Tuple are faster than list 

# 4.Lists consumes more memory  
# 4.Tuple consumes less memeory 

# 5.Lists are used to insertion and deletion operation.
# 5.Tuples are used to accessing operation.

