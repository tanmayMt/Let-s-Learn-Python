def armstring(n):
    for i in range(1,n+1):
        sum=0
        temp=i
        while temp!=0:
            digit=temp%10
            sum=sum+digit**3
            temp=temp//10
        if i==sum:
            print(f"{i} ")

n=int(input("Enter the value of n: "))
armstring(n)