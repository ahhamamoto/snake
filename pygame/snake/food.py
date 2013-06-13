import pygame
import os
import sys
import random
import time
from pygame.locals import *

SCREEN_DIMENSION = 800, 640

COLORS = {
		'black': (0, 0, 0),
		'white': (255, 255, 255),
		'red': (255, 0, 0),
		'green': (0, 255, 0),
		'blue': (0, 0, 255),
		'gray': (84, 84, 84)
}

class Food():
	def __init__(self, color=(255, 225, 255), size=16, width=960, height=640):
		self.color = color
		self.size = size
		self.eaten = False
		self.calculate_position()

	# desenha comida na tela
	def draw(self, surf):
		surf.fill(self.color, (self.x, self.y, self.size, self.size))

	def grow(self):
		self.calculate_position()
		self.eaten = False

	def calculate_position(self):
		self.x = random.randrange(0, SCREEN_DIMENSION[0] / self.size) * 16
		self.y = random.randrange(0, SCREEN_DIMENSION[1] / self.size) * 16

		if self.y < 32:
			self.y += 32