# There are Three Types of Statements:

# 1.Conditional Statements(If elif and else)
# 2.Iterative Statements(for and while loop)
# 3.Transfer Statements(Break and Continue)

# Transfer Statements --> Transfer statement will change
# or transfer the flow of the program.

# There are Two Types of Transfer Statements in Python:

# 1.Break 
# 2.Continue

# Break Keyword --> If you are using Break keyword in your loop so 
# whenever pvm encounter break statements automatically your Loop 
# execution will be stopped or terminate.(Stopping our Loop)

# Continue Keyword --> This keyword is used to skip current iteration 
# from a loop.


# Example of Break keyword.

# Break --> Terminate or Stop your loop

# for i in range(7):
#     if i==4:
#         break 
#     print(i)

# x = [10,20,40,50,60,70,30,80,90,10,10,10,20,30]
# for i in x:
#     if i==30:
#         break
#     print(i)

#Continue --> Skip the current iteration

# for i in range(7):
#     if i==4:
#         continue
#     print(i)

# x = [10,20,40,50,60,70,30,80,90,10,10,10,20,30]
# for i in x:
#     if i==30 or i==50:
#         continue
#     elif i==20:
#         break
#     print(i)

#Nested Loop with Break and Continue


# Note --> When we are using break statement with nested loops then only 
#          one loop will be terminate with break statement. 
#      --> When we are using continue statement with nested loops then 
#          only one loop iteration will be skipped.

# for i in range(4): #0,1,2,3
#         for j in range(4): #0,1,2,3
#                 if j==2:
#                     break 
#                 print(i,j)


# for i in range(4): #0,1,2,3
#         for j in range(4): #0,1,2,3
#                 if j==2:
#                     continue
#                 print(i,j)

# for i in range(5): #0,1,2,3,4
#     for j in range(15): #0,1,..14
#         if j==2:
#             break
#         print(i,j)

# pass keyword --> The pass keyword is just a place holder for future code.
# pass means nothing is there in the block

# for i in range(10):
#     pass

if True:
    pass

