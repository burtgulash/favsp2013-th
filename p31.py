#! /usr/bin/python

import sys

class TreeNode:
	player_ids = {}
	next_id = 0

	def __init__(self, name, parent, player):
		self.name = name
		self.parent = parent
		self.children = {}
		self.best = [0, 0]
		self.equilibrium = [self.name]

		self.player = player
		if player not in TreeNode.player_ids:
			TreeNode.player_ids[player] = TreeNode.next_id
			TreeNode.next_id += 1

	def addChild(self, child, player):
		self.children[child] = TreeNode(child, self, player)
		return self.children[child]

	def is_leaf(self):
		return len(self.children) == 0

	def getChildren(self):
		return self.children.values()

	def getPlayerId(self):
		return TreeNode.player_ids[self.player]

def parseLine(line):
	parts = line.strip(" \n").split(":")

	payoffs = None
	if len(parts) == 3:
		payoffs = parts[2].split(",")
		payoffs = map(int, payoffs)
		# todo check int

	return parts[0], parts[1], payoffs

def loadTree(filee):
	parts = parseLine(next(filee))
	tree = TreeNode(parts[0], None, parts[1])
	indent = 0

	for line in filee:
		cur_indent = 0
		for c in line:
			if c != " ":
				break
			cur_indent += 1

		parts = parseLine(line)
		child_name = parts[0]
		player = parts[1]

		if cur_indent > indent:
			tree = tree.addChild(child_name, player)
		elif cur_indent == indent:
			tree = tree.parent.addChild(child_name, player)
		else:
			for i in range(indent - cur_indent):
				tree = tree.parent
			tree = tree.parent.addChild(child_name, player)

		tree.player = parts[1]
		if parts[2]:
			tree.best = parts[2]

		indent = cur_indent

	while tree.parent is not None:
		tree = tree.parent

	return tree


def printNode(treeNode, lvl):
	print " " * lvl,
	print treeNode.name, treeNode.player, treeNode.best
	for child in treeNode.getChildren():
		printNode(child, lvl + 1)

def printTree(tree):
	printNode(tree, 0)

def backInduction(treeNode):
	if not treeNode.is_leaf():
		for child in treeNode.getChildren():
			backInduction(child)

		best, best_child = 0, None # -inf
		for child in treeNode.getChildren():
			if child.best[treeNode.getPlayerId()] > best:
				best, best_child = child.best[treeNode.getPlayerId()], child
		
		treeNode.best = best_child.best
		treeNode.equilibrium = [treeNode.name] + best_child.equilibrium


if __name__ == "__main__":
	tree = loadTree(sys.stdin)
	backInduction(tree)
	printTree(tree)
	print "Subgame Perfect Nash Equilibrium:", tree.equilibrium
