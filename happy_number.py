class Solution:
    def isHappy(self, n: int) -> bool:
            digits = str(n)
            sum_digits = sum(map(lambda x: int(x)**2, digits))
            if sum_digits == 1:
                return True
            else: 
                self.isHappy(sum_digits)
        
if __name__ == '__main__':
    runner = Solution()
    print(runner.isHappy(92))
