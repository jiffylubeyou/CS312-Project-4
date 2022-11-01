#!/usr/bin/python3

from which_pyqt import PYQT_VER
if PYQT_VER == 'PYQT5':
	from PyQt5.QtCore import QLineF, QPointF
elif PYQT_VER == 'PYQT4':
	from PyQt4.QtCore import QLineF, QPointF
else:
	raise Exception('Unsupported Version of PyQt: {}'.format(PYQT_VER))

import math
import time
import random

# Used to compute the bandwidth for banded version
MAXINDELS = 3

# Used to implement Needleman-Wunsch scoring
MATCH = -3
INDEL = 5
SUB = 1

class GeneSequencing:

	def __init__( self ):
		pass
	
# This is the method called by the GUI.  _seq1_ and _seq2_ are two sequences to be aligned, _banded_ is a boolean that tells
# you whether you should compute a banded alignment or full alignment, and _align_length_ tells you 
# how many base pairs to use in computing the alignment

	def align( self, seq1, seq2, banded, align_length):
		self.banded = banded
		self.MaxCharactersToAlign = align_length

		seq1Array = []
		seq1Array.append(None)
		seq2Array = []
		seq2Array.append(None)
		for char in seq1:
			seq1Array.extend(char)
		for char in seq2:
			seq2Array.extend(char)
		E = [[Node() for x in range(len(seq2Array))] for y in range(len(seq1Array))]
		Edit(seq1Array, seq2Array, E)





###################################################################################################
# your code should replace these three statements and populate the three variables: score, alignment1 and alignment2
		score = E[-1][-1].data
		alignment1 = 'abc-easy  DEBUG:({} chars,align_len={}{})'.format(
			len(seq1), align_length, ',BANDED' if banded else '')
		alignment2 = 'as-123--  DEBUG:({} chars,align_len={}{})'.format(
			len(seq2), align_length, ',BANDED' if banded else '')
###################################################################################################					
		
		return {'align_cost':score, 'seqi_first100':alignment1, 'seqj_first100':alignment2}


def Edit(x, y, E):
	for i in range(len(x)):
		E[i][0].data = i
	for j in range(len(y)):
		E[0][j].data = j
	for i in range(1, len(x)):
		for j in range(1, len(y)):
			subNumber = 0
			if x[i] == y[j]:
				subNumber = E[(i-1)][(j-1)].data - 3
			else:
				subNumber = E[(i-1)][(j-1)].data + 1
			addNumber = E[i][j - 1].data + 5
			deleteNumber = E[i - 1][j].data + 5
			# This finds the minimum of the three
			minimum = subNumber
			if addNumber < minimum:
				minimum = addNumber
			if deleteNumber < minimum:
				minimum = deleteNumber
			# You have minimum number now write in number
			if minimum == subNumber:
				E[i][j].data = subNumber
				E[i][j].backPath = E[i - 1][j - 1]
				E[i][j].backDirection = "diagonal"
			elif minimum == addNumber:
				E[i][j].data = addNumber
				E[i][j].backPath = E[i][j - 1]
				E[i][j].backDirection = "left"
			elif minimum == deleteNumber:
				E[i][j].data = deleteNumber
				E[i][j].backPath = E[i - 1][j]
				E[i][j].backDirection = "up"
			else:
				print("Something ain't right here")







class Node(object):
	def __init__(self):
		self.data = 0
		self.backPath = None
		self.backDirection = None