def armstring(n):
    sum=0
    temp=n
    while temp!=0:
        digit=temp%10
        sum=sum+digit**3
        temp=temp//10
    if n==sum:
        print(f"{n} is a armstrong number")
    else:
        print(f"{n} is not a armstrong number")

n=int(input("Enter the value of n: "))
armstring(n)