# As a user want to count the words in the line provide from keyboard. 
# The output should display the list of words and count of each word in the line.

str1 = input("Enter the line: ")

str_list = str1.split()

word_count = {}

for word in str_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word]= 1

for word, count in word_count.items():
    print(f"{word}: {count}")