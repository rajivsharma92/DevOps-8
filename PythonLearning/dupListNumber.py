# Q8. Write a Python program to remove duplicates from a list.

myList  = [1,1,2,3,4,4,3,3,5,6,6,7,9,12,12,34,34] 

new_list = []
count  = 0

for i in myList:
    if i not in new_list : 
        new_list.append(i)

print(new_list)

# Sum of all th elements in the list

for i in new_list:
    count = count + i
print("Sum of list: " , count)