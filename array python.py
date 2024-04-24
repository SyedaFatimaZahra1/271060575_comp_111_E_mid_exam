from array import array
arr = array('i', [1, 3, 5, 3, 7, 9, 3])
arr.insert(3, 2)  
print(arr)

arr = array('i', [1, 3, 5, 3, 7, 9, 3])
arr_count = arr.count(3)
print(arr_count)
print(arr)
print("Remove the third item form the array:")
arr.pop(2)
print(arr)
i = array("i", [3, 4, 5])
i.append(6)
print(i)
z = i[::-1]
print(z)
def median(arr):
    if not arr: 
        return "The array is empty." 
    length = len(arr)   
    if length % 2 != 0:  
        mid_index = length // 2
        return arr[mid_index]
    elif length % 2 == 0:
        first_mid_index = length // 2 - 1
        second_mid_index = length // 2
        return (arr[first_mid_index] + arr[second_mid_index])/ 2
arr1 = array('i', [4, 7, 2])  
arr2 = array('i', [3, 4, 1])
arr3 = sorted(arr1 + arr2)
print(median(arr3))
def test_duplicate(array_nums):
    nums_set = set(array_nums)    
    return len(array_nums) != len(nums_set)     
print(test_duplicate([1,2,3,4,5]))
print(test_duplicate([1,2,3,4, 4]))
print(test_duplicate([1,1,2,2,3,3,4,4,5]))

origArr = array('i',[10,11,12,13,14,16,17,18,19,20])
print("Original array: ", origArr)
print("Missing number in the said array (10-20):")
for i in range(10,20+1):
   if i not in origArr:
     print(i)
row = 2
column = 3
a = [[i*j for j in range(column)] for i in range(row)]
print(a)
from array import array
arr = array('i', [1, 3, 5, 3, 7, 9, 3])
ins = arr.insert(3,2)
print(ins)
arr = array('i', [1, 3, 5, 3, 7, 9, 3])
arr.insert(3, 2)  
print(arr)

arr = array('i', [1, 3, 5, 3, 7, 9, 3])
arr_count = arr.count(3)
print(arr_count)














