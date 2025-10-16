name=input("Enter customer name: ")
mobile=input("Enter mobile number: ")
cost=float(input("Enter cost of purchase: "))
discount=cost*0.1  # 10% discount
total=cost-discount
print(f"Customer Name: {name}\nMobile Number: {mobile}\nCost: {cost}")
print(f"Discount: {discount}\nTotal Amount to be Paid: {total}")
