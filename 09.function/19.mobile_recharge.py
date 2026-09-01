def mobile_recharge(amount):

    if amount < 0:
        return "Invalid Amount"
    if amount >= 500:
        cashback = 20
    elif amount >= 200:
        cashback = 10
    else:
        cashback = 5

    cashback_amount = amount * cashback / 100
    final_amount = amount - cashback_amount

    return final_amount

amount = int(input("Enter recharge amount: "))

result = mobile_recharge(amount)
print("Final amount after cashback: ", result)