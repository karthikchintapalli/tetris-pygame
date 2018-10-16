from block import *
class Board():
	def __init__(self):
		self.board = [[-1 for x in xrange(boardwidth)] for y in xrange(boardheight)]
		self.score = 0
	def fillPiecePos(self):
		for i in xrange (boardheight):
			for j in xrange(boardwidth):
				if self.board[i][j] != -1:
					x = (board_x + j) * ul
					y = (board_y + i) * ul
					pygame.draw.rect(screen, colors[self.board[i][j]], [x, y, ul, ul])
					pygame.draw.rect(screen, black, [x, y, ul, ul], 1)

	def drawBoard(self):
		screen.fill(white)
		heading = headfont.render("Tetris", True, red)
		screen.blit(heading, [260, 30])
		pygame.draw.rect(screen, black, [board_x * ul, board_y * ul, boardwidth * ul, boardheight * ul], 1)
		scordisp = scorefont.render("Score : " + str(self.score), True, black)
		screen.blit(scordisp, [270, 630])
		self.fillPiecePos()

	def checkRowFull(self):
		delcount = 0
		for i in xrange (boardheight):
			count = 0
			homcount = True
			color = None
			for j in xrange(boardwidth):
				if self.board[i][j] is -1:
					count += 1
				if j == 0:
					color = self.board[i][j]
				else:
					if self.board[i][j] != color:
						homcount = False
			if count == 0:
				if homcount is True:
					self.board = [[-1 for x in xrange(boardwidth)] for y in xrange(boardheight)]
					break
				else:		
					delcount += 1
					del self.board[i]
					self.board.insert(0, [-1 for x in xrange(boardwidth)])
		return [delcount, homcount]