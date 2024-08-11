class Employee:
    
    def __init__(self, name, salary):
        
        self.name = name

        self.salary = salary

    def get_details(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")
#Taking Employee class as master class
class Manager(Employee):

    def __init__(self, name, salary, department):

        super().__init__(name, salary)

        self.department = department

    def get_details(self):
        print(f"Employe Name: {self.name}, Salary: {self.salary}, Department: {self.department}")

employee1 = Manager('Rajiv Sharma', 2700000, "DevOps engineer")

employee1.get_details()
    