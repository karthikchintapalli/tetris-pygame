from board import *
from pieces import *
class Gameplay:
	def __init__(self):
		self.gameboard = Board()
		self.gameExit = False
		self.pieceactive = False
		self.activepiece = None
		self.score = 0
	def initGame(self):
		screen.fill(white)
		heading = headfont.render("Tetris", True, red)
		screen.blit(heading, [260, 150])
		tip = scorefont.render("Bonus : Achieve a row of a single color to clear the board!", True, blue)
		screen.blit(tip, [20, 200])
		cont = scorefont.render("Press ENTER to start game", True, black)
		screen.blit(cont, [200, 250])
		pygame.display.update()
		flag = 0
		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						flag = 1
						break
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			if flag == 1:
				break
		self.startGame()


	def startGame(self):
		while self.gameExit is False:
			if self.pieceactive is False:
				self.activepiece = self.selectPiece()
				pygame.time.set_timer(25, 500)
				self.pieceactive = True
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_a:
						self.activepiece.moveLeft(self.gameboard.board)
						self.gameboard.drawBoard()
						self.activepiece.draw()
					elif event.key == pygame.K_d:
						self.activepiece.moveRight(self.gameboard.board)
						self.gameboard.drawBoard()
						self.activepiece.draw()
					elif event.key == pygame.K_w:
						self.activepiece.rotate(self.gameboard.board)
						self.gameboard.drawBoard()
						self.activepiece.draw()
					elif event.key == pygame.K_SPACE:
						self.activepiece.drop(self.gameboard.board)
						self.gameboard.drawBoard()
						self.activepiece.draw()
				if event.type == 25:
					if self.activepiece.moveDown(self.gameboard.board) is False:
						for i in xrange(4):
							x = (self.activepiece.pos[0] + self.activepiece.coords[self.activepiece.state][i][0])
							y = (self.activepiece.pos[1] + self.activepiece.coords[self.activepiece.state][i][1])
							self.gameboard.board[y][x] = self.activepiece.ref
						if self.gameOver() is True:
							self.gameExit = True
						delrows = self.gameboard.checkRowFull()[0]
						homecount = self.gameboard.checkRowFull()[1]
						self.updateScore(delrows, homecount)
						self.gameboard.score = self.score
						self.gameboard.drawBoard()
						self.pieceactive = False
					else:
						self.gameboard.drawBoard()
						self.activepiece.draw()
				if event.type == pygame.QUIT:
					self.gameExit = True

			pygame.display.update()
			clock.tick(30)

		screen.fill(white)
		gameover = headfont.render("Game Over!", True, red)
		screen.blit(gameover, [220, 150])
		scordisp = scorefont.render("Your score was " + str(self.score), True, black)
		screen.blit(scordisp, [210, 200])
		pygame.display.update()
		time.sleep(3)
		pygame.quit()
		quit()

	def updateScore(self, delrows, homrows):
		self.score = self.score + 10 + delrows * 100
		if homrows is True:
			self.score += 500
	def gameOver(self):
		count = 0;
		for i in xrange(boardwidth):
			if self.gameboard.board[1][i] != -1:
				count += 1
		if count > 0:
			return True
		else:
			return False
		
	def selectPiece(self):
		x = random.random()
		x = x * 4
		if x >= 0 and x < 1:
			return SqPiece()
		if x >= 1 and x < 2:
			return LinePiece()
		if x >= 2 and x < 3:
			return KnightPiece()
		if x >= 3 and x <= 4:
			return JagPiece()	