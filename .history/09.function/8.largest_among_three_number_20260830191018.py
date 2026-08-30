def largest_numbers(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

a=int(input("Enter first number: "))
b=int(input("Enter first number: "))
c=int(input("Enter first number: "))

result = largest_numbers(a, b, c)



