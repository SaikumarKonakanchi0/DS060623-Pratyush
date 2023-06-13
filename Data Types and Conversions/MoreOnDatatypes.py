# Standard Datatype --> int,float,complex,boolean and SyntaxWarning
# TypeCasting --> The process of Converting  one datatype to another

# Types of TypeCasting:

# 1.Implict  TypeCasting
# 2.Explict TypeCasting

# 1.Implicit TypeCasting: 
# ------------------------
# In this typecasting,Python converts the datatype into another datatype
# automatically.
# a=7
# print(type(a))
# print(a)
# b=10.0
# print(type(b))
# print(b)
# c=a+b 
# print(type(c)) #float  
# print(c)#17.0
# d=a*b
# print(type(d)) #stringstringstringstringstring
# print(d)

# Explicit TypeCasting : In this type of TypeCastinG Programmers/
# developers need to convert one datatype to another.

# For TypeCasting We need to use few Functions:

# int()  --> for converting any datatype to int datatype
# float()  --> for converting any datatype to float datatype
# str()  --> for converting any datatype to string datatype
# bool() --> for converting any datatyoe to bool datatype
# complex() --> for converting any datatype to complex datatype.

# a=10
# print(type(a)) #int
# print(a) #7
# b=18.8989
# print(type(b))  #float
# print(b) #10.9876
# c=a+b  #28.8989
# d=str(c) #28.8989 --> string
# print(type(d)) #int
# print(d)#17

#If we are trying to convert float into integer then the content
#/digits that are present after decimal will be ignored

# Possibilities  of Conversions of one datatype to another:

# Conversion of Float to int Datatype --> Possible

# x=10.98364
# y=int(x)
# print(y)
# print(type(y)) 

# #Conversion of Complex to int Datatype --> Not Possible

# x=10+20j
# y=int(x)
# print(y)
# print(type(y)) 

#Conversion of Boolean to int Datatype -->  Possible

# x=True  #1
# y=int(x)
# print(y)
# print(type(y)) 

# x=False  #0
# y=int(x)
# print(y)
# print(type(y)) 


#Conversion of String to int Datatype --> Possible/not Possible

# Note --> In case of string if the content inside the quatation is
#          in the form of integer then only string to int datatype
#          conversion is possible

# x="10"
# y=int(x)
# print(type(y))
# print(y)

# # x="10.5"
# # y=int(x)
# # print(type(y))
# # print(y)

# x="abc10"
# y=int(x)
# print(type(y))
# print(y)


#Conversion of int to float Datatype -->  Possible

# x=10
# y=float(x)#10.0
# print(y)
# print(type(y))


#Conversion of complex to float Datatype -->  Not Possible


# x=10+20j
# y=float(x)
# print(y)
# print(type(y))


#Conversion of boolean to float Datatype -->  Possible

# x=True  #1
# y=float(x)  #1.0
# print(y)
# print(type(y))


# x=False #0
# y=float(x)  #1.0
# print(y)
# print(type(y))



#Conversion of string to float Datatype -->  Not Possible/Possible


# Note --> In case of string if the content inside the quatation is
#          in the form of integer or float then only string to 
#           float datatype conversion is possible

# x="10"
# y=float(x)
# print(type(y))
# print(y)

# x="10.5"
# y=float(x)
# print(type(y))
# print(y)

# x="abc10"
# y=int(x)
# print(type(y))
# print(y)


#Conversion of int to complex Datatype -->  Possible

# x=10
# y=complex(x)  #--> 10+0j =10
# print(y) #10+0j
# print(type(y))

#Conversion of float to complex Datatype -->  Possible
# x=10.9
# y=complex(x)  #--> 10.9+0j =10.9
# print(y) 
# print(type(y))


#Conversion of boolean to complex Datatype -->  Possible

# x=True  #1+0j
# y=complex(x)  
# print(y) 
# print(type(y))

# x=False #0+0j
# y=complex(x)  
# print(y) 
# print(type(y))



#Conversion of string to complex Datatype -->  Not Possible/Possible



# Note --> In case of string if the content inside the quatation is
#          in the form of integer  float or complex then only 
#          string to complex datatype conversion is possible

