def count_character_in_string(input_string, char_to_count):
    str_char_list = input_string.split()
    count = 0

    for word in str_char_list:
        for single_char in word:
            if char_to_count == single_char:
                count += 1

    return count

# Take the line input
str1 = input("Enter the line: ")

# Take the character input
char_Selecter = input('Enter the character you want to count: ' )

# Call the function and store the result
count = count_character_in_string(str1, char_Selecter)

# Print the result
print(f"Number of '{char_Selecter}' in line: ", count)
