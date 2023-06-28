# String --> A sequence of Characters either in single quotes,double 
# quotes or in triple quotes is known as a String.

# Example:

# x = "Python"  --> String 
# x = "10"      --> String
# x = "10.5"    --> String 
# x = "10+20j"  --> String 
# x = "True"    --> String

# How to access a Character From a String ?

# --> For Accessing any character from a string  we are having :

# 1.Indexing 
# 2.Slicing

# Indexing in String(Python)

# Indexing --> Accessing any character with the help of indexes.

# Python Supports Two Types of Indexing:

# 1.Positive --> Left to Right (Forward Direction)
# 2.Negative --> Right to Left (Backward Direction)

#[] ===> Accessing Operator 

#Note --> If index value is negative this means that it is backward indexing.
#     --> If index value is positive this means that it is forward indexing.

# Syntax of Indexing:

#       string_name[index_number]


#Note --> In Case of Forward indexing the first index will be 0 
#     --> In Case of Backward indexing the first index will be -1


# x = "Hello World"
# print(x[3]) #l
# print(x[-8]) #l
# print(x[5])  #
# print(x[-10]) #e
# print(x[-7]) #o
# print(x[-200]) #Error

#Note --> In Case of Indexing if the given index number is not present 
#         in the given string then indexing will raise index error.

#Slicing in Python

# Slicing of String --> A piece(Substring) from a string

# Syntax of Slicing:

#           string_name[begin_index : end_index : step]

# Begin_index --> From where we have to consider the slice(Substring)

# end_index(end index-1) --> Upto till which character we need to consider the slice

# gap/step --> Increment and Decrement

# Two Types of Slicing:

# 1.Forward Slicing
# 2.Backward Slicing

# Note --> Based on the Step/Gap we will decide weather we need to 
#          perform backward slicing or forward slicing.

#Forward Slicing:

# --> If the step value is positive that means forward slicing.
# --> If the begin index is not given then default value for begin index 
#     will be 0
# --> if the end index is not given then default value for end index 
#     will be len(string)-1 
# --> if the step value is not given then default value for step is 
#     1.

#Slicing will never give you an error.

# x = "Python is High Level Programming Language"

# print(x[::]) #Complete String
# print(x[2:9:2]) #to s
# print(x[10:15:4]) #H
# print(x[10:11]) #H
# print(x[10:4:4]) #Empty String
# print(x[5:1]) #Empty
# print(x[10000:20000:30000]) #Empty String
# print(x[15::5]) #Lrnne



#Backward Slicing:

# --> If the step value is negative that means backward slicing.
# --> If the begin index is not given then default value for begin index 
#     will be -1
# --> if the end index is not given then default value for end index 
#     will be -len(string)

#In case of backward slicing end will go till end+1

# x = "Python is High Level Programming Language"
# print(x[::-1]) #x[-1:-len(x):-1]  --> reverse of the string
# print(x[-2:-6:-1])#gaug
# print(x[-6:-2:-2]) #Empty String
# print(x[-150000::-1])#Empty String
# print(x[-2:-3:-1]) #g

#Miscellous Questions Related to Slicing.

# x = "Python is Good"
# print(x[1:6:-3]) #Empty String
# print(x[6:1:-2]) #ot
# print(x[-6:-2:2]) #sG
# print(x[-2:-6:1]) #Empty String
# print(x[10:15:-4]) #Empty String
# print(x[2:9:-2]) #Empty String
# print(x[1:9:-1]) #Empty

#Forward --> end-1
#Backward --> end+1

#Operators in String

# 1.Concatenation Operator 
# 2.Reptition Operator
# 3.Membership Operator
# 4.Logical Operator 
#5.Identity Operator
# 5.Relational Operator  #ASCII Value

# Concatenation Operator(+)
# ==========================
# --> This operator will help to join two strings.
# --> Both the operand must be of string type only.

# x = "Rohit "
# y = "10.5 "
# print(x+y)

#Repitition Operator(*)
# ============================
# --> This operator will repeat a given string n number of times.
# --> One operand is of int type and second is of string type.

# x = "Rohit "

# print(x*10)

