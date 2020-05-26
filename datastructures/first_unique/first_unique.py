class doubleLinkedList():
    def __init__(self, val):
        self.value = val 
        self.left = None
        self.right = None
        self.removed = False

class FirstUnique:
    
    def __insert(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:

            curr_tail = self.tail
            curr_tail.right = node
            node.left = curr_tail
            self.tail = node
            
    def __remove(self, val):
        node = self.mapper[val] 
        if node.removed == True:
            return 
        if self.head == node == self.tail:
            self.head = None
            self.tail = None 
        
        elif self.head == node:
            self.head = self.head.right
            self.head.left = None
        elif self.tail == node:
            self.tail = node.left
            self.tail.right = None
        else:
            curr_left = node.left
            curr_right = node.right
            curr_left.right = curr_right
            curr_right.left = curr_left 
            
        node.removed = True
    
    def __init__(self, nums):
        self.mapper = {}
        self.head = None
        self.tail = None
        
        for i in nums:
            if i not in self.mapper:
                node = doubleLinkedList(i)
                self.mapper[i] = node
                self.__insert(node)
            else:
                self.__remove(i)

    def showFirstUnique(self) -> int:
        if self.head == None:
            return -1
        return self.head.value 

    def add(self, value: int) -> None:
        if value not in self.mapper:
            node = doubleLinkedList(value)
            self.__insert(node)
        else:
            self.__remove(value)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)