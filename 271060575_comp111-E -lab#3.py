print("task 1")
def hailstone(n):
    hail = [n]
    if n == 1:
        return hail
    
    if n % 2 == 0:
        res = hailstone(n // 2)
        hail.extend(res)
        return hail
    
    elif n % 2 != 0:
        res =  hailstone((n * 3) + 1)
        hail.extend(res)
        return hail
    hail.extend(n)
n = int(input("enter num "))
print(hailstone(n))

print("task 4")
def new_str(s, start, stop):
    if start > stop :
        return " "
    else:
        return s[start] + new_str(s, start + 1 , stop)
s = "pingpong"
start = 2
stop = 6
print(new_str(s,start,stop))







