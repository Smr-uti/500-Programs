def decor(func):
    def wrapper():
        print("Welcome process started")
        func()
        print("Welcome process completed")
    return wrapper

@decor
def welcome():
    print("Welcome to Python...!")

welcome()