#Membership Operator(in and not in)

# x = "Python is Good"
# print("P" in x) #True
# print("python" not in x) #True
# print("Pythi" in x) #False


#Identity Operator(is and is not)

# x="Python"
# y="Python"
# z="python"
# print(x is y)#True
# print(x is z) #False


#Logical Operator( and ,or and not)

# Empty string --> False 
# Rest --> True

# x = ""
# y="python"
# print(x and y) #""

# x="Hello"
# y="world"
# print(x and y)#world

# x = "10.5"
# y = "20"
# print(x or y) #10.5

# x=""
# y="Java"
# print(x or y) #Java

# x = "Python"
# print(not x)#False

# x=""
# print(not x) #True


#Traversal/Iteration in a String:

# First way:

# x="Hello World"
# for i in x:
#     print(i)

# Second Way

# x="Hello World"
# for i in range(len(x)):
#     print(x[i])

# Builtin Functions in String:

# Strip() Function ==> This function is used to remove extra whitespaces within a string.
# =================

# x="          Python is Easy              "
# print(x)
# print(x.strip())

#Find and Index Function
 
# Find and Index Both functions are used to find a substring froma string.

# find() Function ==> This function will return the first occurance of the given substring and if the substring is not present then find will return -1.

# index() Function ==> This function will return the first occurance of the given substring and if the substring is not present then find will return ValueError.

# Syntax of Index and Find Function:
        
#         string_name.find(substring,begin_index,end_index)
 
#         string_name.index(substring,begin_index,end_index)

# Begin_index and end_index both are optional if you are not giving
# begin and end index then default value will be considered.

# Default value for begin ==> 0 
# Default value for end ==> len(string)

# Example of Index Function:

# x = "Learning Python is Easy Python"
# print(x.index("Python")) #9
#print(x.index("Java")) #Value Error
#print(x.index("Learning",9,20)) #Value Error

# Example of Find Function:

# x = "Learning Python is Easy Python"
# print(x.find("Python")) #9
# print(x.find("Java")) #-1
# print(x.find("Learning",9,20)) #-1

# #Note --> The only difference between find and index function is 
# if the given substring is not present the find will return -1 and 
# index will return ValueError.


# upper(),lower(),title(),capitalize(),isupper(),islower(),isalpha,isnumeric()


# upper() Function --> Return the string in upper case.

# Example:

# x="Pratyush Srivastava"
# print(x.upper())

# # lower() Function --> Return the string in lower case.

# # Example:

# x="Pratyush Srivastava%%%%"
# print(x.lower())

# title() Function --> It will convert first letter of each word in upper case.

# Example:

# x="The hungry fox is going to the village"
# print(x.title())


#Capitalize function --> It will convert first letter of the string in upper case.

#Example

# x="the hungry fox is going to the village"
# print(x.capitalize())


# isupper() Function --> return True if all characters of the string is in upper case.


# x="The Hungry Fox is going to the village"
# print(x.isupper()) #False

#islower() function --> return True if all characters of the string is in lower case.


# x="the hungry fox is going to the village"
# print(x.islower()) #True

# x="The hungry fox is going to the village"
# print(x.islower()) #False


# isalpha --> return True if all character of the given string is an alphabet character.

# x="The hungry fox is going to the village 1099"
# print(x.isalpha()) #False

# x="IAMGOOD"
# print(x.isalpha()) #True

#isnumeric() Function --> return True if all character of the given string is an numeric Format.

# x="123"
# print(x.isnumeric()) #True


# # isdigit() function --> return True if all characaters of the given string are digits

# x="123"
# print(x.isdigit()) #True

#isalnum() function --> return True if all the characters of the given string is in form of alphanumric.

# x="ABC1234"
# print(x.isalnum())#True

# Count Function --> return the count of the given substring.

# Syntax:


# string_name.count(substring,begin_index,end_index)

# Begin index and end index will be optional if you are not giving both 
# the default values will be considered.

# Default value for begin = 0 
# Deafult value for end  =len(str)-1

# Example:

# x = "Python is Easy to Learn but Java is faster then Python"
# print(x.count("Python"))


