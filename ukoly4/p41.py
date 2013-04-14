#! /usr/bin/env python

import sys

def load(filee):
	n = next(filee)
	fst = next(filee)
	snd = next(filee)

	try:
		n = int(n)
	except ValueError:
		print n, "is not integral."
		return None

	if n < 0:
		print n, "is smaller than 0"
		return None

	fst = map(float, fst.replace(" ", "").split(","))
	snd = map(float, snd.replace(" ", "").split(","))

	if n >= len(fst):
		print n, "is shorter than first sequence"
		return None

	if n >= len(snd):
		print n, "is shorter than second sequence"
		return None

	return n, fst, snd

def findD(n, playa, fst, snd):
	while n > 0:
		if playa == 0:
			if fst[n] + snd[n - 1] >= 1:
				return playa, n
		else:
			if snd[n] + fst[n - 1] >= 1:
				return playa, n
		n -= 1
		playa = 1 - playa
	return playa, n
			
if __name__ == "__main__":
	playa_names = ["A", "B"]

	n, fst, snd = load(sys.stdin)
	playa, d = findD(n, 0, fst, snd)
	print "Duel from distance %d with probabilities:" % n

	print " d     %s     %s" % (playa_names[0], playa_names[1])
	for x in range(0, n + 1):
		print "{0:2d} {1:1.3f} {2:1.3f}".format(x, fst[x], snd[x])
	print "Player %s shoots first at distance %d" % (playa_names[playa], d),
	p = fst[d] if playa == 0 else snd[d]
	print "with probability of hitting:", p
