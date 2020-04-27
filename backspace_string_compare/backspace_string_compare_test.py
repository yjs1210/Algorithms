import unittest
from backspace_string_compare import   Solution


class TestBackSapce(unittest.TestCase):
    #def test_small(self):
    #    for n in range(20):
    #        self.assertEqual(last_digit_of_the_sum_of_fibonacci_numbers(n),
    #                         last_digit_of_the_sum_of_fibonacci_numbers_naive(n))

    def test_large(self):
        sol = Solution()
        for (S, T, truth) in [("xywrrmp", "xywrrmu#p", True), ("a#c", "b", False), ("ab#c", "ad#c", True)]:
            self.assertEqual(sol.backspaceCompare(S, T), truth)
            
if __name__ == '__main__':
    unittest.main()
