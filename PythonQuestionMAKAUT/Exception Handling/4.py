class Negative(Exception):
    def __init__(self,a):
        self.__a=a
    def get_detail(self):
        print(f"{self.__a} is a nagetive value")
try:
    b=int(input("Enter a positive value of b : "))

    if b < 0 :
        raise b
except Negative as n:
    n.get_detail()