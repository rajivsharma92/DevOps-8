new_string = input("Enter you input: ")

print(new_string)

rev_string = new_string[::-1]

print(rev_string)

if rev_string == new_string:
    print("String is a palindrome")
else:
    print("Not a palindrome ")