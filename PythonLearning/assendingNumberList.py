# Q20. Write a Python program to sort a list of numbers in ascending order.

my_list = [1,12,13,14,23,32,44,1,22,434]

assending_order_list= sorted(my_list)

print(assending_order_list)

# Q21. Write a Python program to count the occurrences of each element in a list.

element_Count = {}

for i in assending_order_list:
    if i in element_Count:
        element_Count[i] +=1
    else:
        element_Count [i]= 1
print (element_Count)