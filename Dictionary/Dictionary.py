# Dictionary --> If we want to store elements in the form of  
# keys and values pair then we are going to use dictionary.

# name : "Pratyush"
# batch :"DS060623"
# college : "Edyoda Digital University"

# Example:
# x = {'name' : "Pratyush",'batch' :"DS060623",'college' : "Edyoda Digital University"}

# Properties of Dictionaries:

# 1.Keys cannot be duplicate if you are giving duplicate keys then only last
#   key value pair will be considered.

# 2.Disimilar Objects are allowed for keys as well as for values. 

# 3.Indexing and Slicing concept is not possible in case of dictionary(Unordered Collection)

# 4.Dictionaries are mutable(Changeable)

# 5.Mutable objects(list,set,dict) cannot be used as a key.

# 6.Curly braces are used to represent  a dictionary and each and every
# key value pair will be seperated by :.

# Creation of Dictionary Objects:

# Empty Dictionary:


# d = {}
# d = dict()

# If you know the element:

# d={'name' : "Pratyush",'batch' :"DS060623",'college' : "Edyoda Digital University"}

# How to add Entry in a dictionary?

# Syntax:
     
#      dictionary_name[key] = value

# d={}
# d['name'] = "Pratyush Srivastava"
# print(d)
# d["batch"] = "DS0606023"
# print(d)
# d[987] = 876
# print(d)



# Output:
# {'name': 'Pratyush Srivastava'}
# {'name': 'Pratyush Srivastava', 'batch': 'DS0606023'}
# {'name': 'Pratyush Srivastava', 'batch': 'DS0606023', 987: 876}

# How to access Element inside a dictionary? 

# We can access the elements of the dictionary with the help of key

# Syntax:

#     dictionary_name[key]

# d={}
# d['name'] = "Pratyush Srivastava"
# d["batch"] = "DS0606023"
# print(d["batch"]) #DS060623
# print(d['name']) #Pratyush
# print(d["college"]) #Error

# Note --> While accessing if the given key is not present then we will 
# get key error


# How to update the value of a dictionary?

# We can update only values with the help of keys

# Syntax:
     
#      dictionary_name[key] = updated Value

# d= { 10:20,30:50,60:70}
# d[30] = "Java"
# d[30] = "C++"
# d[60] = "Python"
# print(d) #{10:20,30:"C++",60:"Python"}

# How to Delete a key value pair from a dictionary?

# If we want to delete a key value pair:
# syntax : 

#       del dictionary_name[key]


# if you want to delete whole dictionary:

# Syntax:
       
#        del dictionary_name


# if you want to delete all key value pair 

# syntax:

#      dictionary_name.clear()


# Del Keyword with a Key

# d = {"name":"Pratyush","Class":"DS0606023","College":"Edyoda Digital University"}

# del d["Class"]
# print(d) #{'name': 'Pratyush', 'College': 'Edyoda Digital University'}

# Note --> If the key is not present then you will get an error.


# Del Keyword without a Key

# d = {"name":"Pratyush","Class":"DS0606023","College":"Edyoda Digital University"}
# print(d)
# del d
# print(d)

#Output
# {"name":"Pratyush","Class":"DS0606023","College":"Edyoda Digital University"}
# NameError: name 'd' is not defined

# Clear Function --> This function will delete all key value pair from 
# dictionary

# x = {"name":"Pratyush","Class":"DS0606023","College":"Edyoda Digital University"}
# print(x)
# x.clear()
# print(x)

#Output:

# {'name': 'Pratyush', 'Class': 'DS0606023', 'College': 'Edyoda Digital University'}
# {}


# del dict_name[key] --> Specified key value pair will be deleted
# del  --> complete dictionary object will be deleted
# clear  --> Only key value pair of the dict will be deleted.



