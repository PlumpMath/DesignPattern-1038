class Shape:
    '''draw interface'''
    def draw(self):
        pass
    def erase(self):
        pass

class Circle (Shape):
    def __init___(self, radius=0):
        self.__radius = radius
    def draw(self):
        print "Draw Circle"
    def erase(self):
        print "Erase Circle"
    def getRadius(self):
        return self.__radius
    def setRadius(self, radius):
        self.__radius = radius

class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    def draw(self):
        print "Draw Rectangle"
    def erase(self):
        print "Erase Rectangle"
    def getWidth(self):
        return self.__width
    def setWidth(self):
        self.__height = height
    def getHeight(self):
        return self.__height
    def setHeight(self, height):
        self.__height = height
        
class ShapeFactory:
    def factory(self, which):
        if which == "Circle":
            return Circle()
        elif which == "Rectangle":
            return Rectangle()
        else:
            return None
        
fac = ShapeFactory()
shape = fac.factory("Rectangle")
if shape != None:
    shape.draw()