start_value = int(input("Enter Start Value :"))
end_value = int(input("Enter End Value :"))
if start_value%2==0:
    even_numbers = list(range(start_value,end_value,2))
else:
    even_numbers=list(range(start_value+1,end_value,2))
print(even_numbers)

