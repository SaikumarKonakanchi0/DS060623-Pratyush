# Keyword : In python there are some predefined or reversed words
# whose meaning python already knows such type OverflowError
# such type of are known as Keywords.
# x = True
# print(x)

# In python 3.10 we have 35 words

# English Langauge --> Infinite

#For getting all the keywords in python we need to use below statements

# import keyword
# print((keyword.kwlist))
# print(len(keyword.kwlist))

# x = False
# print(x)

#Objects --> Any real world entity 
  
#          --> Each and every object is having two things : Behaviour and Attributes.

# Behaviour --> Functionality
# Attributes/Properties --> Data/Specification

# Example:
# Dog --> Behaviour(Functionality) --> Barking,Running 
#         Properties --> 4Legs,2Eyes,Tail,Bread,color

# Human --> Behaviour(Functionality) --> Thinking,Speaking,Listening.
#           Properties --> 2Eyes,Gender,Apperance

# Mobile --> Behaviour(Functionality) --> Calling,Browsing,Gaming
#            Properties --> Model,Desgin,Color,RAM,ROM,Operating

# Television --> Behavior(functionality) --> vOLUME,BROWSING,BLUETOOTH
#                Properties --> SIZE,LED,LCD,BRAND,COMPANY


# Before Implementing any object we need to create a class.

# Class is nothing but a blueprint of an object


# Note --> In Python each and every thing is nothing but an object.
# That is a main reason when we are checking the type of type
# of any data then we will get something like class XXX

# x="Hello"
# print(type(x))

#How are Objects are stored in python?

# In Python each and every thing is an object and For storing that
# object in Python we are having private heap block and each
# every object is going to stored at that private heap.


# x=10

# x --> Variable --> Data
# = --> Instruction/Code 
# 10 --> Heap Memeory

# Pratice questions for counting number of objects?

# x = []  #One Object --> list
# x = 10.0 #One object --> float
# x = [10,20,30]  #4 objects --> 3 INT OBJECTS AND 1 LIST OBJECT
# x = {10,20,30,10,20,40,50,60,10,20}  #--> 6 int obj and 1 set object
# X = [10,[10,20,30],"Python",3.15,{10,20,30,10,20}]
# print(X)

# Mutability Vs Immutability


# Mutability means we can change the content(Changeable)

# Immutability means we cannot change the content(UnChangeable)

# Immutable Objects --> int,string,float,complex,boolean,tuples
# Mutable Objects --> list,Set, Dictionary

# Immuatbility check for Int Datatype

# In case of Immutable objects Two possibilites are there

# 1.A new object is created --> int,float,complex,boolean,string
# 2.You cannot perform anything on such object(ERROR) --> Tuple

# Immuatbility check for Int Datatype
# x=10
# print(id(x))
# x=x+5
# print(id(x))

# Immuatbility check for Float Datatype
# x=10.5
# print(id(x))
# x=x+5.5
# print(id(x))

# #Immuatbility check for String Datatype
# x="String1"
# print(id(x))
# x=x+"Python"
# print(id(x))

# Immuatbility check for Boolean Datatype
# x=True
# print(id(x))
# x=x+False
# print(id(x))

# Immuatbility check for Complex Datatype
# x=10+20j
# print(id(x))
# x=x+20+30j
# print(id(x))


