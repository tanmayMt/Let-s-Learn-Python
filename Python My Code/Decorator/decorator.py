def decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@decorator
def greet():
    print("Hello!")

greet()
