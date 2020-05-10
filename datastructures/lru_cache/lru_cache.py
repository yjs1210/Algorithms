
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
        self.cache_init = False

    def _insert(self, node):
        current_head = self.head 
        current_head.left = node 
        node.left = None 
        self.head = node
        self.head.right = current_head 
        self.head = node

    def _remove_node(self, node):
        if self.tail != node:
            curr_right = node.right
            curr_left = node.left
            curr_right.left = curr_left
            curr_left.right = curr_right 
        else:
            curr_left = node.left
            self.tail = curr_left 
            curr_left.right = None 
            

    def _move_to_head(self, node):
        self._remove_node(node)
        self._insert(node)

    def get(self, key: int) -> int:
        if key in self.cache_pointer:
            node = self.cache_pointer[key]
            if self.head == node: 
                return node.value

            self._move_to_head(node)
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
        self.size -= 1
    
    def create_cache(self, key, value):
        node = DoubleLinkedList(key, value)
        self.head = node
        self.tail = node 
        self.cache_init = True
        self.cache_pointer[key] = node
        self.size += 1

    def put(self, key: int, value: int) -> None:
        if not self.cache_init:
            self.create_cache(key, value)
            
        else:
            if key not in self.cache_pointer:
                new_node = DoubleLinkedList(key, value)
                self._insert(new_node)
                self.cache_pointer[key] = new_node
                self.size += 1
                if self.size > self.capacity:
                    self.evict()
            else:
                node = self.cache_pointer[key]
                node.value = value
                if self.head != node:
                    self._move_to_head(node)
            
                
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)