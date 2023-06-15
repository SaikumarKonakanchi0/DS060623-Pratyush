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

#Immutability check for Tuple
#Change the value of 30 into 500
# x=(10,20,30,40,50)
# x[2] = 500
# print(x)
#Change the value of 30 into 500

# Output:
# x[2] = 500
# TypeError: 'tuple' object does not support item assignment


#Mutability Check for List
# x=[10,20,30,40,50]
# print(id(x))
# x[2] = 500
# print(id(x))
# print(x)

# Output:

# 2730552979072
# 2730552979072
# [10, 20, 500, 40, 50]


# Mutable Objects(Hashable objects) --> List,Set Dictionary

# Immutable objects(Unhashable objects) --> int,float,complex,boolean,string,tuples

# Dictionaries are having keys and values:

# All immutable objects we can use as a key.

# x={{10,20,30}:20,30:40}
# print(x)
# Output:

# TypeError: unhashable type: 'set'

# Memory Utilization In python:

# In python if there is any requirement of creating an object
# then python will never create an object immediatly first it will
# check weather the object with same content is already present in 
# the heap memory or not if the object with the same content 
# is present the no any new object will be created the new variable
# is going to point to the older object only.

# Advantage of Memory utilization is Memory conservation or saving memeory.


# x=10
# y=10
# print(id(x))
# print(id(y))

# Output: 
# 2129844503056
# 2129844503056

# x="Python"
# y="Python"
# print(id(x))
# print(id(y))
#Output
# 2160280733360
# 2160280733360

# Note --> Memory utilization concept is applicable for integer
#          and string and boolean datatype.
    #    --> For all Other datatype(Float,complex,tuples) we cannot confirm this thing
    #        that a new object is created or not it depends on 
    #        different compilers/IDE'S.(In Jupyter a new object will be
            #created and in Python IDE no any new object will be created)
        #  --> List,set,dictionary are not following the concept of memoryview
        #      utilization.

#for float datatype:

# x=10.5
# print(id(x))
# y=10.5
# print(id(y))

#for complex datatype:

    
# x=10.5+20j
# print(id(x))
# y=10.5+20j
# print(id(y))

# #for list datatype:

    
# x=[10,20,30]
# print(id(x))
# y=[10,20,30]
# print(id(y))

# #for Tuples datatype:

    
# x=(10,20,30)
# print(id(x))
# y=(10,20,30)
# print(id(y))



# #for set datatype:

    
# x={10,20,30}
# print(id(x))
# y={10,20,30}
# print(id(y))


# #for dict datatype:

    
# x={10:20,20:30,30:40}
# print(id(x))
# y={10:20,20:30,30:40}
# print(id(y))


# #for boolean datatype:

    
# x=True
# print(id(x))
# y=True
# print(id(y))

#TypeCasting --> Converting one datatype to another

# list() --> any sequential datatype into list
# set() --> any sequential datatype into set
# tuple() --> any sequential datatype into tuple
# dict() --> any sequential datatype into dict


# Conversion of List to Tuple --> Possible 
# x=[10,20,30,40,50]
# y=tuple(x)
# print(y)


# (10, 20, 30, 40, 50)


#Conversion of List to Set --> Possible

# x=[10,20,30,40,50]
# y=set(x)
# print(y)

# Output:
# {40, 10, 50, 20, 30}

#Conversion of List to Dictionary --> Not Possible

# x=[10,20,30,40]
# y=dict(x)
# print(y)

# Output:
#   y=dict(x)
# TypeError: cannot convert dictionary update sequence element #0 to a sequence



#Conversion of tuple to list --> Possible


# x=(10,20,30,40,50)
# y=list(x)
# print(y)

# #Output:
# [10, 20, 30, 40, 50]

# Conversion of Tuple to set --> possible


# x=(10,20,30,40,50)
# y=set(x)
# print(y)

# #Output:
# {10, 20, 30, 40, 50}

# Conversion of Tuple to dictionary --> possible

# x=(10,20,30,40,50)
# y=dict(x)
# print(y)

#Output:

#   y=dict(x)
# TypeError: cannot convert dictionary update sequence element #0 to a sequence


#Conversion of set to list object --> Possible

# x={10,20,30,40}
# y=list(x)
# print(y)

#Output:

#[10,20,30,40]


#Conversion of set to tuple object --> Possible

# x={10,20,30,40}
# y=tuple(x)
# print(y)

#Output:

#(10,20,30,40)

#Conversion of set to dict object --> not Possible

# x={10,20,30,40}
# y=dict(x)
# print(y)

#Output:

#   y=dict(x)
# TypeError: cannot convert dictionary update sequence element #0 to a sequence

#Conversion of dictionary to list --> Possible

# x={10:20,30:40,50:60}
# y=list(x)
# print(y)

# Output:
# [10,30,50]

#Conversion of dictionary to tuple --> Possible

# x={10:20,30:40,50:60}
# y=tuple(x)
# print(y)

# Output:
# (10,30,50)

#Conversion of dictionary to set --> Possible

# x={10:20,30:40,50:60}
# y=set(x)
# print(y)

# Output:
# {10,30,50}

#Conversion of string to list --> Possible

# x="Python"
# y=list(x)
# print(y)

# Output:
# ['P', 'y', 't', 'h', 'o', 'n']

#Conversion of string to tuple --> Possible

# x="Python"
# y=tuple(x)
# print(y)

# Output:
# ('P', 'y', 't', 'h', 'o', 'n')

#Conversion of string to set --> Possible

# x="Python"
# y=set(x)
# print(y)

# Output:
# {'P', 'y', 't', 'h', 'o', 'n'}


#Conversion of string to dictionary --> not Possible

# x="Python"
# y=dict(x)
# print(y)

# Output:
# y=dict(x)
#ValueError: dictionary update sequence element #0 has length 1; 2 is required


# In which of the follwoing indexing is there?

# 1.list  --> Yes
# 2.tuple --> Yes
# 3.set  --> No
# 4.String  --> Yes
# 5.Dictionay --> No 


# WHich Datatype we can use as a key in dictionary?

# 1.tuple  --> Yes
# 2.int    --> Yes
# 3.List   --> No
# 4.set    --> No
# 5.Dict   --> No 
# 6.Float   --> Yes
# 7.Boolean --> Yes
# 8.Complex  --> Yes
# 9.String --> Yes

# x = [10,20,(30,40,50),60,70,[10,20,30]]
# print(id(x[2]))

# x = (10,20,[30,40,50],70) 
# x[2][1]=800
# print(x)

# Note --> Inside tuple if we are having a list then we can change
# the content of that list only.
# --> Inside list if we are having a tuple you cannot perform any changes
# in that tuple object other than this rest of the objects you can change.

x=[10,20,[30,40],60,70,"P30hon"]
x[2]=100
x[3]=300
print(x)
