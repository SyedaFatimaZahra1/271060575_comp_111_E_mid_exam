# to calculate factorial
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
result = factorial(6)
print(result)
# to calculate fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n - 2)
n_terms = 23
for i in range(n_terms):
    print(fibonacci(i))
# to calculate sum of n natural numbers
def sum1(n):
    if n == 0:
        return 0
    else:
        return n + sum1(n-1)
n = 5
print(sum1(n))
# to print a list using indexing
def lst_print(n):
    if len(n) <= 1: 
        return n[0]
    else:
        print(n[0]) 
        return lst_print(n[1:])
my_list = [1, 2, 3, 4, 5]
print(lst_print(my_list))
# to sum a list using indexing
def lst_print(n):
    if len(n) <= 1: 
        return n[0]
    else:
        return n[0] + lst_print(n[1:])
my_list = [1, 2, 3, 4, 5]
print(lst_print(my_list))
# to print a list till specific num
def print_list_until(lst, stop_value):
    if not lst or lst[0] == stop_value:
        return
    else:
        print(lst[0], end=" ")
        print_list_until(lst[1:], stop_value)

lst = [1, 2, 3, 4, 5]
stop_value = 3
print_list_until(lst, stop_value)
# to print a list reversely till specific num
def print_list_until(lst, stop_value):
    if not lst or lst[-1] == stop_value:
        return
    else:
        print(lst[-1], end=" ")
        print_list_until(lst[:-1], stop_value)

lst = [1, 2, 3, 4, 5]
stop_value = 3
print_list_until(lst, stop_value)
# to calculate sum of digits    
def sum_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)
number = 12345
result = sum_digits(number)
print(result)
'''
sum_digits(12345)
= 5 + sum_digits(1234)
= 5 + 4 + sum_digits(123)
= 5 + 4 + 3 + sum_digits(12)
= 5 + 4 + 3 + 2 + sum_digits(1)
= 5 + 4 + 3 + 2 + 1  # base case is met, so it starts returning
= 15
'''
# to reverse string
def rev_str(s):
    if len(s) == 1:
        return s
    else:
        return s[-1:] + rev_str(s[:-1])
s = "tatheer"
print(rev_str(s))
'''
rev_str("hello, world")
= "d" + rev_str("hello, worl")
= "d" + "l" + rev_str("hello, wor")
= "d" + "l" + "r" + rev_str("hello, wo")
= ...  # more recursive calls
= "d" + "l" + "r" + "o" + "w" + " " + "," + "o" + "l" + "l" + "e" + "h"
'''
# to check if its palindrome
def pali(str1):
    if len(str1) == 1:
        return True
    elif len(str1) < 1:
        return True
    elif str1[0] == str1[-1]:
        return pali(str1[1:-1])
    else:
        return False
print(pali("string"))
print(pali("level"))
print(pali("levdl"))
print(pali("tit"))
# to do countdown
def count(num):
    if num == 10:
        return 10
    else:
        print(num)
        return count(num + 1)
n = 0
print(count(n))
# to do reverse countdown
def count(num):
    if num == 0:
        return 0
    else:
        print(num)
        return count(num - 1)
n = 10
print(count(n))
# to calculate greatest common divisor
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b , a % b)
result = gcd(48 , 18)
print(result)
# to calculate square
def power(n, exponent):
    if exponent == 0:
        return 1
    else:
        return n * power(n, exponent - 1)
result = power(3, 2)
print(result)
'''
Let's go through the example call power(3, 2):
The initial call is with n = 3 and exponent = 2.
Since exponent is not 0, it enters the else block:
Calculates n * power(n, exponent - 1).
Calls power(3, 1) in the recursive call.
Again, it's not the base case, so it calls power(3, 0).
Now, the base case is met (exponent == 0), and it returns 1.
The result of power(3, 1) is 3 * 1 = 3.
The result of the initial call is then 3 * 3 = 9.
'''
# to calculate cube
def power(n, exponent=1):
    if exponent == 0:
        return 1
    else:
        return n * power(n, exponent - 1)
result_general = power(3, 2)   
result_cube = power(3, 3)     
print(result_general)
print(result_cube)
# to print only even digits  
def print_even_recursive(start, end):
    if start <= end:
        if start % 2 == 0:
            print(start)
        print_even_recursive(start + 1, end)
print_even_recursive(1, 10)
'''
The initial call is with start = 1 and end = 10.
It checks if start (1) is less than or equal to end (10), which is true.
It then checks if start % 2 == 0, which is false (1 is not even), so nothing is printed.
It makes a recursive call with an incremented start value: print_even_recursive(2, 10).
This process repeats until the base case is no longer true.
When start becomes 11, the base case becomes false, and the recursion stops
'''
# to print only odd digits
def print_odd_recursive(start, end):
    if start <= end:
        if start % 2 != 0:
            print(start)
        print_odd_recursive(start + 1, end)
print_odd_recursive(1, 10)
# to print multiplication table
def multiplication_table_recursive(number, multiplier=1):
    if multiplier <= 10:
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")
        multiplication_table_recursive(number, multiplier + 1)
multiplication_table_recursive(5)

def func(a,multip):
    if multip < 1:
        return None
    else:
        result = a * multip
        print(f"{a} * {multip} = {result}")
        return func(a , multip - 1)
num = 7
multiplier = 10
print(func(num,multiplier))

 
'''
The initial call is with number = 5 and multiplier = 1.
It checks if multiplier (1) is less than or equal to 10, which is true.
It calculates and prints the multiplication expression for 5 x 1.
It makes a recursive call with the same number (5) and an incremented
multiplier value (2): multiplication_table_recursive(5, 2).
This process repeats until the base case is no longer true.
When multiplier becomes 11, the base case becomes false, and the recursion stops.
'''        
# to count occurence , tower of hanoi , binary search , merge sort 











    
