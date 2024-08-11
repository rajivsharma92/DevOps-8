num = int(input("Enter the number: "))

count = 1

sum = 0

while count<=num:
    if count%5 ==0:
        sum = sum + count
    count = count +1

print("The SUm of Number from 1 to 20 divisible by 5 is: ", sum)