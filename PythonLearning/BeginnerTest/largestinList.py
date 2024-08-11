# Q6. Write a Python program to find the largest number in a list.

def largest_list(list):
    largest = 0
    for i in list:
        if largest<i:
            largest =i
    return largest

my_list = [2,1,3,4,5,1,12,14,23,45,23,34,90]

result = largest_list(my_list)

print("The largest in list is", result)
