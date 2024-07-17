import math
from abc import ABC, abstractmethod


class Calculator():
    def __init__(self):
        pass

    def add_one(self, values: list[int]) -> list[int]:
        # write a function to return list of values+1
        # return values
       
        if not all(isinstance(value, int) for value in values):
            raise ValueError("Input type should be list of integers")

        result = [value + 1 for value in values]
        return result


class Rectangle():
    # Write a Rectangle class with two functions: to calculate area and to calculate perimeter.
    def __init__(self, width: int, length: int):
        # comment: I'd prefer to check the values here instead of doing in each method
        #if not (isinstance(width, int) and isinstance(length, int) and width > 0 and length > 0):
        #    raise ValueError("Width and length must be positive integers.")
 
        self.width = width
        self.length = length

    def calculate_area(self) -> int:
        # Check whether both values are positive and handle otherwise.       
        if not (isinstance(self.width, int) and isinstance(self.length, int) and self.width > 0 and self.length > 0):
            raise ValueError("Width and length must be positive integers.")
        return self.width * self.length

    def calculate_perimeter(self) -> int:
        # Check whether both values are positive and handle otherwise.
        if not (isinstance(self.width, int) and isinstance(self.length, int) and self.width > 0 and self.length > 0):
            raise ValueError("Width and length must be positive integers.")
        return 2 * (self.width + self.length)


class Curves(ABC):
    # Define two abstract methods and implement them for two subclasses.
    def __init__(self, x: int, a: int, b: int):
        if not (isinstance(x, int) and isinstance(a, int) and isinstance(b, int)):
            raise ValueError("Inputs must be integers.")

        self.x = x  # comment: I think, x should not be assigned here, instead on find_y_by_x
        self.a = a
        self.b = b

    @abstractmethod
    def find_where_y_is_zero(self):
        pass

    @abstractmethod
    def find_y_by_x(self):
        pass


class Linear(Curves):
    # y = ax + b
    def find_y_by_x(self) -> int:
        return self.a * self.x + self.b

    def find_where_y_is_zero(self) -> float:
        if self.a == 0:
            if self.b == 0:
                raise ValueError("y = 0 for all x")
            else:
                raise ValueError("There is no solution.")
        return - self.b / self.a


class Bilinear(Curves):
    # y = ax^2+b
    def find_y_by_x(self):
        return self.a * self.x ** 2 + self.b

    def find_where_y_is_zero(self) -> float:
        # Check whether calculations are possible with given parameters.
        if self.a == 0:
            if self.b == 0:
                raise ValueError("y = 0 for all x")
            else:
                raise ValueError("There is no solution.")

        d = - self.b / self.a
        if d < 0:
            raise ValueError("There is no root in real number.")
        result = math.sqrt(d)  # comment: we only return the non negative root

        return result
