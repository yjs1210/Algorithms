
# python3


def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    from collections import defaultdict

    dp_map = defaultdict(list)

    for idx, j in enumerate(second_sequence):
        dp_map[j] += idx
    
    dp_ans_map = {}
    for i in first_sequence:
        if i in dp_map:
            ##eligible indices
            for k in dp_map[i]:
                
                for lower_seq, (opt, min_idx) in dp_ans_map:
                    if i < lower_seq &  k > min_idx:
                        
                        

            


    for i in first_sequence:
        if i in 
    












if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
