str1 = input("Enter the String: ")

# To remove spaces in the string
str1 = str1.replace(" ", "")


# To reverse the str1
reverse_String = str1[::-1]

print("Reverse string: ", reverse_String)

unique_char = ""

for char in reverse_String:
    if char not in unique_char:
        unique_char = unique_char + char

print("Unique chars are: ", unique_char)
