def decor(func):
    def check_login():
        print("Checking Login...!")
        func()
        print("Login check completed")
    return check_login

@decor
def dashboard():
    print("Welcome to dashboard")

dashboard()