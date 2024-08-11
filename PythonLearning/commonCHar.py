# Q18. Write a Python program to find the common characters between two strings.
"""
str1 = "Hello Rajiv"

str2 = "Hello Sundeep"

str3 = []

for char in str1:
    if char in str2:
        if char not in str3:
            str3.append (char)

print(str3)

"""
str1 = "Hello Rajiv".lower()
str2 = "Hello Sundeep".lower()

common_chars = []

for char in str1:
    if char in str2 and char not in common_chars:
        common_chars.append(char)

print("Common characters:", common_chars)
