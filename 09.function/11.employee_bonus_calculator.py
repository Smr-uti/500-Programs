def employee_bonus_calculator(salary, experience):

    if experience >= 5:
        bonus_percentage = 20
    elif experience >=3:
        bonus_percentage = 10
    else:
        bonus_percentage = 5

    bonus = salary + bonus_percentage / 100

    return bonus

salary=int(input("Enter salary: "))
bonus=int(input("Enter bonus: "))

result = employee_bonus_calculator(salary, bonus)

print(result)