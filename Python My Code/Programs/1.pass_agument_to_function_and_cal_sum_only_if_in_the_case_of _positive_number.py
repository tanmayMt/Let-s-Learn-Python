def sum(*agrs):
    sum=0
    for i in agrs:
        if i >= 0:
            sum=sum+i
    return sum

s=sum(2,-3,5,-2)
print(f'Sum of positive numbers: {s}')