from block import *
class SqPiece(Block):
	def __init__(self):
		self.ref = 0
		self.state = 0
		self.pos = [boardwidth / 2, 1]
		self.coords = [
		[[-1, -1], [0, -1], [0, 0], [-1, 0]],
		[[-1, -1], [0, -1], [0, 0], [-1, 0]],
		[[-1, -1], [0, -1], [0, 0], [-1, 0]],
        [[-1, -1], [0, -1], [0, 0], [-1, 0]]
		]
class LinePiece(Block):
	def __init__(self):
		self.ref = 1
		self.state = 0
		self.pos = [ boardwidth / 2,  1]
		self.coords = [
		[[-2, -1], [-1, -1], [0, -1], [1, -1]],
		[[0, -2], [0, -1], [0, 0], [0, 1]],
		[[-2, 0], [-1, 0], [0, 0], [1, 0]],
		[[-1, -2], [-1, -1], [-1, 0], [-1, 1]]
		]
class KnightPiece(Block):
	def __init__(self):
		self.ref = 2
		self.state = 0
		self.pos = [ boardwidth / 2,  1]
		self.coords = [
		[[-2, -1], [-1, -1], [0, -1], [0, 0]],
		[[0, -2], [0, -1], [0, 0], [-1, 0]],
		[[-1, -1], [-1, 0], [0, 0], [1, 0]],
		[[-1, -1], [0, -1], [-1, 0], [-1, 1]]
		]
class JagPiece(Block):
	def __init__(self):
		self.state = 0
		self.ref = 3
		self.pos = [ boardwidth / 2,  1]
		self.coords = [
		[[-1, -1], [0, -1], [0, 0], [1, 0]],
		[[0, -1], [-1, 0], [0, 0], [-1, 1]],
		[[-2, -1], [-1, -1], [-1, 0], [0, 0]],
		[[0, -2], [0, -1], [-1, -1], [-1, 0]]
		]
