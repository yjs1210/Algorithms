
class DoubleLinkedList:
    
    def __init__(self, key, value, left = None, right = None):
        self.value = value
        self.key = key
        self.left = left
        self.right = right

class LRUCache:
    
    
    from collections import defaultdict
    def __init__(self, capacity: int):
        self.cache_pointer = {}
        self.capacity = capacity
        self.size = 0
        self.cache = None

    def get(self, key: int) -> int:
        if key in self.cache_pointer:
            return self.cache_pointer[key].value
        else:
            return -1
            
    def evict(self):
        end = self.tail
        new_tail = end.left
        new_tail.right = None
        self.tail = new_tail
        del self.cache_pointer[end.key]
        del end 
    
    def create_cache(self, key, value):
        node = DoubleLinkedList(key, value)
        self.cache = node
        self.head = node
        self.tail = node 

    def put(self, key: int, value: int) -> None:
        if not self.cache:
            self.create_cache(key, value)
        
        if key not in self.cache_pointer:
            new_node = DoubleLinkedList(key, value)
            head_node = self.head
            head_node.left = new_node
            new_node.right = head_node
            self.cache_pointer[key] = new_node
            self.head = new_node
            self.size += 1
            if self.size > self.capacity:
                self.evict()
                
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)