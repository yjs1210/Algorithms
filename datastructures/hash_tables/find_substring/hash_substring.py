# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def _hash_func(s, p, x):
        ans = 0
        for c in reversed(s):
            ans = (ans * x + ord(c)) % p
        return ans 

def are_equal(text, pattern, m):
    is_equal = True
    for i in range(m):
        if text[i] != pattern[i]:
            is_equal = False
            break
    return is_equal

def precompute_hashes(T, n, m, p, x):
    H = [0]*(n-m+1)
    S = T[n-m:n]
    H[n-m] = _hash_func(S, p, x)
    y = 1
    for i in range(1, m+1):
        y = (y*x)%p
    
    for i in range((n - m - 1), -1, -1):
        H[i] = (x*H[i+1] + ord(T[i]) - y*ord(T[i+m])) % p
    
    return H


def get_occurrences(pattern, text):
    ##prime number
    p = 1933
    ##number alphabets
    x = 26
    phash = _hash_func(pattern, p, x)
    res = []
    
    n = len(text)
    m = len(pattern)
    H = precompute_hashes(text, n, m , p, x)
    for i in range(n - m + 1):
        thash = H[i]
        if phash != thash:
            continue
        else:
            if are_equal(text[i:i+m], pattern, m):
                res.append(i)

    return res

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

