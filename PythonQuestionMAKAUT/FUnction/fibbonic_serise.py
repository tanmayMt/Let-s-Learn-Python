def fib(n):
    f=0
    s=1
    print(f"{f} {s}",end=' ')
    sum=0
    for i in range(0,n-1):
        sum=f+s
        f=s
        s=sum
        print(sum,end=" ")
l=fib(int(input("Enter the value of n: ")))