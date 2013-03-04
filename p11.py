#! /usr/bin/env python

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
			
	
def printMatrix(matrix):
	for row in matrix:
		for col in row:
			print "%d,%d" % col,
		print
	print

def printEqulibria(matrix, strict):
	eqs = findNashEquilibria(matrix, strict)
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			c = '|' if (i, j) in eqs else ','
			print "%d%c%d" % (matrix[i][j][0], c, matrix[i][j][1]),
		print
	print
			

def findNashEquilibria(matrix, strict):
	m = len(matrix)
	assert(m > 0)
	n = len(matrix[0])

	row_maxs = [None] * m
	col_maxs = [None] * n

	for i in range(m):
		max_j = 0
		for j in range(n):
			if matrix[i][j][1] > matrix[i][max_j][1]:
				max_j = j
			elif not strict and matrix[i][j][1] == matrix[i][max_j][1]:
				max_j = j

		row_maxs[i] = max_j

	for j in range(n):
		max_i = 0
		for i in range(m):
			if matrix[i][j][0] > matrix[max_i][j][0]:
				max_i = i
			elif not strict and matrix[i][j][0] == matrix[max_i][j][0]:
				max_i = i
		col_maxs[j] = max_i

	equilibria = []
	for i, row_max in enumerate(row_maxs):
		if col_maxs[row_max] == i:
			equilibria += [(i, row_max)]

	print "Nash equilibria: ", equilibria
	return equilibria

		

if __name__ == "__main__":
	m = generateMatrix(5, 5)
	# m = [[(1,1),(0,0)],[(0,0),(1,1)]]
	printMatrix(m)
	strict = False
	printEqulibria(m, strict)
