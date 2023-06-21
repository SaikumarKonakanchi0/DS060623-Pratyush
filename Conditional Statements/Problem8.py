#"Write a program to accept percentage from the user and display the grade according to the following criteria:
#  Marks Grade
#  > 90 A
#  > 80 and <= 90 B
#  >= 60 and <= 80 C
#  below 60 D"

percentage = float(input("Enter Your Marks in Percentage %"))
if percentage>90 and percentage<=100:
    print("Grade A")
elif percentage>80 and percentage<=90:
    print("Grade is B")
elif percentage>70 and percentage<=80:
    print("Grade is C")
elif percentage>60 and percentage<=70:
    print("Grade is D")
elif percentage>50 and percentage<=60:
    print("Grade is E")
else:
    print("Your Grade is F You are Fail")

# Note --> If both conditions are True then and will return True
#      --> If any one condition is True then or will return True
