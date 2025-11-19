#Project 2: Shapes Class Hierarchy

import abc
import math
from multiprocessing import Value
from os import name
from re import X

class basicShape(abc.ABC):
    def __init__(self, name: str):
        self._area: float = 0.0
        self._name: str = name

    #getters/setters:
    @property
    def area(self) -> float:
        return self._area

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name
    #abc to calc shape area:
    @abc.abstractmethod
    def calc_area(self) -> None:
        pass

class circle(basicShape):
    #circle shape, area = pi*r^2;
    def __init__(self, x: float, y: float, r: float, n: str = "Circle"):
        super().__init__(n)
        self._xcenter: float = x
        self._y_center: float = y
        self._radius: float = r

        self.calc_area()
    def calc_area(self) -> None:
        self._area = math.pi*(self._radius**2)
    #getter/setters:
    @property
    def x_center(self) -> float:
        return self._x_center

    @property
    def y_center(self) -> float:
        return self._y_center

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, new_radius: float):
        if new_radius >0:
            self._radius = new_radius
            self.calc_area()
        else:
            raise ValueError("Radius has to be positive.")

class rect(basicShape):
    #rectangle shape, area=l*w;
    def __init__(self, l: float, w: float, n: str = "Rectangle"):
        super().__init__(n)
        self._length: float = l
        self._width: float = w

        self.calc_area()

    def calc_area(self) -> None:
        self._area = self._length * self._width

    #getter/setters:
    @property
    def length(self) -> float:
        return self._length
    @length.setter
    def length(self, new_length: float):
        if new_length >0:
            self._length = new_length
            self.calc_area()
        else:
            raise ValueError("Length must be positive!")

    @property
    def width(self) -> float:
        return self._width
    @width.setter
    def width(self, new_width: float):
        if new_width > 0:
            self._width = new_width
            self.calc_area()

        else:
            raise ValueError("Width must be positive!")


class squ(rect):
    def __init__(self, s: float, n: str = "Square"):
        self._side: float = s
        #using rect constructor thru super:
        super().__init__(l=s, w=s, n=n)
        #using basicshape property setter for name just in case:
        self.name = n

        #calc_area inherited from rectangle!

    @property
    def side(self) -> float:
        return self._side
    @side.setter
    def side(self, new_side: float):
        if new_side > 0:
            self._side = new_side
            self.length = new_side
            self.width = new_side
        else:
            raise ValueError("Side must be positive!")



#test program:
def run_test_program():
    print("\nRunning test program for shapes:")

    shapes = []

    recta_1 = rect(l=10, w=20, n="Recta_1")
    recta_2 = rect(l=30, w=20, n="Recta_2")

    circ_1 = circle(x=0, y=0, r=4, n="circ_1")
    circ_2 = circle(x=1, y=1, r=9, n="circ_2")

    squa_1 = squ(s=10, n = "squ_1")

    shapes.extend([recta_1, recta_2, circ_1, circ_2, squa_1])

    print("Polymorph testing:")
    for shape in shapes:
        print(f"{shape.name} Area = {shape.area:.5f}")

    print("\nModification/verification testing:")
    #CIRCLE:
    c1_test = circ_1
    orig_rad = c1_test.radius

    print(f"{c1_test.name} Current: {c1_test.radius}{c1_test.area:.5f}")
    #radius modifi:
    c1_test.radius*=2
    print(f"{c1_test.name} Doubled: {c1_test.radius}{c1_test.area:.5f}")

    #RECTANGLE:
    r1_test = recta_1
    orig_length = r1_test.length
    orig_width = r1_test.width
    print(f"{r1_test.name} Current: {r1_test.length}{r1_test.width}{r1_test.area:.5f}")
    #lw modifi:
    r1_test.length *=2
    r1_test.width *=2
    print(f"{r1_test.name} Doubled: {r1_test.length}{r1_test.width}{r1_test.area:.5f}")

    #SQUARE:
    s_test = squa_1
    print(f"{s_test.name} Current: {s_test.side}{s_test.area:.5f}")
    #side modifi:
    s_test.side *=2
    print(f"{s_test.name} Doubled: {s_test.side}{s_test.area:.5f}")

    print("\nShapes testing finished.")

if __name__=="__main__":
    run_test_program()

