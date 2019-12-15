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

if __name__ == '__main__':
    unittest.main()