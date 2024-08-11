my_list = [1,2,3,3,5,67,89,12,34,56,67,78,89]

largest = my_list[0]

for i in my_list:
    if i>largest:
        largest = i
print(largest)