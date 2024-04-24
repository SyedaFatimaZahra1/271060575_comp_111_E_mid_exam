print("task 1")
matrix_a=[[1,2,3],[4,5,6],[7,8,9]]
matrix_b=[[1,2,3],[4,5,6],[7,8,9]]
output=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matrix_a)):
     for j in range((len(matrix_b[0]))):
          for k in range(len(matrix_b)):
            output[i][j]+=matrix_a[i][k] * matrix_b[k][j]
for o in output:
     print(o)
print("task 2")
lst = [3, 7, 1, 10, 5]
max_val = lst[0]  
for num in lst:
    if num > max_val:
        max_val = num  
print("Largest number in the list:", max_val)


lst = [3, 7, 1, 10, 5]
min_val = lst[0]  
for num in lst:
    if num < min_val:
        min_val = num
print("Smallest number in the list:", min_val)

def second_largest(lst):
    sorted_list = sorted(lst, reverse=True)
    if len(sorted_list) > 1:
        return sorted_list[1]
    else:
        None
my_list = [5, 3, 8, 1, 7, 2, 4]
result = second_largest(my_list)
print("Second largest num", result)


print("task 3")
row = int(input("enter num of rows"))
col = int(input("enter num of cols"))
k = []
for i in range(row):
    s=[]
    for j in range(col):
        value = int(input(f"enter the value at position{i}{j}"))
        s.append(value)
    k.append(s)
print(k)

print("task 4")
lst = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(lst[1])

lst = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
for i in range(3):
    mid_col = lst[i][3//2]
    print(mid_col)
    
print("task 6")
lst = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
sum = 0
for i in range(len(lst)):
    sum += lst[i][i]
print(sum)

total = 0
for i in range(len(lst)):
    total += lst[i][i-1]
print(total)    
        







