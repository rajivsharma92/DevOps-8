# Q4. Write a Python program to reverse a string.
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

my_str = input("Enter the string: ")

result = reverse_string(my_str)

print("Reversed string is:", result)

if result == my_str:
    print(f"Entered Sring {my_str} is palindrome. ")
else:
    print(f"Entered Sring {my_str} is not palindrome. ")

