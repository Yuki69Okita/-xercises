"""
Ex. 1 - Convert input
---------------------
Take two inputs from the user.
One will be an integer.
The other will be a float number.
Then multiply them to display the output.
"""
int_num = int(input("Integer number: "))
float_num = float(input("Float number: "))
print("Result: ", int_num * float_num)


"""
Ex. 2 - Math Power
Take two numbers from the users.
Calculate the result of second number power of the first number.
"""
base_num = int(input("Base number: "))
power_num = int(input("Power number: "))
print("Result: ", base_num ** power_num)

# Second way
base_num = int(input("Base number: "))
power_num = int(input("Power number: "))
print("Result: ", pow(base_num, power_num))


"""
Ex. 3 - Create a random number
Create a random number between 0 to 10.
"""
import random
print("Result: ", random.randint(0, 10))


"""
Ex. 4 - Floor division
Find the floor division of two numbers.
"""
first_num = int(input("First number: "))
second_num = int(input("Second number: "))
print("Result: ", first_num // second_num)

# Second way
import math
first_num = int(input("First number: "))
second_num = int(input("Second number: "))
print("Result: ", math.floor(first_num / second_num))


"""
Ex. 5 - Swap two variables
The value of the first variable will become the value of the second variable.
On the other hand, the value of the second variable will become the value of the first variable.
"""
first_num = 2
second_num = 3
print(f"First value: {first_num}, Second value: {second_num}")
first_num, second_num = second_num, first_num
print(f"First value: {first_num}, Second value: {second_num}")

# Second way
first_num = 2
second_num = 3
print(f"First value: {first_num}, Second value: {second_num}")
temp = first_num
first_num = second_num
second_num = temp
print(f"First value: {first_num}, Second value: {second_num}")
