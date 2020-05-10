import unittest
from first_unique import FirstUnique


class TestCache(unittest.TestCase):
    #def test_small(self):
    #    for n in range(20):
    #        self.assertEqual(last_digit_of_the_sum_of_fibonacci_numbers(n),
    #                         last_digit_of_the_sum_of_fibonacci_numbers_naive(n))
    
    def test(self):
        cache = FirstUnique([1,2,3,4,4,3])
        self.assertEqual(cache.showFirstUnique(), 1)
        cache.add(1)       #// returns 1  
        self.assertEqual(cache.showFirstUnique(), 2)  #// evicts key 2  #3,1,2
        cache.add(2)
        self.assertEqual(cache.showFirstUnique(), -1)

        cache = FirstUnique([7,7,7,7,7,7])
        self.assertEqual(cache.showFirstUnique(), -1)
        cache.add(7)
        cache.add(3)
        self.assertEqual(cache.showFirstUnique(), 3)
        cache.add(3)
        cache.add(17)

        

        
        
if __name__ == '__main__':
    unittest.main()

