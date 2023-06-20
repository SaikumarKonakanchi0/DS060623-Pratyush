# Operators --> Operators are the Special Symbols
#               that are used to perform a specific 
#               Task

# Example:

# + --> Addition
# * --> Multiplication
# // --> Dividation
# - --> Subtraction

# Operand --> The variables or value that are involved
#             in any operation is known as Operand.

# Example:
    
#     c=a+b 
#      c=10+20
    
#     c,a,b --> Operands

# Expression --> Expression is nothing but a combination
#                of operator and operand

# Example:

#      c=a+b  --> Expression

# Example of Operator Operand and Expressions.


# a=10 
# b=20 
# c=a+b 

# Operator --> +,=
# Variables --> a,b,c 
# Operand --> a,b,c 
# Expression --> c=a+b

# a=10
# b=20
# c=a+b-a 

# Operators --> +,-,=
# variables --> a,b,c 
# Operand --> a,b,c
# Expression --> c=a+b-a

# Types of Operators in Python.

# 1.Arithmetic Operator
# 2.Comparison and Relational operator 
# 3.Assignment Operator 
# 4.Membership Operator
# 5.Identity Operators 
# 6.Logical Operator

 
# Arithmetic Operators --> are those symbols which
# are used to perform airthemtic operations.

# Arithmetic Operators in Python

# 1. +  --> Addition Operator 
# 2. -  --> Subtraction Operator 
# 3. *  --> Multiplication Operator 
# 4. / --> Division Operator 
# 5. // --> Floor Division Operator 
# 6. % --> Modulus Operator or Reminder
# 7. ** --> Exponential Operator or Power Operator.

# + Operator --> Add Two values

# a=10
# b=20 
# print(a+b)

#Output: 30

# - Operator --> Subtract Two values

# a=10
# b=20 
# print(a-b)

#Output: -10

# * Operator --> Multiply Two values

# a=10
# b=20 
# print(a*b)

#Output: 200

# ** Exponential Operator --> Power of a Number
# a=3
# b=4
# print(a**b) #==> 3**4 --> 3*3*3*3

#Output: 81


# % Modulus Operator or Reminder Operator --> Reminder of a Number.


# a=10
# b=3
# print(a%b)  #10%3

# #Output: 1


# / Division --> Quotient of a Number

# a=10
# b=5
# print(a/b) #2.0

# a=99
# b=11
# print(a/b) #2.0

# Note --> In Case of Division opertaor the result will be 
# in float only.

#Output:2.0

# //Floor Division --> After DividinG Floor Divison will give Floor value

# a=10
# b=3
# print(a//b)

# Output: 3

# a=10.0
# b=3
# print(a//b)

#Output: 3.0

# a=100
# b=25.0
# print(a//b)  #4.0

# Note --> In Case of Floor Division 
#      --> If both the operand are of integer type then
#          result will always be in the form of integer.

#      --> If atleast one operand is of float type then
#          answer will always be in the form of float.


# Comparison and Relational Operator:

# ==> This operator will always return a Boolean Value.

# > --> Greater Than Operator 
# < --> Less Than Operator
# >= --> Greater Than Equal to Operator 
# <= --> Less Than Equal To Operator
# == --> Equal to Operator 
# != --> Not Equal to Operator


#Example:

# a=10
# b=20
# print(a!=b) #True
# print(a>b) #False
# print(a<b) #True 
# print(a>=b) #False 
# # print(a<=b) #True
# # print(a==b) #False

#Note --> Comparison or Relational Operator are used in
#          Conditional Statement

#Assignment Operator --> Assign a Value to a variable,

# = --> Assignment Operator

# Example :

# a=10

# We  can Combine more than one operator with assignment
# operator(SHhrthand Notations)

# x+=10  --> x=x+10
# x-=10  --> x=x-10
# x*=10  --> x=x*10
# x//=10 --> x=x//10
# x/=10 --> x=x/10

# x=10
# x*=10 #--> #x=x*10
# print(x)

