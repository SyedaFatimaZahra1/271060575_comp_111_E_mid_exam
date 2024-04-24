#to make list
thislist = ["apple", "banana", "cherry"]
print(thislist)
# to find length(starts at 0)
print(len(thislist))
# list can have diff data types
list1 = ["abc", 34, True, 40, "male"]
# to find type of data
print(type(thislist))
print(type(list1))
'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''
# to slice index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[-4:-1])
# to check presence
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
# to change value
thislist[1] = "blackcurrant"
print(thislist)
# to change value in range 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
# to use insert()[add item at specified position]
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
# to use append()[add item at end]
numbers = [21, 34, 54, 12]
numbers.append(32)
print("After Append:", numbers)
# to use extend()[add another list or any iterable]
numbers = [1, 3, 5]
even_numbers = [4, 6, 8]
numbers.extend(even_numbers)
print("List after append:", numbers) 
# to use del()[delete the specified]
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
del languages[1]
print(languages)
# to use remove()[removes the specified element]
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
languages.remove('Python')
print(languages) 
# to use pop()[deletes at specified value]
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# to use clear()[deletes all items]
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
# to use reverse()[reverses order]
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
# to use copy()[makes copy of the list]
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
# to apply for loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
# to apply while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
# to loop through index numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])  
# to loop using list comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
# to use sort(alphanumerically ascending by default , also its case sensitive)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# to sort by descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
# to Sort the list based on how close the number is to 50:
def myfunc(n):
    return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
# to combine lists(1st method)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
# to combine lists by append()[2nd method]
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)
# to turn every list item into square(1st way)  
numbers = [1, 2, 3, 4, 5, 6, 7]
res = []
for i in numbers:
    res.append(i * i)
print(res)
# to turn every list item into square(2nd way) 
numbers = [1, 2, 3, 4, 5, 6, 7]
res1 = [x * x for x in numbers]
print(res1)
# to iterate two lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x, y in zip(list1, list2[::-1]):
    print(x, y)   
# to remove empty string from list of string
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
res = list(filter(None, list1))
print(res)
# to add new item to list after a specified item
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# understand indexing
# list1[0] = 10
# list1[1] = 20
# list1[2] = [300, 400, [5000, 6000], 500]
# list1[2][2] = [5000, 6000]
# list1[2][2][1] = 6000
# solution
list1[2][2].append(7000)
print(list1)
# to replace list item with a new value if found
list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)
list1[index] = 200
print(list1)
# to remove all occurence of a specific item in list
list1 = [5, 20, 15, 20, 25, 50, 20]
while 20 in list1:
    list1.remove(20)
print(list1)
# to sum all items in a ist
my_list = [1, 2, 3, 4, 5]
total_sum = 0
for num in my_list:
    total_sum += num
print("Sum of the list:", total_sum)
# to multiply all items in a list
my_list = [1, 2, 3, 4, 5]
total_product = 1
for num in my_list:
    total_product *= num
print("Product of the list:", total_product)
# to get largest number
my_list = [3, 7, 1, 10, 5]
max_value = my_list[0]  
for num in my_list:
    if num > max_value:
        max_value = num
print("Largest number in the list:", max_value)
# to get smallest number
my_list = [3, 7, 1, 10, 5]
min_value = my_list[0]  
for num in my_list:
    if num < min_value:
        min_value = num
print("Smallest number in the list:", min_value)
# to remove duplicates from list
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for num in original_list:
    if num not in unique_list:
        unique_list.append(num)
print("List with duplicates removed:", unique_list)
# to check if list is empty
my_list = []
if not my_list:
    print("The list is empty.")
else:
    print("The list is not empty.")   
# to take 2 list as input and return True if they have common member
def have_common_member(list1, list2):
    return any(item in list1 for item in list2)
list_a = [1, 2, 3, 4, 5]
list_b = [5, 6, 7, 8, 9]
result = have_common_member(list_a, list_b)
if result:
    print("The lists have at least one common member.")
else:
    print("The lists do not have any common members.")
# to print list after removing even numbers
def remove_even_numbers(input_list):
    odd_numbers = [num for num in input_list if num % 2 != 0]
    return odd_numbers
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_list = remove_even_numbers(original_list)
print("List after removing even numbers:", result_list)
# to print list after removing odd numbers
def remove_odd_numbers(input_list):
    even_numbers = [num for num in input_list if num % 2 == 0]
    return even_numbers
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_list = remove_odd_numbers(original_list)
print("List after removing odd numbers:", result_list)
# to check if each number is prime in list . return True if all are
# 1st way (to print only prime ones)
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
my_list = [1, 2, 4, 5, 6, 7]
result = []
for num in my_list:
    result.append(is_prime(num))
print(result)
# 2nd way (to print msg if all are prime nums)
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
my_list = [1, 2, 4, 5, 6, 7]
all_primes = all(is_prime(num) for num in my_list)
if all_primes:
    print("All numbers are prime.")
else:
    print("Not all numbers are prime.")
# to access index of a list
my_list = [10, 20, 30, 40, 50]
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")
# to append list to a second list
   # Using extend()
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print("List1 after extending:", list1)
    # Using +=
list3 = [7, 8, 9]
list1 += list3
print("List1 after += operation:", list1)
# to find second smallest number
def second_smallest(input_list):
    sorted_list = sorted(input_list)
    return sorted_list[1] if len(sorted_list) > 1 else None
my_list = [5, 3, 8, 1, 7, 2, 4]
result = second_smallest(my_list)
print("Second smallest number:", result)
# to find second largest number
def second_largest(input_list):
    sorted_list = sorted(input_list, reverse=True)
    return sorted_list[1] if len(sorted_list) > 1 else None
my_list = [5, 3, 8, 1, 7, 2, 4]
result = second_largest(my_list)
print("Second largest number:", result)
# to convert string into list
my_string = "Hello, World!"
char_list = list(my_string)
print("List of characters:", char_list)
# to find average of all list elements
numbers = []
for i in range(20):
    num = int(input("Enter number {}: ".format(i + 1)))
    numbers.append(num)
total = sum(numbers)
average = total / len(numbers)
print("Average of the list:", average)
# to take 20 inputs from user and store them in list
numbers = []
for i in range(20):
    num = int(input("Enter number {}: ".format(i + 1)))
    numbers.append(num)
print("List of numbers:", numbers)
# to Take 20 integer inputs from user and print the following:
#number of positive numbers
#number of negative numbers
#number of odd numbers
#number of even numbers
#number of 0s
# Initialize counters
positive_count = 0
negative_count = 0
odd_count = 0
even_count = 0
zero_count = 0
for _ in range(20):
    num = int(input("Enter an integer: "))
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    if num == 0:
        zero_count += 1
print("Number of positive numbers:", positive_count)
print("Number of negative numbers:", negative_count)
print("Number of odd numbers:", odd_count)
print("Number of even numbers:", even_count)
print("Number of zeros:", zero_count)

