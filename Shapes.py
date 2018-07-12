# Import the math mod
import math


# Parallelogram Class
class Parallelogram:
    '''A Class to represent a parallelogram'''
    # Creat the instance variables
    def __init__(self, base, side, theta):
        '''(Parallelogram, float, float, float) -> NoneType
        This function is designed to create the instance variables for the
        class
        REQ: Base, side, and theta should be inputted as floats
        '''
        self._base = base
        self._side = side
        self._theta = theta
        self._shape = "Parallelogram"

    # Method for string output when want to print
    def __str__(self):
        '''(Parallelogram) -> str
        This function is designed to create the string output for when the
        user wants to see the shape and area
        '''
        self.area()
        area = self._area
        # Create the string output which well concatenate on after
        output = ("I am a " + self._shape + " with area " + str(area))
        # Return the output
        return output

    # Method for calculating the area
    def area(self):
        '''(Parallelogram) -> float
        This functio is designed to calculate the area of the shape
        '''
        self._area = (self._base * self._side *
                      math.sin((math.radians(self._theta))))
        # Return the area
        return self._area

    # Method for creating a list of the info
    def bst(self):
        '''(Parallelogram) -> list
        This function is designed to return a list with the inputted values
        from the user
        '''
        # Create the empty list to return
        self._listout = []
        # Put the elemements into the list
        self._listout.append(float(self._base))
        self._listout.append(float(self._side))
        self._listout.append(float(self._theta))
        # Return the list
        return self._listout


# Rhombus Class
class Rhombus(Parallelogram):
    '''A Class to represent a Rhombus'''
    # Create the instance variables
    def __init__(self, base, side, theta):
        '''(Rhombus, float, float, float) -> NoneType
        This function is designed to create the instance variables for the
        class
        REQ: Base, side, and theta should be inputted as floats
        '''
        self._base = base
        self._side = side
        self._theta = theta
        self._shape = "Rhombus"


# Rectangle Class
class Rectangle(Parallelogram):
    '''A Class to represent a Rectangle'''
    # Creat the instance variables
    def __init__(self, base, side):
        '''(Rectangle, float, float) -> NoneType
        This function is designed to create the instance variables for the
        class
        REQ: Base and side should be inputted as floats
        '''
        self._base = base
        self._side = side
        self._theta = 90
        self._shape = "Rectangle"


# Square Class
class Square(Rectangle, Rhombus):
    '''A Class to represent a square'''
    # Creat the instance variables
    def __init__(self, base, side):
        '''(Square, float, float) -> NoneType
        This function is designed to create the instance variables for the
        class
        REQ: Base and side should be inputted as floats
        '''
        self._base = base
        self._side = side
        self._theta = 90
        self._shape = "Square"
