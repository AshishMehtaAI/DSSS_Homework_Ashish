import unittest
from math_quiz import Random_Integer, Random_Operator, Problem_Answer_Generator


class TestMathGame(unittest.TestCase):

    def test_Random_Integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = Random_Integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_Random_Operator(self):
        # Test if the random operator selected is always in the list of operators 
        operators=['+', '-', '*']
        for _ in range(1000):
             rand_operator=Random_Operator()
             self.assertTrue(rand_operator in operators)

    def test_Problem_Answer_Generator(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),(3, 4, '-', '3 - 4', -1),
                (3, 3, '-', '3 - 3', 0),(5, 2, '*', '5 * 2', 10)
            ]
            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                 self.assertEqual((expected_problem, expected_answer),(Problem_Answer_Generator(num1, num2, operator)))
                

if __name__ == "__main__":
    unittest.main()
