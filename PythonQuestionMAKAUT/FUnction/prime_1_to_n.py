import math
def prime(n):
    for t in range(2,n+1):
        sqrt=int(math.sqrt(t))
        flag=0
        for i in range(2,sqrt+1):
            if t%i==0:
                flag=1
                break
        if flag != 1:
            print(t,end=' ')


            

num=int(input("Enter the value of n: "))
prime(num)