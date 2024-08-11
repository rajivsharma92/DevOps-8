principle = eval("Enter the Principle amount:")

rate_of_intrest = eval("Enter the Rate of Interest: ")

duration_of_emi = eval("Enter the DUration of EMI in months: ") 

rate_of_intrest = eval(rate_of_intrest/(12*100)) #convert it into monthaly basis

emi = principle * rate_of_intrest * ((1+rate_of_intrest)**duration_of_emi) / ((1 + rate_of_intrest)**n -1 )

print("Monthaly emi: ", round(emi,3))
