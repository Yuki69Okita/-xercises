# Easy
## Ex. 1 - Convert input
Take two inputs from the user. <br />
One will be an integer. <br />
The other will be a float number. <br />
Then multiply them to display the output.

### Solution:
```python
int_num = int(input("Integer number: "))
float_num = float(input("Float number: "))

print("Result: ", int_num * float_num)
```
- You need to convert inputs to int and float because the input is always a string
- You can save the result in new variable and then print (but I didn't)
- \* - multiply operator
--------------

## Ex. 2 - Math Power
Take two numbers from the users. <br />
Calculate the result of second number power of the first number.

### Solution:
```python
base_num = int(input("Base number: "))
power_num = int(input("Power number: "))

print("Result: ", base_num ** power_num)
```
- You need to convert inputs to int because the input is always a string
- You can save the result in new variable and then print (but I didn't)
- \** - power operator

### Solution 2:
```python
base_num = int(input("Base number: "))
power_num = int(input("Power number: "))

print("Result: ", pow(base_num, power_num))
```
- You need to convert inputs to int because the input is always a string
- You can save the result in new variable and then print (but I didn't)
- pow(base, power) - built-in function
---------

## Ex. 3 - Create a random number
Create a random number between 0 and 10.

### Solution:
```python
import random


print("Result: ", random.randint(0, 10))
```
- You need to import "random" modul
- From there you can use all functions and variables you need
- You can save the result in new variable and then print (but I didn't)
- randint(from, to) - returns a number form number to number
-----------

## Ex. 4 - Floor division
Find the floor division of two numbers.

### Solution:
```python
first_num = int(input("First number: "))
second_num = int(input("Second number: "))

print("Result: ", first_num // second_num)
```
- You need to convert inputs to int because the input is always a string
- You can save the result in new variable and then print (but I didn't)
- \// - floor division operator

### Solution 2:
```python
import math


first_num = int(input("First number: "))
second_num = int(input("Second number: "))

print("Result: ", math.floor(first_num / second_num))
```
- You need to import "math" modul
- From there you can use all functions and variables you need
- You need to convert inputs to int because the input is always a string
- You can save the result in new variable and then print (but I didn't)
- floor(numb) - returns floor number of number
------------------

## Ex. 5 - Swap two variables
The value of the first variable will become the value of the second variable. <br />
On the other hand, the value of the second variable will become the value of the first variable.

### Solution:
```python
first_num = 2
second_num = 3

print(f"First value: {first_num}, Second value: {second_num}")

first_num, second_num = second_num, first_num

print(f"First value: {first_num}, Second value: {second_num}")
```
- There are two variables
- In Python, you can assign multiple variables simultaneously
- There are two "print()" functions, just to see the differences

### Solution 2:
```python
first_num = 2
second_num = 3

print(f"First value: {first_num}, Second value: {second_num}")

temp = first_num
first_num = second_num
second_num = temp

print(f"First value: {first_num}, Second value: {second_num}")
```
- There are two variables
- After that add third temporary variable (assigning first variable)
- Then assign second variable to first variable and temporary variable to second variable
- There are two "print()" functions, just to see the differences
------------------

## Ex. 6 - Sort a list
Create a list and then sort it backwards.

### Solution:
```python
ex_list = [1, 4, 9, 1, 5]
ex_list.sort(reverse=True)

print(ex_list)
```
- There is variable
- .sort() - built-in method which returns same variable but sorted
- reverse=True - keyword which is saying that the variable needs to be descending order
