import math
from abc import abstractmethod

class Calculator():
    def __init__( self ):
        pass

    def add_one(self, values: list[int]) -> list[int]:
# write a function to return list of values+1
        # return values
class Rectangle():
#### Write a Rectangle class with two functions: to calculate area and to calculate perimeter.
    def __init__(self, width: int, length: int):
        pass
    def calculate_area(self) -> int:
#### Check whether both values are positive and handle otherwise.
        return 0
    def calculate_perimeter(self)-> int:
#### Check whether both values are positive and handle otherwise.
        return 0
class Curves:
#### Define two abstract methods and implement them for two subclasses.
    def __init__(self, x: int, a: int, b: int):
        self.x = x
        self.a = a
        self.b = b


    # def find_where_y_is_zero(self):


    # def find_y_by_x(self):

class Linear(Curves):
        # y = ax + b
    def find_y_by_x(self)-> int:
        return 0
    def find_where_y_is_zero(self)-> int:
        return 0
class Bilinear(Curves):
    # y = ax^2+b
    def find_y_by_x(self):
        return 0
    def find_where_y_is_zero(self)-> int:
#### Check whether calculations are possible with given parameters.
        return 0


