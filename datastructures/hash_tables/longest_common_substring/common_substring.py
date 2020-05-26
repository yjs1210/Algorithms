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
	arr_res = [[0]*m for i in range(m+1)]


	### precompute hash values of lnegth = 1 as initialize
	for i in range(m):
		arr_res[1][i] = ord(s[i])
	
	### precompute hash values of length 2...m 
	for i in range(2, m):
		for j in range(m-i):
			arr_res[i][j] = (arr_res[i-1][j] * d + ord(s[j+i-1])) % p 
	
	for i in range(1, m):
		






	ans = Answer(0, 0, 0)
	for i in range(len(s)):
		for j in range(len(t)):
			for l in range(min(len(s) - i, len(t) - j) + 1):
				if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
					ans = Answer(i, j, l)
	return ans

for line in sys.stdin.readlines():
	s, t = line.split()
	ans = solve(s, t)
	print(ans.i, ans.j, ans.len)
