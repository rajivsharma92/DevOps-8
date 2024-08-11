my_list =  [3,4,2,1,2,3,4,5,5]

my_list.sort()

x = my_list

unique_list = set(my_list)


print(unique_list)

unique_list = list(unique_list)

print(unique_list)
print("Second largest number: ", unique_list[-2])
print("Largest Number: ", max(unique_list))