# x="abcabcabc"
# print(x.count("bc"))#3

# x="abcabcabcabcabc"
# print(x.count("bc",5,10))#1

# x="Python is high level Programming langauge but Python is slower then Java whereas Java is much Faster then Python Overall C/C++ is the fastest Programming Language"
# print(x.count("Programming"))


# x="Python is high level Programming langauge but Python is slower then Java whereas Java is much Faster then Python Overall C/C++ is the fastest Programming Language"
# print(x.count("o"))


# replace Function --> This function will find the old substring from 
#a string and replace that substring with new substrin


# Syntax:

#  string_name.replace(old_string,new_string)

# Note --> if the old substring is not present then nothing will happen we will not get any error.

# Example:

# x="Learning Python is Easy and Python is high level as well"
# s1 = x.replace("Python","Java")
# print(s1)#Learning Java is Easy and Java is high lev

# x="Learning Python is Easy and Python is high level as well"
# s1 = x.replace("123","Java")
# print(s1) #Learning Python is Easy and Python is high lev

# x="Learning Python is Easy"
# s1 = x.replace("n","Java")
# print(s1) #LearJavaiJavag PythoJava is Easy



# Split Function ==> convert a given string into a list based on the 
# seperator value.

# x="Learning Python is Easy"
# print(x.split(" "))

# x="Learni#g Pyt#on is Ea#y"
# print(x.split("#"))

#Join() Function --> Convert list into string.

# x=["Learning","Python","is","Easy"]
# print(" ".join(x))


# x=["Learning","Python","is","Easy"]
# print("#".join(x))


# ASCII Values/UniCode Values --> 

# According to the american standard coding information interchange each 
# and every character is specified with its unquie integer value 
# that valus is known as Ascii Value.


# Each and Every character is specified with its unique value.

# Character                          ASCII Value 

# A                                      65
# B                                      66
# C                                      67
# D                                      68 
# ...
# ...
# Z                                      90

# a                                      97
# b                                      98
# c                                      99
# ...
# ...
# z                                     122



# 0                                     48
# 1                                     49
# 2                                     50
# ..
# ..                                    57

# ord function() --> This function will return the Ascii of Character.

# Syntax:
 

#       ord(Character)
# "Python"

# Note : In ord function we can pass only one character. if you are 
#       to pass multiple values or string in ord function it will
#       give you an error.

# print(ord("A"))
# print(ord("a"))
# print(ord("0"))
# print(ord("#"))
#print(ord("ABC")) #Error

# chr Function --> Based on the ASCII value if we want to fetch the character 
#                  the we are going to use char function

# print(chr(59))

#Practice Question Based on Ascii Values

# 1.Python Program to find the charcaters in upper case.

# for i in range(65,91):
#     print("Ascii Value of "+str(chr(i))+" is "+str(i))


# # 1.Python Program to find the charcaters in form of numbers.

# for i in range(48,58):
#     print("Ascii Value of "+str(chr(i))+" is "+str(i))


# # 1.Python Program to find the charcaters in lower.

# for i in range(97,123):
#     print("Ascii Value of "+str(chr(i))+" is "+str(i))

# for i in range(1,123):
#     print("Ascii Value of "+str(chr(i))+" is "+str(i))

# Sorted Function: Sort the given string in the form of asceding order or desceding order.

# On what basics characters are sorted ==> ASCII

# ==> Return answer in the form of list

# #Ascending order sorting
# x="123AratYQ" #0 - 48    , A-65    , a=97 
# print(sorted(x)) #[1,2,3,A,Q,Y,a,r]

# #Descending order sorting
# x="123AAratYQ" #0 - 48    , A-65    , a=97 
# print(sorted(x,reverse=True)) 

# Relational and Comparison Operator

# x="Python"
# y="python"
# print(x>y)#False

# x="Pzthon"
# y="Python"
# print(x>y)#True

# x = "123hELLOpYTHON"
# y = "987HelloPython"
# print(x>y)#False

# String Formatting:
x="Namish"
roll_no=98
print("My Name is "+x+" My Roll No is "+str(roll_no))
print(f"My Name is {x} My Roll No is {roll_no}")


