# Get user input and split by commas to create lists, then convert to sets
my_set1 = set(input("Enter the elements of set1 (separated by comma): ").split(","))
my_set2 = set(input("Enter the elements of set2 (separated by comma): ").split(","))

# Find the common elements between the two sets
common_elements = my_set1.intersection(my_set2)

# Check if there are common elements and print them
if common_elements:
    print("Common elements are:", common_elements)
else:
    print("No common elements")
