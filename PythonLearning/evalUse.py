selling_price = eval(input("Enter the price of an object: "))
cost_price = eval(input("Enter the price of an Object: "))

print('-----------------------------------')

print('Selling Price = ', selling_price)

print('Cost Price = ', cost_price)

profit = selling_price - cost_price

if selling_price>cost_price:
    print("Profit = ", profit)
else:
    print('Loss = ', profit)