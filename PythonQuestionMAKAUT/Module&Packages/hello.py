import sys

n=len(sys.argv) # Total command line arguments passed
print("Total arguments passed: ",n)

print("Arguments Passed: ",end=' ')
for i in range(0,n):
    print(sys.argv[i],end=' ')

print("\nName of Python Script: ",sys.argv[0])


