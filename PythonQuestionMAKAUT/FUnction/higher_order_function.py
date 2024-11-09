def fun1():
    print("fun1")

def my_fun(n,fun):
    print('n=',n)
    fun()

f=fun1
my_fun(4,f)
