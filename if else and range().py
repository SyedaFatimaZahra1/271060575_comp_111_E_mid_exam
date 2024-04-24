a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
x = 55
y = 110  
print("X") if x > y else print("Y")  
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
z = 10
if z<0:
    print("z is less than 0")
else:
    if z < 5:
        print("z is less than 5")
    else:
        print("z is greater than 5")
    
#range(start, stop, step)
print('''The range() function returns a sequence
of numbers, starting from 0 by default, and increments by 1
(by default), and stops before a specified number.''')      
x = range(6)
for n in x:
  print(n)
x = range(3, 6)
for n in x:
  print(n)
x = range(3, 20, 2)
for n in x:
  print(n)



























  
