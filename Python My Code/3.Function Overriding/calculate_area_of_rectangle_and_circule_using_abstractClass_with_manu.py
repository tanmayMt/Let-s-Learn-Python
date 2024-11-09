from abc import ABC, abstractmethod

class Shape(ABC):
  @abstractmethod
  def area(self):
    pass

class Circle(Shape):
  def area(self): # overriding area() method of Shape class
    r = float(input('Enter the radius of the circle '))
    a = 3.14 * r * r
    print('Area of the circle = ', a)
    
class Rectangle(Shape):
  def area(self): # overriding area() method of Shape class
    leng = float(input('Enter the length of the rectangle '))
    brdh = float(input('Enter the breadth of the rectangle '))
    a = leng * brdh
    print('Area of the rectangle = ', a)
    


while(True):
  print("1 :Calculate area of circle")
  print("2 :Calculate area of rectangle")
  print("3 :Exit")
  key=int(input("Enter you choice:"))

  if key==1:
    C = Circle()
    C.area()
    continue
  elif key==2:
    R = Rectangle()
    R.area()
    continue
  elif key==3:
    exit()
  else:
    print("you have enter wrong key")