# x="10"
# y=complex(x)
# print(type(y))
# print(y)

# x="10.5"
# y=complex(x)
# print(type(y))
# print(y)
# x="10.5+20j"
# y=complex(x)
# print(type(y))
# print(y)

# x="True"
# y=complex(x)
# print(type(y))
# print(y)


# For String Conversion:

# You can convert any datatype into string.

# x=10
# y=str(x)
# print(type(y))
# print(y)

# x=10.5
# y=str(x)
# print(type(y))
# print(y)

# x=10+20j
# y=str(x)
# print(type(y))
# print(y)

# x=True
# y=str(x)
# print(type(y))
# print(y)

# Boolean Conversion:

# 0,0.0,0+0j,False,""  --> False
# Other This --> True

# x=10+0j
# y=bool(x)
# print(type(y))
# print(y)

# x=0.0001
# y=bool(x)
# print(type(y))
# print(y)

# x=0.000000000000000000000000
# y=bool(x)
# print(type(y))
# print(y)

# x=0.0001
# y=bool(x)
# print(type(y))
# print(y)

# x="-1989484"
# y=bool(x)
# print(type(y))
# print(y)

# 0.0001
# Whatever empty content is there that will be considered as False

# 0 --> Empty Number
# 0.000  --> Empty Float Number
# ""  --> empty string 
# 0+0j --> empty complex 


# Standard Datatypes --> Integer,Float,String,Boolean,complex

# --> List,Tuple and Set are used to store multiple values.

# List Datatype:

# --> List is a collection of dissimilar elements.
# --> If we want to store multiple values as a single enitity
# then we are going to use list datatype
# --> Sqaure brackets are used to represent a list
# --> List is mutable(We can perform changes in list)

# x =[10,10.5,'Python',10+20j]
# print(x[3])
# print(type(x))
#Acces any element of list

#Syntax :   list_name[index_number]

#Tuple Datatype

# --> Tuple is a collection of dissimilar elements.
# --> If we want to store multiple values as a single enitity
# then we are going to use tuple datatype
# --> Parenthesis are used to represent a tuple
# --> Tuple is immutable(We cannot perform any changes or tuples are fixed)
# --> Read only version of list

# x =(10,10.5,'Python',10+20j)
# print(x[3])
# print(type(x))
# Acces any element of list

# Syntax :   list_name[index_number]


# Set Datatype:

# Set is also a collection of element.
# Set doesnot contain duplicate values.
# In set indexing is not possible
# Curly barces are used to represent a set
# Sets are mutable(We can perform changes)

# x = {1,1,1,2,3,2,4,24,1,4,1,42,4}
# print(x)
# print(type(x))


# Dictionary Datatype: 

# Dictionary is also a collection of element that will store Data in the
# form of Keys and Values.

# Curly Braces are used to represent a dictionary and each and
# every key value pair is seperated by :.


# Dictionaries are Mutable(We can perform changes.)

# Dictionary keys must be unique if we are using
# duplicate keys the only last key value pair will be considered.

# name:"SANJAY"
# Mobile_no:9876543210
# College:"EDYODA DIGITAL UNIVERSITY"

# x = {True:20,10+20j:"Python","Mobile_no":9876543210,"College":"EDYODA DIGITAL UNIVERSITY","College":"Amity University"}
# print(type(x))
# print(x)

# <class 'dict'>
# {True: 20, (10+20j): 'Python', 'Mobile_no': 9876543210, 'College': 'Amity University'}


# Syntax for accessing any value:

# dictionary_name[key_val]

# x = {True:20,10+20j:"Python","Mobile_no":9876543210,"College":"EDYODA DIGITAL UNIVERSITY","College":"Amity University"}
# print(type(x))
# print(x)
# print(x["Mobile_no"])
# print(x[10+20j])

# <class 'dict'>
# {True: 20, (10+20j): 'Python', 'Mobile_no': 9876543210, 'College': 'Amity University'}
# 9876543210
# Python

# Two Important Function

# print() ==> Display the output
# input() ==> Take input from end user in the form of string

x = float(input("Enter a Number"))
y = float(input("Enter second Number "))
z=x+y
print(z)