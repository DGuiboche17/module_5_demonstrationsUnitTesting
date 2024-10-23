"""
Description: Module 05 demonstration: Functions with Unit Testing
Author: ACE Faculty
Date: {current date}
Usage: To execute the unit tests: 
        From the unit_testing directory in the Terminal:
        python -m unittest -v tests/test_functions.py
    To execute the python src program:
        From the unit_testing directory in the Terminal:
        python src/functions.py
"""

import unittest
from unittest.mock import patch
from src.functions import greet_name_age, \
                          math_operation, \
                          prompt_name_greeting
                            


# test_functionname_condition_expected
# 4 compononents to test name needed
class TestFunctions(unittest.TestCase):
    def test_greet_name_age_valid_arguments_expected_string(self):
        # Arrange
        name = "Dennis"
        age = 29
        expected = "Hello Dennis, you are 29 years old!"


        # Act
        actual = greet_name_age(name, age)


        # Assert
        self.assertEqual(expected, actual)

    def test_math_operation_addition_returns_sum(self):
        # Arrange
        operand1 = 10
        operand2 = 5
        operation = "+"

        expected = 15.0

        # Act
        actual = math_operation(operand1,operand2,operation)

        # Assert
        self.assertEqual(expected, actual)

        # Arrange, act and assert.
        # self.assertEqual(15.0, math_operation(10, 5, "+"))

    def test_math_operation_subtraction_returns_sum(self):

        # arrange
        operand1 = 10
        operand2 = 5
        operation = "-"

        expected = 5.0

        # act
        actual = math_operation(operand1, operand2, operation)

        # assert
        self.assertEqual(expected, actual)

        # self.assertEqual(5.0, math_operation(10, 5, "-"))

    def test_math_operation_invalid_operator_valueerror(self):
        # arrange 
        operator1 = 4
        operator2 = 15

        # use invalid operator
        operation = "*"
        expected = "Invalid operation."
        # Act and Assert
        with self.assertRaises(ValueError) as context:
            math_operation(operator1, operator2, operation)

        self.assertEqual(expected, str(context.exception))

    def test_prompt_name_greeting_valid_inputs_greeting_returned(self):
        # builtins.input allows us to mock input behaviour

        with patch("builtins.input") as mock_input:
            # Arrange
            mock_input.side_effect = ["Dennis", "Winnipeg"]
            expected = "Your name is Dennis and your current city is Winnipeg."

            # Act
            actual = prompt_name_greeting()
        # assert
        self.assertEqual(expected, actual)


    """
    WITHOUT MOCKING THE TEST WILL PAUSE AND ASK FOR INPUT
    # def test_prompt_name_greeting_no_mocking_pauses_program(self):
    #     expected = "Your name is Dennis and your current city is Winnipeg."

    #     actual = prompt_name_greeting()

    #     self.assertEqual(expected, actual)
            

    """