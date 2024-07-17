import unittest
import pandas as pd
import pandas.testing as pd_testing
import json
import sys

if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO

from ImplementMe.main.inheritance_and_exception_handling import Calculator, Rectangle, Curves, Linear, Bilinear
from ImplementMe.main.DataFrame_and_requests import DataFrame_Excersises
from ImplementMe.main.functional_programming import Functional_Programming


class CalculatorTest(unittest.TestCase):
    def test_add_one(self):
        calculator: Calculator = Calculator()
        inputValues = calculator.add_one([1,2,3])
        expectedResult = [2,3,4]
        self.assertEqual(inputValues, expectedResult)

    def test_Rectangle_inheritance(self):
        rectangle: Rectangle = Rectangle(10, 15)
        inputValues_area = rectangle.calculate_area()
        inputValues_perimeter = rectangle.calculate_perimeter()
        self.assertEqual(inputValues_area, 150)
        self.assertEqual(inputValues_perimeter, 50)
    def test_Rectangle_exceptions_handling(self):
        rectangle: Rectangle = Rectangle(-1, 12)
        with self.assertRaises(ValueError):
            rectangle.calculate_area()

    # def test_Curves_inheritance(self):  # comment: I think this test is wired
    #     curves: Curves = Curves(1,2,3)
    #     self.assertEqual(Linear.find_where_y_is_zero(curves), -1.5)
    # def test_exception(self):
    #     curves: Curves = Curves(1,2,3)  # comment: I think this test is wired
    #     with self.assertRaises(ValueError):
    #         Bilinear.find_where_y_is_zero(curves)

    def test_Linear_find_where_y_is_zero(self):
        linear: Linear = Linear(1, 2, 3)
        self.assertEqual(linear.find_where_y_is_zero(), -1.5)

    def test_Linear_find_where_y_is_zero_error_all_x(self):
        linear = Linear(1, 0, 0)
        with self.assertRaisesRegex(ValueError, "y = 0 for all x"):
            linear.find_where_y_is_zero()

    def test_Linear_find_where_y_is_zero_error_no_solution(self):
        linear = Linear(1, 0, 1)
        with self.assertRaisesRegex(ValueError, "There is no solution."):
            linear.find_where_y_is_zero()

    def test_Linear_find_y_by_x(self):
        linear: Linear = Linear(1, 2, 3)
        self.assertEqual(linear.find_y_by_x(), 5)

    def test_Bilinear_find_where_y_is_zero(self):
        bilinear: Bilinear = Bilinear(1, -1, 4)
        self.assertEqual(bilinear.find_where_y_is_zero(), 2)

    def test_Bilinear_find_where_y_is_zero_error_all_x(self):
        bilinear: Bilinear = Bilinear(1, 0, 0)
        with self.assertRaisesRegex(ValueError, "y = 0 for all x"):
            bilinear.find_where_y_is_zero()

    def test_Bilinear_find_where_y_is_zero_error_no_solution(self):
        bilinear: Bilinear = Bilinear(1, 0, 1)
        with self.assertRaisesRegex(ValueError, "There is no solution."):
            bilinear.find_where_y_is_zero()

    def test_Bilinear_find_where_y_is_zero_error_no_root(self):
        bilinear: Bilinear = Bilinear(1, 2, 3)
        with self.assertRaisesRegex(ValueError, "There is no root in real number."):
            bilinear.find_where_y_is_zero()

    def test_Bilinear_find_y_by_x(self):
        bilinear: Bilinear = Bilinear(2, 1, 3)
        self.assertEqual(bilinear.find_y_by_x(), 7)


