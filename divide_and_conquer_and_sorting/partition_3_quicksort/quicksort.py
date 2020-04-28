# python3

from random import randint


def partition3(array, left, right):
    left_idx = left
    pivot = array[left]
    for i in range(left+1, right+1):
        curr_val = array[i]
        if curr_val < pivot:
            left_idx += 1
            array[left_idx], array[i]  = array[i], array[left_idx]
    
    array[left] , array[left_idx]  = array[left_idx], array[left]
    right_idx = left_idx
    
    for i in range(left_idx+1, right+1):
        curr_val = array[i]
        if curr_val == pivot:
            right_idx += 1
            array[right_idx], array[i]  = array[i], array[right_idx]
    
    return left_idx, right_idx 

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1-1)
    randomized_quick_sort(array, m2+1, right) 

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
