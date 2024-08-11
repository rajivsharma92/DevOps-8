def are_anagrams(str1, str2):
    # Normalize the strings by converting them to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Check if lengths are the same
    if len(str1) != len(str2):
        return False

    # Sort characters of both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Compare sorted strings
    return sorted_str1 == sorted_str2

# Input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if they are anagrams
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
