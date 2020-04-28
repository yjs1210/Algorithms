# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    import math
    assert len(elements) <= 10 ** 5
    ##each element sends to the recursive parent what its majority is. if tie, communicate that, if both ties, then communicate tie.
    
    def recursive_calls(left, right):
        if len(elements[left:right+1]) == 1:
            return (elements[left])
        else:
            mid = (left+right)//2
            left_val = recursive_calls(left, mid)
            right_val = recursive_calls(mid+1, right)

            if left_val == right_val:
                return left
            else:
                left_counter = 0
                right_counter =0 
                for i in range(left, right+1):
                    if elements[i] == left_val:
                        left_counter += 1
                    elif elements[i] == right_val:
                        right_counter += 1

                if left_counter > len(elements)/2:
                    return 1
                elif right_counter > len(elements)/2:
                    return 1

    ans = recursive_calls(0, len(elements)-1)
    if ans:
        return 1
    else:
        return 0 
            
     




    







if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
