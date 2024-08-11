def vowel_Count (string):
    count = 0
    vowels = "aeiouAEIOU"

    for char in string:
        if char in vowels:
            count = count + 1
    return count
my_string = input("Enter the line: ")

result = vowel_Count(my_string)

print("Total number of vowel in the line is: ", result)