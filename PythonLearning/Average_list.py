#Q11. Write a Python program to find the average of a list of numbers.

my_list = [1,2,3,3,4,5,6,7]

total_sum = 0

for i in my_list:
    total_sum = total_sum + i

average = float(total_sum / len(my_list))

print("Total sum of the lis is ", total_sum)

print("Average of the list is ", average)
