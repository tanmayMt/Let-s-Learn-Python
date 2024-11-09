def sum_of_even_number(n):
    sum=0
    for i in range(2,n+1):
        if i%2 == 0:
            print(i,end=' ')
            sum+=i
    return sum


result=sum_of_even_number(int(input("Enter the value of n: ")))
print(f"Sum of even:{result}")    #110