#Membership Operator --> Membership operator is
# used to check weather an element is a part of a 
# given sequence(list,string,tuple,set) or not.

#--> Return Result in form of True and False

# --> in operator  --> True if the element is present else False
# --> not in Operator --> False if the element is present else True

# x = " Python is Good"
# print(" " in x) #True
# print("p" in x) # False
# print("Python" in x) #True
# print("isa" in x) # False
# print("Good" not in x) #False
# print("Pyt" in x) #True 
# print("on is" in x) #True
# print("Pyo" in x) #False


# Identity Operator --> Return True and False 
#                   --> Identity Operators will 
# check weather the address(memory location)of two objects
# are same or not if they are same then you will get True else
# you will get answer as False

# --> is  --> Return True if both objects are same
# --> is not --> Return False if both objects are same


# x=10
# y=10
# print(id(x))
# print(id(y))
# print(x is y)

# Output:
# 1490759189008
# 1490759189008
# True

# x="Python"
# y="python"
# print(x is not y)

# Difference between == equal to operator and is Operator?

# Ans: == --> Equal to operator is used to check the content of the objects
#      is --> is used to check the address(memory location) of two object.

# x = 10.876
# y = 10.876
# print(x==y) #True 
# print(x is y) #True

# x = [10,20,30]
# y = [10,20,30]
# print(x==y) #True 
# print(x is y) #False

# Logical operators :

# and  --> Binary Operator(Two Operand)
# or   --> Binary Operator
# not  --> Unary Operator(One Operand)


# Truth Table of LOGICAL operators

# A        B        A and B         A or B    not A

# True    True        True            True    False
# False   True        False           True    True
# True    False       False           True    False
# False   False       False           False   True

# and logical operator --> if any operand is returning False then
#                          result will be False else True

# or logical operator --> if any operand is returning True then
#                          result will be True else False

# not Logical operator --> true means False and False means True                 


# Steps:

# Whatever operand is Given Convert that operand into 
# boolean and then apply logical operators but instead
# of returning True and False return Values.

# Case 1: For Non Boolean:

# x and y:
# if x evalutes as False then return x else y

# x or y:
# if x evalutes as True then return x else y

# 0,0.0,0+0j,False,[],(),{},"" ===> False
# Other than this --> True

# x = 10
# y = 20

# print(x and y) #20
# print(x or y) #10
# print(not x) #False

# x=0.0
# y=10
# print(x and y)#0.0
# print(x or y) #10
# print(not x) #True

# x = []
# y=[10,20,30]
# print( x and y) #[]
# print(x or y) #[10,20,30]
# print(not x) #True

# x = 10.5 
# y = 0.00000000000000000001
# print(x and y) #0.000000000000000001
# print(x or y )#10.5

# x = 0.00000000000000000000000000003
# y = 99
# print(x and y) #99
# print(x or y) #0.000000000000000000000000003

# x = " "
# y = "Python"
# print(x and y) #Python
# print(x or y) #" "

# Operator Procedence:

# If we have multiple operators in an expression
# then which operator will be evalued
# first will be decided by Operator Procedence.


# Procdence of Operator list:

# Opertoars                                   Meaning

# ()                                         Parenthesis 
# **                                         Exponential
# *,//,/,%                                 Division,floor division,modulus,multiplication
# +,-                                       Subtraction,Addition
# ==,!=,>,>= ...                            Comparison Operator 
# not                                        logical not 
# and                                        logical and 
# or                                         logical


# BoDMAS --> Bracket , Power,Division,modulus,fdiv,mult,add,sub... Comparsion operator

# x = 3/2*4+3+(10/5)**3-2
    # 3/2*4+3+(2.0)**3-2
    # 3/2*4+3+8.0-2
    # 1.5*4+3+8.0-2
    # 6.0+3+8.0-2
    # 17.0-2
    # 15.0.
# print(x)

x = 2*3**3*3**3
    # 2*27*3**3
    # 2*27*27
    # 54*27
    # 1458
print(x)


    

    
