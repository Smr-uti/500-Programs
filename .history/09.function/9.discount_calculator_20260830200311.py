def calculate_discount(price, discount):

    discount_amount = price * discount/100
    final_price = price - discount

    return final_price

price=float(input("Enter price: "))
discount=float(input("Enter discount: "))

result = calculate_discount(price, discount)

