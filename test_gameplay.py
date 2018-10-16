from gameplay import *

def test_selectPiece():
	game = Gameplay()
	piece = game.selectPiece()
	assert (isinstance(piece, SqPiece) or isinstance(piece, LinePiece) or isinstance(piece, KnightPiece) or isinstance(piece, JagPiece))

def test_updateScore():
	game = Gameplay()
	game.score = 100
	game.updateScore(2, True)
	assert(game.score == 810)
