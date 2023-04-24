"""
Ex. 1 - Sum of elements
From a list get the sum of each number.
"""
sum_list = [2, 5, 6, 4, 3]
sum_num = 0

for element in sum_list:
    sum_num += element

print("Result:", sum_num)

# Second way:
sum_list1 = [2, 5, 6, 4, 3]
print("Result:", sum(sum_list1))

"""
Ex. 2 - Largest element of a list
Find the largest element of a list.
"""
larg_list = [2, 5, 6, 4, 3]
max_num = 0

for i in larg_list:
    if i > max_num:
        max_num = i

print("Result:", max_num)

# Second way:
larg_list1 = [2, 5, 6, 4, 3]
print("Result:", max(larg_list1))

"""
Ex. 3 - Sum of squares
Take a number as an input.
Then get the sum of the numbers.
"""
user_input = int(input("Please, enter a number: "))
sum_squares = 0

for i in range(user_input + 1):
    sum_squares += i ** 2

print("Result:", sum_squares)

# Second way:
user_input1 = int(input("Please, enter a number: "))
formula = user_input1 * (user_input1 + 1) * (2 * user_input1 + 1) / 6
print("Result:", int(formula))

"""
Ex. 4 - Second Largest
Find the largest element of a list.
"""
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

# Second way:
second_l_list1 = [2, 5, 6, 4, 3, 90, 37894, 908]
second_l_list1.remove(max(second_l_list1))
print("Result:", max(second_l_list1))

"""
Ex. 5 - Second smallest element
Find the second smallest element of a list.
"""
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

# Second way:
second_s_list1 = [2, 5, 6, 4, 3, 90, 37894, 908]
second_s_list1.remove(min(second_s_list1))
print("Result:", min(second_s_list1))

"""
Ex. 6 - Remove duplicate characters
For a given string, remove all duplicate characters from that string.
"""
user_string = input("Give me a string: ")
result = ""

for element in user_string:
    if element not in result:
        result += element

print("Result:", result)
