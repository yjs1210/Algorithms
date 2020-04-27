# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    def identify_period(m):
        hist = []
        hist.append(0)
        hist.append(1)

        curr_idx = 2
        while True:
            next = hist[curr_idx -2] + hist[curr_idx -2]
            hist.append(next)
            
            if (hist[curr_idx] == 1) & (hist[curr_idx-1] == 0):
                break

            curr_idx += 1
        
        return curr_idx - 1, hist 
    
    period, fib_nums = identify_period(m)
    
    n_target = n % period 

    return fib_nums[n_target] % m

        




if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
