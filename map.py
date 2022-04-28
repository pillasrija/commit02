# write a program to triple all numbers of a given list of integers use python map

nums = (1,2,3,4,5,6)
print("original list: ", nums)
result = map(lambda x: x + x + x, nums)
print("Triple of said list numbers:")
print(list(result))

# write a program to add three given list use python map and lambda

num1 = [1,2,3]
num2 = [4,5,6]
num3 = [7,8,9]
print("original list: ")
print(num1)
print(num2)
print(num3)
result = map(lambda x,y,z: x + y + z,num1,num2,num3)
print("new list after adding above three lists:")
print(list(result))

# write a program to listify the list of given individually use python map

color = ['red','blue','black','white','pink']
print("original list:")
print(color)
print("after listify the list of string are:")
result = list(map(list,color))
print(result)

# write a program to power of said num in bases raised to the corresponding num in the index

bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("base numbers abd index:")
print(bases_num)
print(index)
result = list(map(pow, bases_num, index))
print("power of said number in bases raises to the corresponding number in the index:")
print(result)

# write a program to square the elements of a list using map

def square_num(n):
    return n * n
nums = [4,5,2,9]
print("original list:",nums)
result = map(square_num,nums)
print("square the elements of the said list using map():")
print(list(result))

# write a program to add two given lists and find the difference between lists use map

def addition_subtrction(x,y):
    return x + y, x - y

nums1 = [6, 5, 3, 9]
nums2 = [0, 1, 7, 7]
print("original lists:")
print(nums1)
print(nums2)
result = map(addition_subtraction,nums1,nums2)
print("result:")
print(list(result))

# write a program to convert a given list of integers and a tuple of integers in a list of strings

nums_list = [1, 2, 3, 4]
nums_tuple = (0, 1, 2, 3)
print("original list and tuple:")
print(nums_list)
print(nums_tuple)
result_list = list(map(str,nums_list))
result_tuple = tuple(map(str,nums_tuple))
print("list of strings:")
print(result_list)
print("tuple of string:")
print(result_tuple)