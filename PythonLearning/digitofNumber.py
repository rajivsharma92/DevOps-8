num = int(input("ENter the number: "))
x = num
sum = 0

rem = 0

rev =0

while num>0:
    rem = num%10
    num = num//10
    sum = sum+rem
    rev = rev*10 + rem
    
print("Sum of number ", x, "is", sum)
print ("Reverse of the number: ", "is", rev)