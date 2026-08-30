def electricity_bill(unit):

    if unit > 100:
        rate = 5
    elif unit > 200:
        rate = 7
    elif unit > 300:
        rate = 10
    else: 
        rate = 15

    bill_amount = unit * rate

    return bill_amount

unit = int(input("Enter unit: "))
# rate = int(input("Enter rate: "))

result = electricity_bill(unit)

print(result)


    
