product_price = eval(input("Enter the prcie of the product: "))
cgst_rate = eval(input("Enter the CGST rate  "))
sgst_rate = eval(input("Enter the SGST rate  "))

cgst_price = product_price * (cgst_rate / 100)

sgst_price = product_price * (sgst_rate / 100)

gst_total =  cgst_price+ sgst_price

product_price_gst = product_price + gst_total

print ("-----------------")
print("Product Price: ", product_price_gst)

print("CGST: ", cgst_price)

print("SGST: ", sgst_price)

print(15+20/5+3*2-1)