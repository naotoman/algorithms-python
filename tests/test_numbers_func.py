import unittest
import sys
sys.path.append('../')
sys.path.append('./')
import numbers_func

class TestNumbersFunc(unittest.TestCase):

    def test_prime_fact_dic(self):
        testCase = {
            2: {2: 1},
            3: {3: 1},
            4: {2: 2},
            7: {7: 1},
            12: {2: 2, 3: 1},
            18: {2: 1, 3: 2}
        }
        for x, expect in testCase.items():
            result = numbers_func.prime_fact_dic(x)
            self.assertEqual(result, expect)


    def test_prime_fact_list(self):
        testCase = {
            2: [2],
            3: [3],
            4: [2, 2],
            7: [7],
            12: [2, 2, 3],
            18: [2, 3, 3]
        }
        for x, expect in testCase.items():
            result = numbers_func.prime_fact_list(x)
            self.assertEqual(result, expect)


    def test_pow_mod(self):
        testCase = {
            (1, 1, 100): 1,
            (1, 8, 100): 1,
            (2, 1, 100): 2,
            (10, 1, 5): 0,
            (10, 1, 7): 3,
            (10, 1, 100): 10,
            (2, 7, 100): 28,
            (3, 5, 5): 3,
            (3, 5, 2): 1,
            (3, 5, 10): 3,
            (3, 5, 9): 0,
        }
        for (x, y, z), expect in testCase.items():
            result = numbers_func.pow_mod(x, y, z)
            self.assertEqual(result, expect)


    def test_gcd(self):
        testCase = {
            (1, 1): 1,
            (1, 2): 1,
            (2, 1): 1,
            (3, 3): 3,
            (4, 4): 4,
            (6, 35): 1,
            (15, 12): 3,
            (51, 23): 1,
            (6, 150): 6,
        }
        for (x, y), expect in testCase.items():
            result = numbers_func.gcd(x, y)
            self.assertEqual(result, expect)

if __name__ == '__main__':
    unittest.main()