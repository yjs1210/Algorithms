# python3

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')

def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

def solve(s, t):
	d = 26
	p = 29
	m = len(s)
	n = len(t)
	arr_res_s = [[0]*m for i in range(m+1)]
	arr_res_t = [[0]*n for i in range(n+1)]


	### precompute hash values of lnegth = 1 as initialize
	for i in range(m):
		arr_res_s[1][i] = ord(s[i])
	
	### precompute hash values of length 2...m 
	for i in range(2, m):
		for j in range(m-i):
			arr_res_s[i][j] = (arr_res_s[i-1][j] * d + ord(s[j+i-1])) % p 
	
	max_len = 0 
	### precompute hash values of lnegth = 1 as initialize
	check_1 = set(arr_res_t[1])
	n_exists = False
	for i in range(n):
		hash = ord(t[i])
		arr_res_t[1][i] = hash
		if not n_exists:
			if hash in check_1:
				n_exists = True
				max_len = 1
	
	### precompute hash values of length 2...n 
	for i in range(2, n):
		n_exists = False
		check_1 = set(arr_res_t[i])
		for j in range(n-i):
			hash = (arr_res_t[i-1][j] * d + ord(t[j+i-1])) % p 
			arr_res_t[i][j] = hash
			if not n_exists:
				if hash in check_1:
					n_exists = True
					max_len = i

	return max_len

for line in sys.stdin.readlines():
	s, t = line.split()
	ans = solve(s, t)
	print(ans.i, ans.j, ans.len)
