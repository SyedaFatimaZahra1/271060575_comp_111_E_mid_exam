'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
'''
print("to write in file ")
n = open("my_file.txt" ,"a")
n.write("first line")
n.write("first line")
n.write("first line")
print("to read line")
n = open("my_file.txt" ,"r")
print(n.readline())
n.close()
print("to append \\ incorrect")
p=open("my_file.txt" , "a")
p.write("123")
p=open("my_file.txt" , "r")
print(p.read())
p.close()
print("to loop through file")
n=open("my_file.txt" , "r")
for item in n:
    print(item)
new = item
print(new)
print("to read specific characters")
ss = open("my_file.txt" , "r")
print(ss.read(6))
print("to read last N lines")
def LastNlines(fname, N):
    try:
        with open(fname) as file:
            for line in (file.readlines()[-N:]):
                print(line, end='')
    except FileNotFoundError:
        print('File not found')
if __name__ == '__main__':
    fname = 'my_file.txt'
    N = 1
    LastNlines(fname, N)
print(" to count nums of words")   
def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            # Replace commas without spaces with spaces
            text = text.replace(',', ' ')
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print('File not found')
        return 0
if __name__ == '__main__':
    file_path = input('Enter the path to the text file: ')
    word_count = count_words(file_path)
    print(f'Number of words in the file: {word_count}')
print("to write , append and read")
n = open("my_file.txt" ,"a")
n.write("fatima \n")
n.write("zahra \n")
n = open("my_file.txt" ,"r")
print(n.read())
print("to check if file exists")
import os
if os.path.exists("my_file.txt"):
    print("it exists")
else:
    print("not exists")
f = open("my_file.txt" ,"r")
print("to loop through file")
for x in f:
    print(x)
f = open("my_file.txt" ,"r")
con = f.readline()
print(con)
f = open("my_file.txt" ,"r")
print(f.read(9))
print("to duplicate file")
import shutil
shutil.copy('my_file.txt', 'destination.txt')
t = open('destination.txt' , "r")
print(t.read())



























