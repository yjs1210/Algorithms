import unittest
from hash_chains import QueryProcessor


class TestCache(unittest.TestCase):
    #def test_small(self):
    #    for n in range(20):
    #        self.assertEqual(last_digit_of_the_sum_of_fibonacci_numbers(n),
    #                         last_digit_of_the_sum_of_fibonacci_numbers_naive(n))
    
    def test(self):
        map_ = QueryProcessor(5)
        map_.add('world')    
        map_.add('Hell0')   
        map_.check(4)
        #map_.find('World')
        map_.find('world')
        map_.delete('world')
        map_.check(4)
        map_.delete('Hell0')
        map_.add('luck')
        map_.add('GooD')
        map_.check(2)
        map_.delete('good')
        

        
        
if __name__ == '__main__':
    unittest.main()

