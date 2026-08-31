def decor(order_food):
    def wrapper():
        print("Order processing started.")
        order_food()
        print("Order processing completed...")

        
    return wrapper



def order_food():
    print("Food order placed successfully!")

wrapper=decor(order_food)
wrapper()

