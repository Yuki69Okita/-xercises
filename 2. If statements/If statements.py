"""
Ex. 1 - Max of two
Find the max number of two numbers.
"""
first_numb = int(input("First number: "))
second_numb = int(input("Second number: "))

if first_numb >= second_numb:
    print(f"Largest number is ", first_numb)
else:
    print("Largest number is ", second_numb)

# Second way:
first_numb = int(input("First number: "))
second_numb = int(input("Second number: "))

print("Largest number is ", max(first_numb, second_numb))


"""
Ex. 2 - Max of three
Find the largest of the three numbers.
"""
first_numb = int(input("First number: "))
second_numb = int(input("Second number: "))
third_numb = int(input("Third number: "))

if first_numb > second_numb and first_numb > third_numb:
    print("Largest number is ", first_numb)
elif second_numb > first_numb and second_numb > third_numb:
    print("Largest number is ", second_numb)
else:
    print("Largest number is ", third_numb)

# Second way:
first_numb = int(input("First number: "))
second_numb = int(input("Second number: "))
third_numb = int(input("Third number: "))

print("Largest number is ", max(first_numb, second_numb, third_numb))

"""
Ex. 3 - Which is weird
If  is odd, print Weird.
If  is even and in the inclusive range of  to , print Not Weird.
If  is even and in the inclusive range of  to , print Weird.
If  is even and greater than , print Not Weird.
"""
n = int(input("Enter a number: "))

if n % 2 != 0 or n in range(6, 21):
    print("Weird.")
else:
    print("Not Weird.")


"""
Ex. 4 - Is a vowel or a consonant
User needs to enter a single letter.
Then determine if that letter is a vowel or a consonant.
"""
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

# Second way
char = input("Enter a letter: ").lower()

if len(char) != 1 or not char.isalpha():
    print("Please enter one letter.")
else:
    if char in "aeiou":
        print("It's a vowel.")
    else:
        print("It's a consonant.")


"""
Ex. 5 - Taxes
User needs to enter his salary.
If the salary is bigger than $50,000 assume that tax rate will be 25%.
If the salary is less than $50,000 assume that tax rate will be 15%.
Then print the result.
"""
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
