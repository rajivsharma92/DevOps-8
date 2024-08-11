# list = [1,2,3,4,5,6,7,1,2,3]

# #Access and modify elements

# print(list[2])
# list[2]=10
# print(list)

# # Add number to the list

# list.append(11)

# print(list)

# # Remove an index element from list

# list.remove(11) #Enter the number which you want to delete

# print(list)

# # Use list.reverse () to reverse the list data
# list.reverse()

# print (list)

# # print(list.count(1))
# list.clear()

# print(list)

# # list.extend()
# # Enter n number of element in a list
# my_list = [12]
# # n = int(input("Enter the number of elements you want in the list: "))

# # for _ in range(n):
# #     element = input("Enter an element: ")
# #     my_list.append(element)

# # print("Initial list:", my_list)

# new_elements = input("Enter elements to extend the list, separated by spaces: ").split()
# my_list.extend(new_elements)
# print("List after extending:", my_list)

my_list = []
n = int(input("Enter the total enteries you want to add in "))
for i in range(n):
    element = int(input("Enter the number: "))
    my_list.append(element)
print(my_list)