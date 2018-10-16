from pieces import *
from board import *
from block import *

def test_rotate_Line():
	board = Board()
	new_piece = LinePiece()
	new_piece.pos[1] = 5
	old_coords = new_piece.coords[new_piece.state]
	new_piece.rotate(board.board)
	new_piece.rotate(board.board)
	new_piece.rotate(board.board)
	new_piece.rotate(board.board)
	new_coords = new_piece.coords[new_piece.state]
	assert (old_coords == new_coords)

def test_rotate_Jag():
	board = Board()
	new_piece = JagPiece()
	new_piece.pos[1] = 5
	old_coords = new_piece.coords[new_piece.state]
	new_piece.rotate(board.board)
	new_piece.rotate(board.board)
	new_piece.rotate(board.board)
	new_piece.rotate(board.board)
	new_coords = new_piece.coords[new_piece.state]
	assert (old_coords == new_coords)

def test_rotate_Knight():
	board = Board()
	new_piece = KnightPiece()
	new_piece.pos[1] = 5
	old_coords = new_piece.coords[new_piece.state]
	new_piece.rotate(board.board)
	new_piece.rotate(board.board)
	new_piece.rotate(board.board)
	new_piece.rotate(board.board)
	new_coords = new_piece.coords[new_piece.state]
	assert (old_coords == new_coords)

def test_moveDown():
	board = Board()
	new_piece = LinePiece()
	old_y = new_piece.pos[1]
	new_piece.moveDown(board.board)
	new_y = new_piece.pos[1]
	assert (new_y == old_y + 1)

def test_moveLeft():
	board = Board()
	new_piece = SqPiece()
	old_x = new_piece.pos[0]
	new_piece.moveLeft(board.board)
	new_x = new_piece.pos[0]
	assert (new_x == old_x - 1)

def test_moveLeft_twice():
	board = Board()
	new_piece = SqPiece()
	old_x = new_piece.pos[0]
	new_piece.moveLeft(board.board)
	new_piece.moveLeft(board.board)
	new_x = new_piece.pos[0]
	assert (new_x == old_x - 2)

def test_moveRight():
	board = Board()
	new_piece = KnightPiece()
	old_x = new_piece.pos[0]
	new_piece.moveRight(board.board)
	new_x = new_piece.pos[0]
	assert (new_x == old_x + 1)

def test_drop():
	board = Board()
	new_piece = KnightPiece()
	new_piece.drop(board.board)
	old_y = new_piece.pos[1]
	new_piece.moveDown(board.board)
	new_y = new_piece.pos[1]
	assert (new_y == old_y)