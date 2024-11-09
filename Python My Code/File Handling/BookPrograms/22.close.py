f=open("20.demo","r")
buf=f.read()
print("buf: ",buf)
f.close()


buf1=f.read() # Hare we want to read a file which is already closed.
              # So this will give an error.
print("buf1: ",buf1)