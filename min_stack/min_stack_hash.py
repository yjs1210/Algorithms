class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.len = 0
        self.data = {}
        self.min_num = None
        

    def push(self, x: int) -> None:
        if self.len == 0:
            self.data[self.len]  = (x,x)
            
        else:
            last_min = self.data[self.len-1][1]
            
            if x < last_min:
                self.data[self.len]  = (x,x)
            else:
                self.data[self.len] = (x, self.data[self.len-1][1])
            
        self.len += 1

    def pop(self) -> None:
        del self.data[self.len-1]
        self.len -= 1

    def top(self) -> int:
        return self.data[self.len-1][0]
        

    def getMin(self) -> int:
        return self.data[self.len-1][1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()