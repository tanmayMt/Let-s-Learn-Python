try:
    x=int(input("Enter the value of x: "))
    if x<0:
        raise ValueError
except ValueError:
    print("Negative value in x")