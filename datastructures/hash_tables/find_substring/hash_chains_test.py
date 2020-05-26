import unittest
from hash_substring import get_occurrences


class TestCache(unittest.TestCase):
    #def test_small(self):
    #    for n in range(20):
    #        self.assertEqual(last_digit_of_the_sum_of_fibonacci_numbers(n),
    #                         last_digit_of_the_sum_of_fibonacci_numbers_naive(n))
    
    def test(self):
        get_occurrences('bra', 'abracadabra')
        

        
        
if __name__ == '__main__':
    unittest.main()

