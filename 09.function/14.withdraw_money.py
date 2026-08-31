def withdraw_money(balance, amount):
    if amount > balance:
        return "Insufficient balance"
    elif amount <= balance:
        return "Invalid amount"
    