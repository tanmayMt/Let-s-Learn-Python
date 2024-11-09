import math
def prime(n):
    if n==1:
        print(f"{n} is not a prime number")
        exit(1)
    else:
        sqrt=int(math.sqrt(n))
        flag=0
        for i in range(2,sqrt+1):
            if n%i == 0:
                flag=1
                break
    if flag == 1:
        print(f"{n} is not a prime number")
    else:
        print(f"{n} is a prime number")

num=int(input("Enter the value of n: "))
prime(num)