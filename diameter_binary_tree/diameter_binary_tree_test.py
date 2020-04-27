import unittest
from diameter_binary_tree import  Solution


class TestDiameterTree(unittest.TestCase):
    #def test_small(self):
    #    for n in range(20):
    #        self.assertEqual(last_digit_of_the_sum_of_fibonacci_numbers(n),
    #                         last_digit_of_the_sum_of_fibonacci_numbers_naive(n))
    
    def test_large(self):
        sol = Solution()
        for (T, dia) in [([1,2,3,4,5], 3)]:
            self.assertEqual(sol.diameterOfBinaryTree(sol.create_tree_from_flat_list(T)), dia)
            
if __name__ == '__main__':
    unittest.main()
