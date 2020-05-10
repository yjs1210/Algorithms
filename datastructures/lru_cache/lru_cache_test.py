import unittest
from lru_cache import LRUCache


class TestCache(unittest.TestCase):
    #def test_small(self):
    #    for n in range(20):
    #        self.assertEqual(last_digit_of_the_sum_of_fibonacci_numbers(n),
    #                         last_digit_of_the_sum_of_fibonacci_numbers_naive(n))
    
    def test(self):
        cache = LRUCache(3)
        cache.put(1, 1)    #1
        cache.put(2, 2)    #2,1 
        self.assertEqual(cache.get(1),1) #1,2
        cache.get(1)       #// returns 1  
        cache.put(3, 3)   #// evicts key 2  #3,1,2
        self.assertEqual(cache.get(2),2)    #// returns -1 (not found) #2,3,1
        cache.put(4, 4)   #// evicts key 1 #4,2,3,1
        self.assertEqual(cache.get(1),-1)    #// returns -1 (not found)
        self.assertEqual(cache.get(3),3)       #// returns 3
        cache.get(4)       #// returns 4
        self.assertEqual(cache.head.value,4)   
        cache.put(4,2)
        self.assertEqual(cache.size,3)  
        self.assertEqual(cache.head.value, 2)
        self.assertEqual(cache.get(4), 2)
        

        
        
if __name__ == '__main__':
    unittest.main()

