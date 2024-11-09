def fact(n):
    if n==0:
        return 0
    else:
        return n%10+fact(n//10)
    
num=int(input("Enter the number: "))
result=fact(num)
print(f"Sum of {num}: {result}")