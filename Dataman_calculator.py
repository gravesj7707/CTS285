# -*- coding: utf-8 -*-
"""
Created on Mon Oct 2 17:45:00 2023
@author: Brittany and Justin
"""
from flask import Flask

# Initialize memory bank
memory = 0

# Dictionary to store user credentials
user_credentials = {}

# Function to create an account
def create_account():
    username = input("Enter your username: ")
    if username in user_credentials:
        print("Username already exists. Please choose a different username.")
        return

    password = input("Enter your password: ")
    user_credentials[username] = password
    print("Account created successfully.")

# Function to log in
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in user_credentials and user_credentials[username] == password:
        print("Login successful.")
        return True
    else:
        print("Login failed. Please try again.")
        return False

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

# Menu to select operation, main calculator loop
while True:
    print("Select operation:")
    print("1. Create Account")
    print("2. Log In")
    print("3. Add")
    print("4. Subtract")
    print("5. Multiply")
    print("6. Divide")
    print("7. Memory Recall")
    print("8. Clear Memory")
    print("9. Exit")

    choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

    if choice == '9':
        print("Calculator exiting...")
        break

    if choice == '1':
        create_account()
    elif choice == '2':
        login()
    elif not user_credentials:
        print("You need to create an account or log in first.")
    else:
        if choice == '3' or choice == '4' or choice == '5' or choice == '6':
            try:
                # Non-numeric inputs
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter valid numerical value.")
                continue

            # Perform selected operation based on user's choice.
            if choice == '3':
                result = add(num1, num2)
            elif choice == '4':
                result = subtract(num1, num2)
            elif choice == '5':
                result = multiply(num1, num2)
            elif choice == '6':
                result = divide(num1, num2)

            # Display result and update memory
            print("Result:", result)
            memory = result
        elif choice == '7':
            print("Memory Recall:", memory)
        elif choice == '8':
            memory = 0
            print("Memory Cleared.")
        else:
            print("Invalid choice")
