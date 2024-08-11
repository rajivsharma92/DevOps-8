# Q14. Write a Python program to find the common elements between two lists.

my_list = [1,2,10,3,4,5,6,7,8]

my_list2 = [1,1,2,3,10,5,6,7,8,9]

common =[]

# Iterate over elements in the first list
for i in my_list:
    # Check if the element is in the second list
    if i in my_list2:
        # Append the element to the common list if it's not already included
        if i not in common:
            common.append(i)

print(common)

order_list = common.sort()

print(common)