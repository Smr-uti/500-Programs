def parking_fee_calculator(hours):

    if hours <= 0:
        return "Invalid hours"

    if hours <= 2:
        rate = 30

    elif hours <= 5:
        rate = 20

    else:
        rate = 15

    return hours * rate


hours = int(input("Enter hours: "))

result = parking_fee_calculator(hours)

print("Parking fee: ", result)