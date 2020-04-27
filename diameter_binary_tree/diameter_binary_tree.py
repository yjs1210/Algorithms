# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def create_tree_from_flat_list(self, node_list, index=0):
        if index >= len(node_list) or node_list[index] is None:
            return None
        d = node_list[index]
        l = index * 2 + 1
        r = l + 1
        tree = TreeNode(d)
        tree.left = self.create_tree_from_flat_list(node_list, l)
        tree.right = self.create_tree_from_flat_list(node_list, r)
        return tree
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.diameter = 0 
        
        def dfs_update(self, node):
            if not node:
                return 0
            max_left = dfs_update(self, node.left)
            max_right = dfs_update(self, node.right)
            length = max(max_left, max_right) 
            self.diameter = max(max_left + max_right, self.diameter)
            return length + 1 
        
        dfs_update(self, node = root)
        return self.diameter 
        
        
        
        
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        