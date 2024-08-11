# # Q12. Write a Python program to find the largest and smallest numbers in a list.
# import math

# x = input(ener name)
# my_list = [1,2,3,4,5,6,7,8,9,10,2]
# """
# Easy way to get this: 

# new_list = sorted(my_list)

# print("Smallest number in list", new_list[0])
# print("largest number in my list: ", new_list[-1])

# """

# largest = my_list[0]
# smallest = my_list[0]

# for i in my_list:
#     #Update the largest number
#     if i> largest:
#         largest = i
#     #Update the smaller number
#     if i <smallest:
#         smallest = i

# print(largest, smallest)

# # second_largest = math.floor(my_list)

# # print ("THe second largest number is ", second_largest)

# print(round(1.5)-round(-1.5))

# print(':,'.format('100000'))
first_char = input("Enter the last character: ")
first = ord(first_char)
# print(first)
second_char = input("Enter the first last character: ")
second = ord(second_char)
print(type(first))


for i in range(first, second,):
    char = chr(i)
    print(char)