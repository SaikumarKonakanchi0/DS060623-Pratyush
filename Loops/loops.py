# There are Three types of statements in Python:

# 1.Conditional Statement(if-elif and else)/Decision Condition
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
# x=list(range(10)) #start value is 0 ,step value is 1
# print(x)

# #With Two Arguments 
# x=list(range(10,20)) #10,11,12,13,14,15,16,17,18,19
# print(x)

# #With Three Arguments 
# x=list(range(10,20,2))#10,12,14,16,18
# print(x)


# x=list(range(10,20,4))#10,14,18
# print(x)


# Iterative Statement ==> When we want to execute
# a group of statements multiple times then we 
# are going to use Iterative Statements.


# Suppose we want to print hello world 1000 times
# so for this we are having two approches:
    
# 1.We can write hello world 1000times


# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")

# 2.We can use loop

# for i in range(1,20):
#     print("HEllo world")

# Note --> With the help of loop we can easily print
# hello world 1000 times by writing only two lines of Code but if we are using 
# first approach then we need write 1000 lines and all 
# lines are repeated which is not feasible in any 
# programming language thatswhy we prefer 
# iterative statements to execute a group of statements 
# multiple times.


# In python Two types of loops are There:

# 1.FOR Loop 
# 2.While Loop 

# Note --> In python we don't have any do while loop


# FOR Loop:
# ==========
# --> If we want to execute a number of statement in some sequence 
# then we are going to use for loop.


# Sequence --> List,Tuple,Set,Dictionary,String,Range

# Syntax:

# for i in sequence:
#     stmt-1
#     stmt-2
#     stmt-3

# i is known as Iterator

# The value of Iterator is changing based on the given sequence.


# Nested Loop -->

# Loop Inside Loop is known as Nested Loops


# Note --> Once all iteration of the inner loop 
# will be completed then pointer will come for 
# next iteration  of outer loop.

# For each iteration of Outer loop Complete inner Loop 
# will be executed

# Syntax:

# for i in sequence:
#     for j in sequence:
#         body/sequence