import pygame
import random
import time
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
brown = (255, 255, 0)
colors = [red, green, blue, brown]
ul = 20
screenwidth = 30
screenheight = 35
board_x = 5
board_y = 5
boardwidth = 20
boardheight = 25
class Block():
	def __init__(self):
		pass
	def rotate(self, board):
		oldstate = self.state
		if self.state != 3:
			self.state += 1
		else:
			self.state = 0
		valid = True
		for i in xrange(4):
			x = (self.pos[0] + self.coords[self.state][i][0])
			y = (self.pos[1] + self.coords[self.state][i][1])
			if (y >= boardheight) or (y < 0) or ( x < 0) or (x >= boardwidth) or (board[y][x] is not -1):
				valid = False
				self.state = oldstate
				break
		return valid
	def moveLeft(self, board):
		self.pos[0] -= 1
		valid = True
		for i in xrange(4):
			x = (self.pos[0] + self.coords[self.state][i][0])
			y = (self.pos[1] + self.coords[self.state][i][1])
			if (x < 0) or (board[y][x] is not -1):
				valid = False
				self.pos[0] += 1
				break
		return valid
	def moveRight(self, board):
		self.pos[0] += 1
		valid = True
		for i in xrange(4):
			x = (self.pos[0] + self.coords[self.state][i][0])
			y = (self.pos[1] + self.coords[self.state][i][1])
			if (x >= boardwidth) or (board[y][x] is not -1):
				valid = False
				self.pos[0] -= 1
				break
		return valid
	def moveDown(self, board):
		self.pos[1] += 1
		valid = True
		for i in xrange(4):
			x = (self.pos[0] + self.coords[self.state][i][0])
			y = (self.pos[1] + self.coords[self.state][i][1])
			if (y >= boardheight) or (board[y][x] is not -1):
				valid = False
				self.pos[1] -= 1
				break
		return valid
	def draw(self):
		for i in xrange(4):
			x = (board_x + self.pos[0] + self.coords[self.state][i][0]) * ul
			y = (board_y + self.pos[1] + self.coords[self.state][i][1]) * ul
			pygame.draw.rect(screen, colors[self.ref], [x, y, ul, ul])
			pygame.draw.rect(screen, black, [x, y, ul, ul], 1)
	def drop(self, board):
		while self.moveDown(board) is True:
			True