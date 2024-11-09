'''
2. Write a program which has the class "circle". Use a class 
variable to define the value of constant "pi(π)".
Calculate the area and circumference of the circle with 
specified value.
'''
import math

class Circle:
    PI=math.pi  # class attribute
    
    def __init__(self,radius):
        self.radius=radius

    def cal_area(self):
        return Circle.PI*self.radius**2

    def cal_circumference(self):
        return 2*Circle.PI*self.radius



radius=int(input("Enter the value of radius: "))
c1=Circle(radius)

area=c1.cal_area()
circumference=c1.cal_circumference()

print(f"The area of the circle is {area}\nCircumference of the circle is {circumference}")