import json

class Complex:
    def __init__(self,r=0,i=0):
        self.real=r
        self.imag=i
    def print_data(self):
        print(self.real,self.imag)

def encode_complex(x):
    if isinstance(x,Complex):
        return x.real,x.imag
    else:
        raise TypeError("Complex objecte is not JSON serializable")

def decode_complex(dct):
    if '_Complex_' in dct:
        return Complex(dct['real'],dct['image'])
    else:
        dct

c=Complex(1.0,2.0)
# c.print_data()

f=open("3.demo","w+")
json.dump(c,f,default=encode_complex)

f.seek(0)

inc=json.load(f,object_hook=decode_complex)
print(inc)