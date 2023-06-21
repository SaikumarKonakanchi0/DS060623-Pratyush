# There are Three types of statements in Python:

# 1.Conditional Statement(if-elif and else)
# 2.Iterative Statement(Loops)
# 3.Transfer Statements(Break and Continue)


# Len() Function --> Len function will return Number
# of Elements in a given sequence.

# Example:

# x = [10,20,30,40,50,60]
# print(len(x))

# x="Python is Good"
# print(len(x))

# x=(10,20,30,40,50,60,70,70,30,40,50)
# print(len(x))

# x = {10,20,30,10,10,20,30,40,506,0,30,504,0}
# print(len(x))

# x={"name":"Ayush","class":"BTEch",10:20,30:40}
# print(len(x))

# Range Function --> This function is used to Generate 
# a sequence of numbers.Range function immutable.

# 1-10 --> 1,2,3,4,5,6,7,8,9


# Range function will always three arguments:

# First Argument(Optional) --> Start Value --> Default value 0
# Second Argument --> End Value -->Mandatory (If we are giving only
#                                             one value with range function then that value will be considered as  end value) 

# Third Argument(Optional) --> Step or Gap --> Default is 1


# Syntax:
# range(start_value,end_value,step)

# end will go till end-1


#With One Argument:
x=list(range(10)) #start value is 0 ,step value is 1
print(x)

#With Two Arguments 
x=list(range(10,20)) #10,11,12,13,14,15,16,17,18,19
print(x)

#With Three Arguments 
x=list(range(10,20,2))#10,12,14,16,18
print(x)


x=list(range(10,20,4))
print(x)
