# Q10. Write a Python program to find the length of a string.

myString = input("Enter the new String: ")
count = 0
for char in myString:
    count = count+1

print(count)


#or easy way use inbuild function or method from python
print(len(myString))