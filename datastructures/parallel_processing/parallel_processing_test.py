import unittest
from parallel_processing import assign_jobs

class TestBrackets(unittest.TestCase):
    #def test_small(self):
    #    for n in range(20):
    #        self.assertEqual(last_digit_of_the_sum_of_fibonacci_numbers(n),
    #                         last_digit_of_the_sum_of_fibonacci_numbers_naive(n))
    
    def test(self):
        for txt, ans in [([1,2,3,4,5], 'yp')]:
            self.assertEqual(assign_jobs(2, txt), ans)
        
if __name__ == '__main__':
    unittest.main()

