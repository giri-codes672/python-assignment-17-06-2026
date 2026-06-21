#Create a Python program that takes two numbers as input from the user and performs the following operations:
user_input1 = int(input("Enter the first number: "))
user_input2 = int(input("Enter the second number: "))
#1. Addition of the two numbers
addition=user_input1 + user_input2
print("Addition of the two numbers: ", addition)
#2. Subtraction of the two numbers
subtraction=user_input1 - user_input2
print("Subtraction of the two numbers: ", subtraction)
#3. Multiplication of the two numbers       
multiplication=user_input1 * user_input2
print("Multiplication of the two numbers: ", multiplication)
#4. Division of the two numbers
division=user_input1 / user_input2
print("Division of the two numbers: ", division)
#Ensure the program handles potential division by zero errors by displaying an appropriate error message instead of crashing.
try:    
    division=user_input1 /0
    print("Division of the two numbers: ", division)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
