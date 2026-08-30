def calculate_salary(salary, bonus):
    final_salary = salary + bonus

    return final_salary

salary=int(input("Enter salary: "))
bonus=int(input("Enter bonus: "))

result = calculate_salary(salary, bonus)

print(result)
