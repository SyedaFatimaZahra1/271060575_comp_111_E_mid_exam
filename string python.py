#to find length
make ="pingpong"
ding = len(make)
print(ding)

#to find length using for loop
def length(string):
    count = 0
    for char in string:
        count += 1
    return count
string_input= str(input("enter a string"))
print(length(string_input))

#to count number of characters
string = str(input("enter a string"))
print("number of characters:" , len(string))

#string made of first 2 and last 2 characters
def string(new_str):
    if len(new_str) < 2:
        return" "
    else:
        return new_str[:2] + new_str[-2:]
input1 = str(input("enter string"))
print("first and last 2 char are: " , string(input1))

#to exchange first and last character
def exchange_first_and_last_chars(input_string):
    result = input_string[-1] + input_string[1:-1] + input_string[0]
    return result
user_input = input("Enter a string: ")
output_result = exchange_first_and_last_chars(user_input)
print("Result:", output_result)

#to display in upper and lower
user_input = input("Enter a string: ")
upper_case_result = user_input.upper()
print("Input in Upper Case:", upper_case_result)
lower_case_result = user_input.lower()
print("Input in Lower Case:", lower_case_result)

# to reverse string which is multiple of 4
def reverse_string_if_multiple_of_four(input_string):
    if len(input_string) % 4 == 0:
        reversed_string = input_string[::-1]
        return reversed_string
    else:
        return input_string
user_input = input("Enter a string: ")
result = reverse_string_if_multiple_of_four(user_input)
print("Result:", result)

# to check if string is palindrome
def is_palindrome(input_string):
    cleaned_string = input_string.replace(" ", "").lower()
    return cleaned_string == cleaned_string[::-1]
user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# to count occurence of all characters
def count_characters(input_string):
    char_counts = {}
    for char in input_string:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in char_counts.items():
        print(f"Character '{char}' occurs {count} times.")
user_input = input("Enter a string: ")
count_characters(user_input)

# to count vowels and consonents
def count_vowels_and_consonants(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in input_string:
        if char.isalpha(): 
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    print("Number of vowels:", vowel_count)
    print("Number of consonants:", consonant_count)
user_input = input("Enter a string: ")
count_vowels_and_consonants(user_input)

def to_count(string):
    vowel = "AEIOUaeiou"
    vowel_count = 0
    cons_count = 0
    for char in string:
        if char not in vowel :
            cons_count += 1
        else:
            vowel_count += 1
    return cons_count , vowel_count        
stri = "jdshyoutsd"
print(to_count(stri))

# to remove occurence of first char to $ except first char itself
string = input("Enter the string: ")
string = string[0] + string[1:].replace(string[0],"$")
print(string)

# to swap first two chars of each string to create new string
def chars_mix_up(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz')) 

# to add ing at end of string . if already ing then add ly(if len is 3)
def add_string(string):
    if len(string) > 2:
        if string[-3:] == "ing":
            string += "ly"
        else:
            string += "ing"
    return string
print(add_string('ab'))     
print(add_string('abc'))    
print(add_string('string'))   
# to take list of words and return longest one and its length
def longest_word():
    a_list = ["php","excercises","backend"]
    longest = a_list[0]
    for item in a_list:
        if len(item) > len(longest):
            longest = item
    return len(longest)
print(longest_word())
# orrrrrrrrrrr
s=["PHP", "Exercises", "Backend"]
a=max(s,key=len)
print(a)

# to remove chars which have odd index values
k="python"
print(k[ ::2])











