order = int(input("Enter order amount: "))
coupon = input("Enter coupon code: ")
if coupon == "SAVE20" and order >= 2000:
    discount = order * 0.2
elif coupon == "SAVE10" and order >= 1000:
    discount = order * 0.1
elif coupon == "WELCOME" and order >= 1500:
    discount = 200
else:
    discount = 0
final_amount = order - discount
print("Discount:", discount)
print("Final amount:", final_amount)