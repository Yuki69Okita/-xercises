# If statements
## Ex. 1 - Max of two
Find the max number of two numbers.

### Solution:
```python
first_numb = int(input("First number: "))
second_numb = int(input("Second number: "))

if first_numb >= second_numb:
    print(f"Largest number is ", first_numb)
else:
    print("Largest number is ", second_numb)
```
- User have to type two numbers
- When that is done with built-in "int()" function will convert string to int
- With if we compare the two numbers:
  - if first number is bigger or equal to second number
    - then prints a message
  - everything else will go in there
    - then prints a message
- If the user type something else than a number, it will raise an error

### Solution 2:
```python
first_numb = int(input("First number: "))
second_numb = int(input("Second number: "))

print("Largest number is ", max(first_numb, second_numb))
```
- User have to type two numbers
- When that is done with built-in "int()" function will convert string to int
- max(numbers/list/..) - built-in function that returns the largest number
- If the user type something else than a number, it will raise an error
--------------
## Ex. 2 - Max of three
Find the largest of the three numbers.

### Solution:
```python
first_numb = int(input("First number: "))
second_numb = int(input("Second number: "))
third_numb = int(input("Third number: "))

if first_numb > second_numb and first_numb > third_numb:
    print("Largest number is ", first_numb)
elif second_numb > first_numb and second_numb > third_numb:
    print("Largest number is ", second_numb)
else:
    print("Largest number is ", third_numb)
```
- User have to type three numbers
- When that is done with built-in "int()" function will convert string to int
- With if we compare the three numbers:
  - if first number is bigger than second and third
    - then prints a message
  - if second number is bigger than first and third
    - then prints a message
  - everything else will go in there
    - then prints a message
- If the user type something else than a number, it will raise an error

### Solution 2:
```python
first_numb = int(input("First number: "))
second_numb = int(input("Second number: "))
third_numb = int(input("Third number: "))

print("Largest number is ", max(first_numb, second_numb, third_numb))
```
- User have to type three numbers
- When that is done with built-in "int()" function will convert string to int
- max(numbers/list/..) - built-in function that returns the largest number
- If the user type something else than a number, it will raise an error
--------------
## Ex. 3 -  Which is weird
If  is odd, print Weird. <br />
If  is even and in the inclusive range of  to , print Not Weird. <br />
If  is even and in the inclusive range of  to , print Weird. <br />
If  is even and greater than , print Not Weird.

### Solution:
```python
n = int(input("Enter a number: "))

if n % 2 != 0 or n in range(6, 21):
    print("Weird.")
else:
    print("Not Weird.")

```
- User have to type a number
- When that is done with built-in "int()" function will convert string to int
- With if we compare whether there is a non-zero remainder when divided by two or number is in range between 6 and 20:
  - if whether the number have a non-zero remainder when divided by two or it is in range between 6 and 20
    - range(from, to, step) - built-in function returns a sequence of numbers
    - then prints a message
  - everything else will go in there
    - then prints a message
- If the user type something else than a number, it will raise an error
------------
## Ex. 4 - Is a vowel or a consonant
User needs to enter a single letter.
Then determine if that letter is a vowel or a consonant.

### Solution:
```python
char = input("Enter a letter: ").lower()
vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

if len(char) != 1 or char not in vowels and char not in consonants:
    print("Please enter one letter.")
else:
    if char in vowels:
        print("It's a vowel.")
    else:
        print("It's a consonant.")
```
- User have to type a character
- .lower() - built-in method where it's creating a string to lower-case
- There are two lists - one with vowels and the other with consonants
- With if we compare whether the input is one character or not in the lists: 
  - if character is not 1 or not in the lists
    - len(string/list/..) - built-in function which returns length
    - then prints a message
  - everything else will go in there
    - if character is in vowels list
      - then prints a message
    - else in consonants
      - then prints a message

### Solution 2:
```python
char = input("Enter a letter: ").lower()

if len(char) != 1 or not char.isalpha():
    print("Please enter one letter.")
else:
    if char in "aeiou":
        print("It's a vowel.")
    else:
        print("It's a consonant.")
```
- User have to type a character
- .lower() - built-in method where it's creating a string to lower-case
- With if we compare whether the input is one character or not ".isalpha()" method:
  - .isalpha() - built-in method which  returns True if all the characters are alphabet letters
  - if character is not 1 or not ".isalpha()" method
    - len(string/list/..) - built-in function which returns length
    - then prints a message
  - everything else will go in there
    - if character is in vowels string
      - then prints a message
    - else in consonants
      - then prints a message
--------------
## Ex. 5 - Taxes
User needs to enter his salary. <br />
If the salary is bigger than $50,000 assume that tax rate will be 25%. <br />
If the salary is less than $50,000 assume that tax rate will be 15%. <br />
Then print the result.

### Solution:
```python
salary = input("Enter your salary: ")

if salary.isdigit():
    salary = float(salary)

    if salary <= 0:
        print("Please enter a number bigger than 0.")
    else:

        if salary >= 50000:
            tax_rate = salary * 0.25
        else:
            tax_rate = salary * 0.15

        tax_owned = salary - tax_rate
        print(f"Because your salary is {salary}, your tax will be {tax_rate}, so that means you own {tax_owned}.")

else:
    print("Please enter a valid number.")
```
- User needs to enter his salary
- With if we compare whether the user input is digit:
  - .isdigit() - built-in method which returns True if all the characters are digits
  - Then salary is converting from string to float
    - But if it's less or equal to 0
      - print a massage
    - else calculate taxes
      - if salary is bigger or equal to $50,000
        - salary * 0.25
      - else
        - salary * 0.15
      - then calculate tax owned
      - print it in a message
  - else
    - print a message
