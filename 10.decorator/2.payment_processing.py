def decor(payment):
    def wrapper():
        print("Payment verification started")
        payment()
        print("Payment verification completed")
    return wrapper

def make_payment():
    print("Payment of 500 rupees successful..!")

wrapper=decor(make_payment)

wrapper()