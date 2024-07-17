import random
from random import randint
import json
import math


class Functional_Programming():
    def __init__(self):
        pass

    def sort_list(self, array: list) -> list:
        # Write a function which sorts list of int from the smallest to larges value if provided list contains only int and return the sorted list. If provided list contains only str, sort in alphabetic order and return in uppercase. If a list contains both or other tape of variables, return ValueError. Do not use prewritten python functions.
        # z.B. [0, 9, 25, 1] -> [0, 1, 9, 25]
        # z.B. ['a', 'd', 'b'] -> ['A', 'B', 'D']
        # z.B. [0, 9, 25, 'a'] -> ValueError

        # quick sort
        if all(isinstance(item, int) for item in array):
            pass
        elif all(isinstance(item, str) and item.isalpha() for item in array):
            array = [s.upper() for s in array]
        else:
            raise ValueError("List contains mixed types of non int/str.")

        if len(array) <= 1:
            return array
        
        pivot = array.pop()

        item_smaller = []
        item_larger = []

        for item in array:
            if item > pivot:
                item_larger.append(item)
            else:
                item_smaller.append(item)

        return self.sort_list(item_smaller) + [pivot] + self.sort_list(item_larger)


    def find_sqrt(self, array: list[int]) -> list[int]:
        # Write a function which receives list of positive and negative ints (also zeroes) and returns list of sqrt for ints >= 0.
        # z.B. [0, 1, -9, 16] -> [0, 1, 4]
        # z.B. [ -1, -9, -16] -> []
        result = []

        if not all(isinstance(num, int) for num in array):
            raise ValueError("Input type should be list of integers")
        
        for num in array:
            if num == 0:
                result.append(0)

            if num > 0:
                for n in range(num + 1):
                    n_square = n * n
                    if n_square == num:
                        result.append(n)
                        break
                    if n_square > num:
                        break

        return result

    def fibonacci_Generator(self):
        # Write a function which produces generator of fibonacci sequence.
        a, b = 0, 1
        while True:
            yield b
            a, b = b, a + b

    def flatten_list(self, list_of_lists: list) -> list:
        # Write a function which produces a standart list from nested list.
        # z.B. [[1,2,3], [4,9,8,7,8]] -> [1,2,3,4,9,8,7,8]
        # z.B. [1,2,[3], [4,[9,[8]],7,8]] -> [1,2,3,4,9,8,7,8]
        # z.B. ["ran",1, [1,3,4,5]] ->    ["ran",1,1,3,4,5]

        result = []
        for item in list_of_lists:
            if isinstance(item, list):
                result.extend(self.flatten_list(item))
            else:
                result.append(item)

        return result

    def inverse_each_sentence(self, text: str) -> str:
        # Write a function which inverts the words' order within each sentence from the given text. Check whether the input is a text (should contain a dot)
        # z.B. ' A two-inch layer of freshly fallen snow covered the yard.' -> 'yard the covered snow fallen freshly of layer two-inch A.'

        if "." not in text:
            raise ValueError("Input should contain at least one dot.")

        sentences = text.split('.')
        result_sentences = []

        for i, sentence in enumerate(sentences):
            if sentence:
                words = sentence.split()
                inverted = ' '.join(reversed(words))
                result_sentences.append(inverted)

        return '. '.join(result_sentences) + '.'


if __name__ == "__main__":  # comment: this tests to be removed later
    fp = Functional_Programming()

    assert fp.sort_list([3, 2, 1, 5]) == [1, 2, 3, 5]
    assert fp.sort_list(['a', 'c', 'd', 'b']) == ['A', 'B', 'C', 'D']

    try:
        fp.find_sqrt(["3", "2", "1", "5"])  # this should throw Value error
    except ValueError:
        pass
    else:
        assert False

    try:
        fp.find_sqrt([3, 2, "a", "b"])  # this should throw Value error
    except ValueError:
        pass
    else:
        assert False

    fg = fp.fibonacci_Generator()
    assert next(fg) == 1
    assert next(fg) == 1
    assert next(fg) == 2
    assert next(fg) == 3
    assert next(fg) == 5

    assert fp.find_sqrt([0, 1, -9, 16]) == [0, 1, 4]
    assert fp.find_sqrt([-1, -9, -16]) == []
    assert fp.find_sqrt([]) == []
    assert fp.find_sqrt([-61, -72, -36, 0, -23, 0, -55, -16]) == [0, 0]

    try:
        fp.find_sqrt(["1", "9", "16", "-25"])  # this should throw Value error
    except ValueError:
        pass
    else:
        assert False

    assert fp.flatten_list([[1, 2, 3], [4, 9, 8, 7, 8]]) == [
        1, 2, 3, 4, 9, 8, 7, 8]
    assert fp.flatten_list([1, 2, [3], [4, [9, [8]], 7, 8]]) == [
        1, 2, 3, 4, 9, 8, 7, 8]
    assert fp.flatten_list(["ran", 1, [1, 3, 4, 5]]) == ["ran", 1, 1, 3, 4, 5]

    assert fp.inverse_each_sentence(
        " A two-inch layer of freshly fallen snow covered the yard.") == "yard the covered snow fallen freshly of layer two-inch A."

    assert fp.inverse_each_sentence(
        " A two-inch layer of freshly fallen snow covered the yard. Stacey peeked outside. To most, it would have been a beautiful sight worthy of taking a photo to put on Instagram.") == "yard the covered snow fallen freshly of layer two-inch A. outside peeked Stacey. Instagram on put to photo a taking of worthy sight beautiful a been have would it most, To."
