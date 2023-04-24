# Loops
## Ex. 1 - Sum of elements
From a list get the sum of each number.

### Solution:
```python
sum_list = [2, 5, 6, 4, 3]
sum_num = 0

for element in sum_list:
    sum_num += element

print("Result:", sum_num)
```
- Creating a list with random numbers
- Creating sum_num variable to save results
- for looping for each element in sum_list
- And printing the result

### Solution 2:
```python
sum_list1 = [2, 5, 6, 4, 3]
print("Result:", sum(sum_list1))
```
- Creating a list with random numbers
- Printing the result with built-in function sum()
- sum() - sums up the numbers in the list

----------------------------
## Ex. 2 - Largest element
Find the largest element of a list.

### Solution:
```python
larg_list = [2, 5, 6, 4, 3]
max_num = 0

for i in larg_list:
    if i > max_num:
        max_num = i

print("Result:", max_num)
```
- Creating a list with random numbers
- Creating variable max_num
- for looping for each element in larg_list
- If element is bigger than max_num, then max_num is equal to it
- And printing the result

### Solution 2:
```python
larg_list1 = [2, 5, 6, 4, 3]
print("Result:", max(larg_list1))
```
- Creating a list with random numbers
- Printing the result with built-in function max()
- max() - returns the largest item in an iterable

------------------------------------
## Ex. 3 - Sum of squares
Take a number as an input. <br />
Then get the sum of the numbers.

### Solution:
```python
user_input = int(input("Please, enter a number: "))
sum_squares = 0

for i in range(user_input + 1):
    sum_squares += i ** 2

print("Result:", sum_squares)
```
- Creating a variable for the user input
- Creating variable for the result
- for looping in user_input + 1 (because it's stopping before last element)
- sum_squeres is equal to it but adding every element ** 2
  - user_input = 3 => 
    - sum_squeres = 0 + 0 ** 2
    - sum_squeres = 0 + 1 ** 2
    - sum_squeres = 1 + 2 ** 2
    - sum_squeres = 5 + 3 ** 3
    - sum_squeres = 14
- And printing the result

## Solution 2:
```python
user_input1 = int(input("Please, enter a number: "))
formula = user_input1 * (user_input1 + 1) * (2 * user_input1 + 1) / 6
print("Result:", int(formula))
```
- Creating variable for the user input
- Creating variable for the math formula
- And printing the result (converting it in int because when using /, it's making it float number)

----------------------------
## Ex. 4 - Second largest element
Find the second largest element of a list.

### Solution:
```python
second_l_list = [2, 5, 6, 4, 3, 90, 37894, 908]
l_num = 0
second_l_num = 0

for i in second_l_list:
    if i > l_num:
        second_l_num = l_num
        l_num = i
    elif i > second_l_num:
        second_l_num = i

print("Result:", second_l_num)
```
- Creating a list with random numbers
- Creating two variables, one for largest number and one for second largest number
- for looping each element
- if the element is bigger than l_num
  - then make second_l_num equal to previous l_num
  - and then save l_num as element
- or if element is not bigger than l_num but element is bigger than second_l_num 
  - then save it as the element
- And printing the result

### Solution 2:
```python
second_l_list1 = [2, 5, 6, 4, 3, 90, 37894, 908]
second_l_list1.remove(max(second_l_list1))
print("Result:", max(second_l_list1))
```
- Creating a list with random numbers
- Removing maximum element with built-in functions .remove() and max()
- And printing the result with max() function
- .remove() - method that removes the specified item

-------------------------------
## Ex. 5 - Second smallest element
Find the second smallest element of a list.

### Solution:
```python
second_s_list = [2, 5, 6, 4, 3, 90, 37894, 908]
largest = 0
smallest = 0

for i in second_s_list:
    if i > largest:
        largest = i
        smallest = i

for i in second_s_list:
    if i < largest:
        smallest = largest
        largest = i
    elif largest < i < smallest:
        smallest = i


print("Result:", smallest)
```
- Creating a list with random numbers
- Creating two variables
- Those variables wil get largest element
- Then second for looping for smallest number
- it's the same logic with second largest
- And then printing the result

### Solution 2:
```python
second_s_list1 = [2, 5, 6, 4, 3, 90, 37894, 908]
second_s_list1.remove(min(second_s_list1))
print("Result:", min(second_s_list1))
```
- Absolutely the same with second largest number but with min() function

-------------------------------
## Ex. 6 - Remove duplicate characters
For a given string, remove all duplicate characters from that string.

### Solution:
```python
user_string = input("Give me a string: ")
result = ""

for element in user_string:
    if element not in result:
        result += element

print("Result:", result)
```
- Creating variable for the user input
- Creating variable for the result
- for looping in the string
- Saving each element in the result variable which is not duplicate
- And printing the result