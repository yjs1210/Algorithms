# python3

import sys
import threading


class Node:
    def __init__(self, val):
        self.child = []
        self.val = val
        self.distance = 0  
    
    def add_child(self, n):
        self.child.append(n)

def compute_height_old(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height

def build_tree(n, parents):

    arr_nodes = [0]*n
    for i in range(n):
        arr_nodes[i] = [Node(i)]
    for idx, parent in enumerate(parents):
        if parent == -1:
            root = idx 
        arr_nodes[parent].add_child(arr_nodes[idx])
    return arr_nodes, root

def compute_height(n, parents):
    # Replace this code with a faster implementation

    arr_nodes, root = build_tree(n, parents)
    distances = [0]*len(arr_nodes)
    
    def dfs(node, distance):
        distances[node.val] = distance
        for i in node.child:
            dfs(i, distance + 1)
    
    dfs(root, 0)

    return distances.max()


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
