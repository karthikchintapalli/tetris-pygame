from board import *

def test_checkRowFull_normal():
	board = Board()
	for i in xrange(boardwidth):
		board.board[5][i] = 1
	board.checkRowFull()
	check_row = [board.board[5][i] for i in xrange(boardwidth)]
	assert (check_row == [-1 for i in xrange(boardwidth)])

def test_checkRowFull_bonus():
	board = Board()
	for i in xrange(boardwidth):
		board.board[5][i] = 1
		board.board[6][i] = i % 3
	board.checkRowFull()
	assert (board.board == [[-1 for x in xrange(boardwidth)] for y in xrange(boardheight)])