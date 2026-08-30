def check_eligibility(salary, credit_score):

    if salary >= 30000 and credit_score >= 700:
        return "Loan_approved"
    elif salary >= 30000 and credit_score >= 600:
        return "Loan under review"
    else: 
        return "Loan rejected"

salary = int(input("Enter salary: "))
credit_score = int(input("Enter credit score: "))

result = check_eligibility(salary, credit_score)

print(result)