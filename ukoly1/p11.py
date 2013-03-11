#! /usr/bin/python

import sys
from random import randint

def randomPair():
	maxValue = 9
	return (randint(0, maxValue), randint(0, maxValue))

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
	

def findDominatingRows(matrix):
	m = len(matrix)
	assert(m > 0)
	n = len(matrix[0])

	dominating_row = None
	dominatings = []
	for i in range(m):
		s_dom = True
		dom = True
		for j in range(m):
			if i != j:
				for k in range(n):
					if matrix[i][k][0] <= matrix[j][k][0]:
						s_dom = False
					if matrix[i][k][0] < matrix[j][k][0]:
						dom = False
		if s_dom:
			dominating_row = i
		if dom:
			dominatings += [i]
	return dominating_row, dominatings
	

def printMatrix(matrix):
	m = len(matrix)
	assert(m > 0)
	n = len(matrix[0])

	matrix_t = transpose(matrix)
	
	dr, drs = findDominatingRows(matrix)
	dc, dcs = findDominatingRows(matrix_t)
	eqs = findNashEquilibria(matrix)


	print "   ",
	for j in range(n):
		print " ++" if j == dc else " + " if j in dcs else " - ",
	print
	
	for i in range(m):
		print " ++" if i == dr else "  +" if i in drs else "  -",
		for j in range(n):
			c = '|' if (i, j) in eqs else ','
			print "%d%c%d" % (matrix[i][j][0], c, matrix[i][j][1]),
		print
	print

def readMatrix(filee):
	matrix = []

	row_len = -1
	for line in filee:
		row = []
		for pair in line.split():
			nums = [int(s) for s in pair.split(",") if s.isdigit()]
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

	printMatrix(matrix)
