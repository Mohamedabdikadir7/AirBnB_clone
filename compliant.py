#!/usr/bin/python3
def add_numbers(num1, num2):
    """
    Add two numbers
    """
    result = num1 + num2
    return result

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Add the two numbers
sum_result = add_numbers(num1, num2)

# Print the result
print("The sum is:", sum_result)