class DataFrameTest(unittest.TestCase):
    def test_import_data(self):
        data_frame: DataFrame_Excersises = DataFrame_Excersises('data/Gym_dataset.csv')
        pd_testing.assert_frame_equal(data_frame.import_data(), pd.read_csv(StringIO(data['Gym_dataset_extracted'])))
    def test_group_by_difficulty(self):
        data_frame: DataFrame_Excersises = DataFrame_Excersises('data/Gym_dataset.csv')
        pd_testing.assert_frame_equal(data_frame.group_by_difficulty('Average'), pd.read_csv(StringIO(data['Gym_group_by_difficulty'])))
    def test_get_statistics(self):
        data_frame: DataFrame_Excersises = DataFrame_Excersises('data/Gym_dataset.csv')
        pd_testing.assert_frame_equal(data_frame.get_statistics(**data['Gym_statistics']['input_1']), pd.DataFrame.from_dict(data['Gym_statistics']['output_1']), check_like=True)
        pd_testing.assert_frame_equal(data_frame.get_statistics(**data['Gym_statistics']['input_2']), pd.DataFrame.from_dict(data['Gym_statistics']['output_2']), check_like=True)
        pd_testing.assert_frame_equal(data_frame.get_statistics(**data['Gym_statistics']['input_3']), pd.DataFrame.from_dict(data['Gym_statistics']['output_3']), check_like=True)

    def test_create_nested_dict(self):
        data_frame: DataFrame_Excersises = DataFrame_Excersises('data/Gym_dataset.csv')
        with open ('data/Gym_nested_dict.json') as json_file:
            self.assertDictEqual(data_frame.create_nested_dict(), json.load(json_file))
    def test_request_send_url(self):
        data_frame: DataFrame_Excersises = DataFrame_Excersises('data/Gym_nested_dict.json')
        self.assertEqual(data['request_send_url'], data_frame.request_send_url(timeout = 1))
        with self.assertRaises(ValueError):
            data_frame.request_send_url(timeout= -1)
    def test_request_get_data(self):
        data_frame: DataFrame_Excersises = DataFrame_Excersises(' ')
        self.assertEqual(data['request_get_data'], data_frame.request_get_data())

class FunctionalProgrammingTests(unittest.TestCase):
    def test_sort_list(self):
        fp: Functional_Programming = Functional_Programming()
        self.assertEqual(fp.sort_list(data['sort']['input_1']), data['sort']['output_1'])
        self.assertEqual(fp.sort_list([1]), [1])
        self.assertEqual(fp.sort_list([]), [])
        self.assertEqual(fp.sort_list(data['sort']['input_2']), data['sort']['output_2'])
        with self.assertRaises(ValueError):
            fp.sort_list(data['sort']['input_3'])
        with self.assertRaises(ValueError):
            fp.sort_list(data['sort']['input_4'])


    def test_find_sqrt(self):
        fp: Functional_Programming = Functional_Programming()
        self.assertEqual(fp.find_sqrt(data['sqrt']['input_1']), data['sqrt']['output_1'], 'sqrt is not taken properly!')
        self.assertEqual(fp.find_sqrt(data['sqrt']['input_2']), data['sqrt']['output_2'], 'list of negative ints should return empty list!')
        with self.assertRaises(ValueError):
            fp.find_sqrt(data['sqrt']['input_3'])
    def test_fibonacci_Generator(self):
        fp: Functional_Programming = Functional_Programming()
        fib_generator = fp.fibonacci_Generator()
        for i in range(100):
            self.assertEqual(next(fib_generator), data['fibonacci'][i], 'fibonacci sequence doesnt match the output!')
    def test_flatten_list(self):
        fp: Functional_Programming = Functional_Programming()
        self.assertEqual(fp.flatten_list(data['flatten']['input_1']), data['flatten']['output_1'], 'list is not flat!')
        self.assertEqual(fp.flatten_list(data['flatten']['input_2']), data['flatten']['output_2'], 'cant process empty list')
        self.assertEqual(fp.flatten_list(data['flatten']['input_3']), data['flatten']['output_3'], 'cant process list of ints')
        self.assertEqual(fp.flatten_list(data['flatten']['input_4']), data['flatten']['output_4'], 'cant process arbitrarily nested list')
        self.assertEqual(fp.flatten_list(data['flatten']['input_5']), data['flatten']['output_5'], 'cant process list of str and int')


    def test_reverse_each_sentence(self):
        fp: Functional_Programming = Functional_Programming()
        self.assertEqual(fp.inverse_each_sentence(data['inverse_text']['input_1']), data['inverse_text']['output_1'])
        self.assertEqual(fp.inverse_each_sentence(data['inverse_text']['input_3']), data['inverse_text']['output_3'])
        with self.assertRaises(ValueError):
            fp.inverse_each_sentence(data['inverse_text']['input_2'])

with open('data/inputs_and_outputs.json', 'r') as json_file:
    data = json.load(json_file)


if __name__ == '__main__':
    unittest.main()



