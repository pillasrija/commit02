# # write a program to sort a list of tuple using lambda
#
# subject_marks = [('english',88), ('science',90), ('maths',97), ('social science',82)]
# print("original list of tuples:")
# print(subject_marks)
# subject_marks.sort(key = lambda x: x[1])
# print("sorting the list of tuples:")
# print(subject_marks)
#
# # write a program to sort a list of dictionaries using lambda
#
# models = [{'make':'nokia','model':216,'color':'black'},{'make':'mi max','model':'2','color':'gold'},
# {'make':'samsung','model':'7','color':'blue'}] print("original list of dictionaries:") print(models) sorted_models
# = sorted(models,key = lambda x: x['color']) print("sorting the list of dictionaries:") print(sorted_models)

# write a program to filter a list of integers using lambda

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("original list of integers:")
print(nums)
print("even numbers from the said list:")
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)
print("Odd numbers from the said list:")
odd_nums = list(filter(lambda x: x % 2 != 0, nums))
print(odd_nums)

# write a program to square and cube every num in a given list of integers using lambda

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("original list of integers:")
print(nums)
print("square every number of the said list:")
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)
print("cube every number of the said list:")
cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums)

# write a program to extract year,month,date and time using lambda

import datetime
now = datetime.datetime.now()
print(now)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print(year(now))
print(month(now))
print(day(now))
print(t(now))

# write a program to rearrange positive and negative num in a given use lambda

array_nums1 = [-1,2,-3,5,7,8,9,-10]
array_nums2 = [1,2,3,4,8,9]
print("original arrays:")
print(array_nums1)
print(array_nums2)
result = list(filter(lambda x:x in array_nums1, array_nums2))
print("intersection of the said arrays:",result)