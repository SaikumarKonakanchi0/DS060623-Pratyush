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

x=10,20,"Python",50
print(type(x))
print(x)

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

x=(10,20,30,40,50)
print(x[1])#20
#print(x[5]) Error
print(x[:]) #Whole tuple 
#print(x[80]) #Error
print(x[2:9])#(30,40,50)
print(x[::-1])#Reverse Tuple
print(x[::-4])#(50,10)
print(x[10::9])#Empty Tuple
#print(x[1:9:0])#Error 
print(x[-1:1:-1]) #(50,40,30)
print(x[10:1:4]) #Empty Tuple
print(x[-3:1:-2]) #(30,)
print(x[-1:-1:-1]) #Empty Tuple
print(x[8:4:2])#Empty Tuple

# start value and end value both cannot same --> ()
# start value is greater than end value --> ()




