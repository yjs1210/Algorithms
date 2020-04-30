# python3


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    output = [(0,[])]*(n+1)
    output[1] = (0, [1])

    for i in range(2,n+1):
        add_1 = output[i-1][0] + 1
        mult_2 = output[int(i/2)][0] + 1 if i % 2 == 0 else n+1
        mult_3 = output[int(i/3)][0] + 1 if i % 3 == 0 else n+1
        
        if add_1 <= mult_2 <= mult_3:
            output[i] = (add_1 ,  output[i-1][1] + [i])
        
        elif mult_2 <= add_1 <= mult_3:
            output[i] = (mult_2 ,  output[int(i/2)][1] + [i])

        else:
            output[i] = (mult_3 ,  output[int(i/3)][1] + [i])

    return output[n][1]
    











if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
