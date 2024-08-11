str1 = input("Enter the Line: ")
str2 = input("Enter the Line: ")

for i in str1:
    if i in str2:
        print(i, end = "")

print("")