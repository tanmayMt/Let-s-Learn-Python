class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def __add__(self,other):
        self.real = self.real + other.real
        self.imag = self.imag + other.imag
        return self.real,self.imag