emplyoeeBasicSalary = eval(input("Enter the Basic Salary:" ))

hra = emplyoeeBasicSalary * 20/100

da = emplyoeeBasicSalary * 110/100

conveyance = 500

sales = eval(input("Enter the total sales: "))

if sales>= 100000:
    incentive = sales * 0.1

    total_Salary = emplyoeeBasicSalary + hra + da + conveyance + incentive + 1000

    print ("Total Salary:  ", total_Salary)

else:
    incentive = sales * 0.04
    total_Salary = emplyoeeBasicSalary + hra + da + conveyance + incentive + 500

    print ("Total Salary:  ", total_Salary)