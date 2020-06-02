# python3

import sys

class Solver:
	def __init__(self, s):
		self.s = s
		self.n = len(s)
		self.m1 = 10**9 + 7
		self.m2 = 10**9 + 9
		self.x = 10**2
		self.h1 = self.compute_H(self.m1)
		self.h2 = self.compute_H(self.m2)

	def compute_H(self, m):
		h = [0]*(self.n)
		for i in range(1, self.n + 1):
			h[i] = (self.x * h[i-1] + ord(self.s[i-1])) % m
		return h

	def identity(self, h, x, a, l):
		return (h[a+l] - x**l*h[a]) 

	def ask(self, a, b, l):
		check_a1 = self.identity(self.h1, self.x, a, l)
		check_b1 = self.identity(self.h1, self.x, b, l)
		check_a2 = self.identity(self.h2, self.x, a, l)
		check_b2 = self.identity(self.h2, self.x, b, l)
		return (check_a1 == check_b1) & (check_a2 == check_b2)


s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")
