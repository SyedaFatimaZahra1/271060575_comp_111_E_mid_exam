
# to find factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
user_input = int(input("Enter a non-negative integer: "))
if user_input < 0:
    print("Please enter a non-negative integer.")
else:
    result = factorial(user_input)
    print(f"The factorial of {user_input} is: {result}")
    
#to reverse number
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return reversed_num
user_input = int(input("Enter a number: "))
result = reverse_number(user_input)
print(f"The reversed number is: {result}")

#to print number in descending order
def print_descending_natural_numbers(n):
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        i = n
        while i >= 1:
            print(i, end=" ")
            i -= 1
user_input = int(input("Enter a positive integer (n): "))
print_descending_natural_numbers(user_input)

#to print multiplication table
def print_multiplication_table(number):
    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")
user_input = int(input("Enter a number to get its multiplication table: "))
print_multiplication_table(user_input)

#to print first ten natural numbers
num = 1
while num <= 10:
    print(num, end=" ")
    num += 1
    
#to find specific numbers that are divisible by 7 and 
# multiples of 5 between 1500 and 2700 (both included)
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num, end=" ")
rows = 5
for i in range(1, rows + 1):
    print("* " * i)
for i in range(rows - 1, 0, -1):
    print("* " * i)
    
#to count number of even and odd elements
numbers = input("Enter a series of numbers separated by spaces: ")
number_list = [int(num) for num in numbers.split()]
even_count = 0
odd_count = 0
for num in number_list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")

#to skip specific numbers
for num in range(7):
    if num != 3 and num != 6:
        print(num)
        
#to get fibonacci seq b/w 0 & 50
a, b = 0, 1
while a <= 50:
    print(a, end=" ")
    a, b = b, a + b
    
#to calculate num of digit and letters
def count_digits_and_letters(input_string):
    digit_count = sum(char.isdigit() for char in input_string)
    letter_count = sum(char.isalpha() for char in input_string)

    print(f"Number of letters: {letter_count}")
    print(f"Number of digits: {digit_count}")
user_input = input("Enter a string and number mix: ")
count_digits_and_letters(user_input)

#to display prime numbers withing specified range
start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
#to display fibonacci series upto 10 terms
num1, num2 = 0, 1
print("Fibonacci sequence:")
for i in range(10):
    print(num1, end="  ")
    res = num1 + num2
    num1 = num2
    num2 = res
#to calculate cube of numbers to a specified range
input_number = 6
for i in range(1, input_number + 1):
    print("Current Number is :", i, " and the cube is", (i * i * i))
#to print pattern
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
#to print 0 to 6 except 3 and 5
for i in range(7):
    if i != 3 and i != 5:
        print(i)
#to check vowel or consonent
letter = input("Enter a single letter: ").lower()
if len(letter) == 1 and letter.isalpha():
    if letter in 'aeiou':
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")
else:
    print("Invalid input. Please enter a single letter.")        
#to print first 10 even nums in reverse order
for i in range(20, 0, -2):
    print(i)    
#to find average
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
if len(numbers) > 0:
    average = sum(numbers) / len(numbers)
    print(f"The average is: {average}")
else:
    print("No numbers entered. Cannot calculate average.")
#to find greatest common divisor of 2 nums
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")    
#to find HCF of 2 nums
def hcf(a, b):
    while b:
        a, b = b, a % b
    return a
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = hcf(num1, num2)
print(f"The HCF of {num1} and {num2} is: {result}")
#to check palindrome
def is_palindrome(word):
    word = word.lower()
    start, end = 0, len(word) - 1    
    while start < end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1    
    return True
user_input = input("Enter a word: ")
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
#to guess the number
import random
def guess_the_number():
    secret_number = random.randint(1, 100)    
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")    
    attempts = 0    
    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
guess_the_number()
#to print sq.root from 1 to 10
for i in range(1, 11):
    square_root = i ** 0.5
    print(f"The square root of {i} is: {square_root}")

#to check validity of password inputted
'''
'''
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
'''
'''
while True:
    password = input("Enter a password: ")

    if 6 <= len(password) <= 16:
        if any(c.islower() for c in password):
            if any(c.isupper() for c in password):
                if any(c.isdigit() for c in password):
                    if any(c in ['$','#','@'] for c in password):
                        print("Valid password")
                        break
                    else:
                        print("Password must contain at least one of $, #, or @")
                else:
                    print("Password must contain at least one digit")
            else:
                print("Password must contain at least one uppercase letter")
        else:
            print("Password must contain at least one lowercase letter")
    else:
        print("Password must be between 6 and 16 characters")

