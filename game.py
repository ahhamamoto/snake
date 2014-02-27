import pygame
import os
from pygame.locals import *

from food import *
from messages import *
from snake import *

SCREEN_DIMENSION = 800, 640

COLORS = {
		'black': (0, 0, 0),
		'white': (255, 255, 255),
		'red': (255, 0, 0),
		'green': (0, 255, 0),
		'blue': (0, 0, 255),
		'gray': (84, 84, 84)
}

class Game():
	def __init__(self):
		self.clock = pygame.time.Clock()
		os.environ['SDL_VIDEO_CENTERED'] = '1'

		pygame.init()
		pygame.display.set_caption('Snake')
		self.screen = pygame.display.set_mode(SCREEN_DIMENSION)
		self.surface = pygame.image.load('background.png').convert()
		pygame.mouse.set_visible(False)

		self.snake = Snake()
		self.food = []
		self.messages = Messages()

	def main(self):
		self.food.append(Food())
		while True:
			self.clock.tick()

			self.snake.set_direction()

			for f in self.food:
				self.snake.eaten_food(f)

			self.snake.update()

			self.screen.blit(self.surface, (0, 0))
			self.screen.fill(COLORS['white'], (0, 0, SCREEN_DIMENSION[0], 32))
			# screen.fill(color['gray'], (0, 32, 960, 608))
			for f in self.food:
				f.draw(self.screen)
			self.snake.draw(self.screen)

			# checa se a cobra esta viva
			if not self.snake.alive:
				if self.snake.score > self.messages.data['max_score']:
					self.messages.update_max_score(self.snake.score)
				self.snake = Snake()
				self.food = []
				self.food.append(Food())
				pygame.time.wait(500)
				self.messages.update_deaths()

			self.check_eaten()

			if len(self.food) < self.snake.food_number:
				self.food.append(Food())

			self.messages.update_time()
			self.messages.update_score(self.snake.score)
			self.messages.update_speed(self.snake.speed)
			self.messages.draw(self.screen)
			
			pygame.display.flip()
			pygame.time.wait(self.snake.speed)

	def check_eaten(self):
		for f in self.food:
			if f.eaten:
				f.grow()

