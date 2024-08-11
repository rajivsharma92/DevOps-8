# Write a Python program to find the intersection of two lists.

list1 = [1,2,3,4,5,6,7]

list2 = [5,6,7,8,9,10]

intersection = []

for i in list1:
    if i in list2:
        intersection.append(i)

print(intersection)