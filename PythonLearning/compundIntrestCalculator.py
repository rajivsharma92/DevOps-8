print('---------------Compound Interest Calculator---------------')

# Input Section
principal_amount = float(input("Enter the amount to deposit: "))
original_principal_amount = principal_amount
rate_interest = float(input("Enter the current rate of interest (in %): "))
time = int(input('Enter the time (in years): '))

# Variables Initialization
compound_interest = 0

def compound_calculator(principal, rate, time):
    final_amount = principal * ((1 + (rate / 100)) ** time)
    compound_interest = final_amount - principal
    return final_amount, compound_interest

# Call the function
final_amount, compound_interest = compound_calculator(principal_amount, rate_interest, time)

# Output Section
print("--------------------------------------------------------------")
print("Principal Amount: ", original_principal_amount)
print("Rate of Interest: ", rate_interest)
print("Lock-in Period: ", time)
print("Amount with CI and Principal: ", final_amount)
print("Total Compound Interest added: ", compound_interest)