#https://csiplearninghub.com/practice-questions-of-loops-in-python/



practice = 1


# product of digits
num = 6
p = 1
while num > 0:
    rem = num % 10
    p = p * rem
    num = num // 10
print("sum is " , p)

# to get factorial
f = 1
for i in range(6 ,0 , -1):
    f = f * i
print(f)

# to check prime number
def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # Number is divisible by a factor, so it's not prime
    return True  # If no factors are found, the number is prime
num_to_check = 17
if is_prime(num_to_check):
    print(f"{num_to_check} is prime")
else:
    print(f"{num_to_check} is not prime")

# 10 num input and their average    
s=0
for i in range(10):
    num = int(input("enter num"))
    s= s + num
print("average is " , s/num)

# to check prime
for num in range(2, 51):
    is_prime = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")

#  to print sum of even and odd b/W range      
so = 0
se = 0
for i in range(12,38):
    if i % 2 == 0:
        se = se + i
    else:
        so = so + i
print("odd" , so)
print("even" , se)

# to print num dic by 11 and not 2
for num in range(100,501):
    if num % 11 == 0 and num % 2 != 0 :
        print(num)

#  to print num except multiple of 3 and 2      
for num in range(1,21):
    if num % 3 != 0 and num % 2 != 0:
        print(num)

# to print average and sum       
num = 1
i = -1
s = 0
while num != 0:
    num = int(input("enter num(0 to exit)"))
    s = s + num
    i = i + 1
print("average is" , s/i)           
print("sum is" , s)

#  to find armstrong number
for num in range(100, 501):
    num_str = str(num)
    armstrong_sum = sum(int(digit) ** 3 for digit in num_str)
    if armstrong_sum == num:
        print(f"{num} is an Armstrong number.")

#  to reverse digits of number
number = int(input("Enter a number: "))
number_str = str(number)
reversed_number_str = number_str[::-1]
reversed_number = int(reversed_number_str)
print(f"The reversed number is: {reversed_number}")

#  to reverse word
word = input("Enter a word: ")
reversed_word = word[::-1]
print("Reversed word:", reversed_word)

# get cube of all within specified range
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
for num in range(start_range, end_range + 1):
    cube = num ** 3
    print(f"The cube of {num} is: {cube}")

# to find GCD/HCF
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result_gcd = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result_gcd}")

# to guess num
magic_num = 4
while True:
    n = int(input("Enter a guess between 1 and 9: "))
    if n > magic_num:
        print("Too big")
    elif n < magic_num:
        print("Too small")
    else:
        print(f"Well guessed! {n} is the correct number.")
        break  
# to to count even and odd
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)

# to skip specific nums
for num in range(0 , 7):
    if num == 3 or num == 6 :
        continue
    else:
        print(num)

# to skip and print specific shit
for num in range(1,51):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 5 == 0:
        print("buzz")
    elif num % 3 == 0:
        print("fizz")
    else:
        print(num)

# to print all sentences netered in lowercase
sentences = []
while True:
    sentence = input("Enter a sentence (or press Enter to finish): ")
    if not sentence:
        break
    sentences.append(sentence.lower())
print("\nSentences in lowercase:")
for sentence in sentences:
    print(sentence)

# to count letter an ddigits in a string
input_string = input("Enter a string: ")
digit_count = 0
letter_count = 0
for char in input_string:
    if char.isdigit():
        digit_count += 1
    elif char.isalpha():
        letter_count += 1
print("Number of digits:", digit_count)
print("Number of letters:", letter_count)

# to print sum with specifc instructions
def sum_or_twenty(num1, num2):
    result = num1 + num2
    if 15 <= result <= 20:
        return 20
    else:
        return result
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
result = sum_or_twenty(num1, num2)
print(f"The sum (or 20 if between 15 and 20) is: {result}")

# to find median of three nums
def find_median(num1, num2, num3):
    if num1 <= num2 <= num3 or num3 <= num2 <= num1:
        return num2
    elif num2 <= num1 <= num3 or num3 <= num1 <= num2:
        return num1
    else:
        return num3
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
median = find_median(num1, num2, num3)
print(f"The median is: {median}")

dsjfskjg
    







