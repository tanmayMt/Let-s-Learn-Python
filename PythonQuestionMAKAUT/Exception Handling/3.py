try:
    x=int(input("Enter the value of x: "))
    if x<0:
        raise ValueError('Negative value in x')
    print(x, " is a nagrtive number")
except ValueError:
    print(ValueError.args)