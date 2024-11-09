try:
    x=int(input("Enter the value of x: "))
    assert x<0
except AssertionError:
    print("Negative value in x")