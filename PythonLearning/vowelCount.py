new_line = input("Enter the line: ")

count = 0
vowel = "aeiouAEIOU"

#vowel_list = ["a","e","i","o","u","A","E","I","O","U"]

for char in new_line:
    if char in vowel:
        count= count+1
print("Total number of vowel:", count)