#Python program to check weather a given string is palindrome or not
# Original_String==Revere_String

# MADAM==> MADAM

string_1 = input("Enter a String :")
if string_1 == string_1[::-1]:
    print("Palindrome String")
else:
    print("Not Palindrome String")