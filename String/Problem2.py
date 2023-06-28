#Python program to check weather two strings are anangram or not.

# Silent ==> Listen  --> Anangram string
# race --> care  --> Anangram String

# sorted(s1) ==>acer 
# sorted(s2) ==>acer

s1 = input("Enter String 1")
s2 = input("Enter String 2")
if sorted(s1)==sorted(s2):
    print("Anangram String")
else:
    print("Not an Anangram String")