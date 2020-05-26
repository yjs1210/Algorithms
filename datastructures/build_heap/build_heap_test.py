import unittest
from build_heap_new import build_heap

class TestBrackets(unittest.TestCase):
    #def test_small(self):
    #    for n in range(20):
    #        self.assertEqual(last_digit_of_the_sum_of_fibonacci_numbers(n),
    #                         last_digit_of_the_sum_of_fibonacci_numbers_naive(n))
    
    def test(self):
        for txt, ans in [([5,4,3,2,1],[(1,4),(0,1),(1,3)])]:
            self.assertEqual(build_heap(txt), ans)
        
if __name__ == '__main__':
    unittest.main()

