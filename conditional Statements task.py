#EMPLOYEE BONUS CALCULATOR
s = int(input("Enter salary: "))
exp = int(input("Enter experience: "))
if exp >= 10:
    b = s * 0.2
elif exp >= 5 and exp < 10:
    b = s * 0.1
elif exp >= 2 and exp < 5:
    b = s * 0.5
else:
    b = 0
tot_sal = s + b
print(b)
print(tot_sal)


#ATM WITHDRAWAL SYSTEM
amount=50000
pin=int(input("enter your pin number: "))
if pin==1234:
    w_amt=float(input("enter amount to withdrawal: "))
    if w_amt>0:
        if w_amt%100==0:
            if w_amt<=amount:
                balance=amount-w_amt
                print(balance)
            else:
                print("insufficient funds")
        else:
            print("entered amount must be a multiple of 100")
    else:
        print("amount must be greater than 0")
else:
    print("invalid pin")

#INCOME TAX CALCULATOR
e=float(input("enter your annual income:"))
if e<=250000:
    t=0
elif e<=500000:
    t=e*0.5
elif e<=1000000:
    t=e*0.2
else:
    t=e*0.3
remaining=e-t
print("tax amount:", t)
print("remaining income:", remaining)

#SHOPPING DISCOUNT SYSTEM
a = int(input("Enter Amount: "))
m = input("Member? y/n: ")
if m == "y":
    if a >= 10000:
        d = 20
    elif a >= 5000:
        d = 15
    elif a >= 2000:
        d = 10
    else:
        d = 0
else:
    if a >= 10000:
        d = 10
    elif a >= 5000:
        d = 5
    else:
        d = 0
d_a = a * d/ 100
final = a - d_a
print("Discount:", d)
print("Final Amount:", final)

#Driving License Eligibility
age = int(input('enter your age:'))
if age >=18:
    print('Eligible for License')
    status = input('Pass or Fail:')
    if status == 'pass':
        print('License Issued')
    else:
        print('Try again')
else:
    print('Not eligible')

#Temperature Classification
temperature = int(input("Enter temperature: "))
if temperature < 0:
    print("Freezing")
elif temperature <= 15:
    print("Very cold")
elif temperature <= 25:
    print("Cold")
elif temperature <= 35:
    print("Normal")
elif temperature <= 45:
    print("Hot")
else:
    print("Extremely hot")

#Password Strength
password = input("Enter password: ")
length = len(password)
if length < 6:
    print("Weak")
elif length <= 9:
    print("Medium")
elif length >= 10 and password.isalpha():
    print("Strong")
elif length >= 10:
    print("Very strong")
else:
    print("Invalid")

#Restaurant Bill
bill = float(input("Enter bill amount: "))
if bill >= 5000:
    discount = bill * 0.2
elif bill >= 3000:
    discount = bill * 0.15
elif bill >= 1000:
    discount = bill * 0.1
else:
    discount = 0
after_discount = bill - discount
gst = after_discount * 0.05
final_bill = after_discount + gst
print("Original bill:", bill)
print("Discount:", discount)
print("GST:", gst)
print("Final bill:", final_bill)

#E-Commerce Coupon System
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