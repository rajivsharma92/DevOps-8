num = int(input("ENter the number to find the factorial of it:"))
x = num
fact = 1
ans =1

while fact<=num:
    ans = ans*fact
    fact= fact+1
print("Factorial of ", x ,"is", ans)