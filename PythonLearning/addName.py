my_list = []

choose = input("Want to the Name: ").lower()
while choose == "yes":

        name= input("Enter the name: ")
        my_list.append(name)

        choose = input("Want to the Name: ").lower()

print("Thanks you for the inputs")
print(my_list)