class Shape:
  def area(self):
    print("Area of any shape")
    
class Circle(Shape):
  def area(self): # overriding area() method of Shape class
    r = float(input('Enter the radius of the circle: '))
    a = 3.14 * r * r
    print('Area of the circle = ', a)
    
class Rectangle(Shape):
  def area(self): # overriding area() method of Shape class
    leng = float(input('Enter the length of the rectangle: '))
    brdh = float(input('Enter the breadth of the rectangle:'))
    a = leng * brdh
    print('Area of the rectangle = ', a)
    
S = Shape()
S.area()

C = Circle()
C.area()

R = Rectangle()
R.area()