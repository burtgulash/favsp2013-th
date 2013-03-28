#! /usr/bin/python

import sys
from random import randint

def randomPair():
	maxValue = 9
	return (str(randint(0, maxValue)), str(randint(0, maxValue)))

def generateMatrix(m, n):
	matrix = [n * [None] for _ in range(m)]
	for i in range(m):
		for j in range(n):
			matrix[i][j] = randomPair()
	return matrix

def transpose(matrix):
	m = len(matrix)
	assert(m > 0)
	n = len(matrix[0])

	trans = [m * [None] for _ in range(n)]
	for i in range(m):
		for j in range(n):
			trans[j][i] = (matrix[i][j][1], matrix[i][j][0])
	return trans
			

def getRowMaxima(matrix):
	m = len(matrix)
	assert(m > 0)
	n = len(matrix[0])

	maxs = []
	for i in range(m):
		row_max = matrix[i][0][1]
		for j in range(n):
			if matrix[i][j][1] > row_max:
				row_max = matrix[i][j][1]
		maxs += [row_max]
	return maxs

def readMatrix(filee):
	matrix = []

	row_len = -1
	for line in filee:
		row = []
		for pair in line.split():
			nums = [s for s in pair.split(",")]
			if len(nums) != 2:
				print "Invalid number of players in %s" % nums
			row += [tuple(nums)]
		if not line or len(row) == 0:
			break

		matrix += [row]

		if row_len > 0 and row_len != len(row):
			print "Rows differ in length."

		row_len = len(row)

	return matrix

def printMatrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			x = matrix[i][j]
			print str(x[0]) + "," + str(x[1]),
		print

def findNashEquilibria(matrix):
	m = len(matrix)
	assert(m > 0)
	n = len(matrix[0])

	eqs = []

	row_maxs = getRowMaxima(matrix)
	col_maxs = getRowMaxima(transpose(matrix))

	for i in range(m):
		for j in range(n):
			if matrix[i][j][0] == col_maxs[j] and matrix[i][j][1] == row_maxs[i]:
				eqs += [(i, j)]
	return eqs

def findMixed(matrix):
	a = matrix[0][0][0]
	b = matrix[0][1][0]
	c = matrix[1][0][0]
	d = matrix[1][1][0]

	if not isinstance(a, int):
		num = d - c
		denom = -b + d - c
		p = "%d / (%s + %d)" % (num, a, denom)
	elif not isinstance(b, int):
		num = d - c
		denom = a + d - c
		p = "%d / (%s + %d)" % (num, b, denom)
	elif not isinstance(c, int):
		num = d
		denom = a - b + d
		p = "(%d + %s) / (%s + %d)" % (num, c, c, denom)
	elif not isinstance(d, int):
		num = -c
		denom = a - b - c
		p = "(%d + %s) / (%s + %d)" % (num, d, d, denom)
	else:
		denom = a - b + d - c
		if denom == 0:
			p = None
		else:
			p = (d - c) / (1.0 * denom)


	a = matrix[0][0][1]
	b = matrix[0][1][1]
	c = matrix[1][0][1]
	d = matrix[1][1][1]

	if not isinstance(a, int):
		num = d - b
		denom = -b + d - c
		q = "%d / (%s + %d)" % (num, a, denom)
	elif not isinstance(b, int):
		num = d
		denom = a + d - c
		q = "%d / (%s + %d)" % (num, b, denom)
	elif not isinstance(c, int):
		num = d - b
		denom = a - b + d
		q = "(%d + %s) / (%s + %d)" % (num, c, c, denom)
	elif not isinstance(d, int):
		num = -b
		denom = a - b - c
		q = "(%d + %s) / (%s + %d)" % (num, d, d, denom)
	else:
		denom = a - b + d - c
		if denom == 0:
			q = None
		else:
			q = (d - b) / (1.0 * denom)

	if isinstance(p, str) or p and 0 <= p <= 1:
		if isinstance(q, str) or q and 0 <= q <= 1:
			return p, q

	return None


def equilibriumToProbabilities(eq):
	return 1 - eq[0], 1 - eq[1]

def numeric(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			x = matrix[i][j]
			if not isinstance(x[0], int) or not isinstance(x[1], int):
				return False
	return True

def strToIntMatrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			m = matrix[i][j]
			a, b = m
			try:
				a = int(a)
			except ValueError:
				pass
			try:
				b = int(b)
			except ValueError:
				pass
		
			matrix[i][j] = a, b


if __name__ == "__main__":
	matrix = None

	if len(sys.argv) > 1 and (sys.argv[1] == "-r" or sys.argv[1] == "--random"):
		rows = 2
		cols = 2

		if len(sys.argv) > 2 and sys.argv[2].isdigit():
			rows = int(sys.argv[2])
			if rows <= 0:
				print "Invalid number of rows."	

		if len(sys.argv) > 3 and sys.argv[3].isdigit():
			cols = int(sys.argv[3])
			if cols <= 0:
				print "Invalid number of columns."	

		matrix = generateMatrix(rows, cols)
	else:
		matrix = readMatrix(sys.stdin)

	strToIntMatrix(matrix)
	printMatrix(matrix)

	print
	if numeric(matrix):
		pureEqs = findNashEquilibria(matrix)
		if pureEqs:
			print "pure equilibria:"
			for equilibrium in pureEqs:
				print "(p, q) = ", equilibriumToProbabilities(equilibrium)
		print

	mixed = findMixed(matrix)
	if mixed:
		print "mixed equilibria:"
		print "(p, q) = ", mixed
