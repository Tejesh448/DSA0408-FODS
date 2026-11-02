prices = [100, 200, 150, 50]
quantities = [2, 1, 3, 2]

discount_rate = 10
tax_rate = 5
total = 0

for i in range(len(prices)):
    total += prices[i] * quantities[i]

discount = total * discount_rate / 100

amount = total - discount

tax = amount * tax_rate / 100

final_amount = amount + tax

print("Total Amount:", total)
print("Discount:", discount)
print("Amount After Discount:", amount)
print("Tax:", tax)
print("Final Amount:", final_amount)
