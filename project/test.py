import unittest

import my_sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = my_sum.sum(data)
        self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()

    '''The test results should show that the sum of [1, 2, 3] is 6 however when I run it just 
    shows "ran 1 test in 0.007s" and "OK"'''