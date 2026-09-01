def calculate_result(maths, science, english):

    total_marks = maths + science + english
    percentage = total_marks / 3

    if maths < 35 or science < 35 or english < 35:
        return "Fail"

    if percentage >= 75:
        return "Distinction"
    elif percentage >= 60:
        return "First Class"
    elif percentage >= 50:
        return "Second Class"
    else: 
        return "Pass"

maths = int(input("Enter the marks for maths: "))
science = int(input("Enter the marks for science: "))
english = int(input("Enter the marks for english: "))

print("percentage: ", (maths + science + english) / 3)
result = calculate_result(maths, science, english)
print(result)