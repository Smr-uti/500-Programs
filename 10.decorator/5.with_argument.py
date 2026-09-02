def decor(func):
    def wrapper(name):
        print("Greeting started")
        func(name)
        print("Greeting completed")
    return wrapper


@decor
def greet(name):
    print("Hello: ", name)

greet("Smruti")
