import unittest
from check_brackets import are_matching, find_mismatch


class TestBrackets(unittest.TestCase):
    #def test_small(self):
    #    for n in range(20):
    #        self.assertEqual(last_digit_of_the_sum_of_fibonacci_numbers(n),
    #                         last_digit_of_the_sum_of_fibonacci_numbers_naive(n))
    
    def test(self):
        for txt, ans in [('[[]]', "Success"), ('(())', "Success"),('[)', 2),('[]]', 3), ('[', 1), ('[[][', 1)]:
            self.assertEqual(find_mismatch(txt), ans)
        

        
        
if __name__ == '__main__':
    unittest.main()

