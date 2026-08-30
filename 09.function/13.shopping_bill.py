def shopping_bill(amount):

    if amount >= 5000:
        discount = 20
    elif amount >= 3000:
        discount = 10
    else: 
        discount = 5

    discount_amount = amount * discount / 100
    final_bill = amount - discount_amount

    return final_bill

amount = int(input("Enter amount: "))

result = shopping_bill(amount)

print(result)