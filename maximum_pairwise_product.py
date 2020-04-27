def maximum_pairwise_product(input_numbers : list):
    '''
    We are given n on the first line and next line 
    that contains n nonnegative integers
    '''
    
    max_1 = 0 
    max_2 = 0

    for i in input_numbers:
        if i > max_1:
            max_2 = max_1
            max_1 = i
        elif i > max_2:
            max_2 = i
        
    return max_1 * max_2

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(maximum_pairwise_product(input_numbers))