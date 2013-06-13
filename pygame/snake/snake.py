# Autor: Anderson Hiroshi Hamamoto
# Snake 

# a implementar
# (DONE) - conforme o jogador vai pegando mais speed, brota mais de uma comida por vez
#          ou spawnar comida de acordo com o tempo
# 	       * comida nascer dentro da cobra e dentro de outras comidas
# (DONE) - nao deixa o jogador ir na direcao oposta
# - colocar pra cobra atravessar para o outro lado da tela
# (DONE) - colocar o score na tela ou apos o jogador morrer
# (FAIL) - colocar uma borda no jogo

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

class Snake():
	
	def __init__(self, direction=90, color=(0, 255, 0), size=16, x=416, y=336, width=960, height=640, length=3):
		self.count = 0
		self.food_number = 1
		self.speed = 100
		self.speed_inc = 10
		self.score = 0
		self.deaths = 0
		self.alive = True
		self.color = color
		self.size = size
		self.default_length = length
		self.body_list = []
		self.default_direction = direction
		self.default_head = [x, y]

		self.length = self.default_length
		self.direction = self.default_direction
		self.head = self.default_head

	# era pra resetar as variaveis e a cobra comecar de novo
	# mas nao funciona
	def reset(self):
		self.length = self.default_length
		self.direction = self.default_direction
		self.head = self.default_head
		self.body_list = []
		self.alive = True
		print self.head

	# faz um update na cobra, direcao que esta indo
	# e os pontos que fazem parte do corpo e checa
	# se ele bateu nele mesmo ou na borda
	def update(self):
		self.body_list.insert(0, list(self.head))
		if len(self.body_list) > self.length:
			self.body_list.pop()

		if self.direction == 0:
			self.head[1] -= self.size
		if self.direction == 90:
			self.head[0] -= self.size
		if self.direction == 180:
			self.head[1] += self.size
		if self.direction == 270:
			self.head[0] += self.size

		for position in self.body_list:
			if self.head == position:
				self.alive = False

		if self.head[0] not in range(SCREEN_DIMENSION[0]):
			self.alive = False
		elif self.head[1] not in range(32, SCREEN_DIMENSION[1]):
			self.alive = False

		# desenha a cobra na tela
	def draw(self, surf):
		surf.fill(self.color, (self.head[0], self.head[1], self.size, self.size))

		for position in self.body_list:
			surf.fill(self.color, (position[0], position[1], self.size, self.size))

	# pega a direcao da cobra de acordo com o evento
	# do teclado
	def set_direction(self):
		last_direction = self.direction
		for e in pygame.event.get():
			if e.type == QUIT:
				pygame.quit()
				sys.exit()
			if e.type == KEYDOWN:
				if e.key == K_UP and last_direction != 180:
					self.direction = 0
				if e.key == K_LEFT and last_direction != 270:
					self.direction = 90
				if e.key == K_DOWN and last_direction != 0:
					self.direction = 180
				if e.key == K_RIGHT and last_direction != 90:
					self.direction = 270
				if e.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
				# last_direction = self.direction

	# verifica se a cobra comeu a comidinha
	def eaten_food(self, food):
		if self.head[0] == food.x and self.head[1] == food.y:
			food.eaten = True
			self.score += 110 - self.speed
			self.length += 1
			self.count += 1
			if self.count % 10 == 0 and self.speed != 30:
				self.speed -= self.speed_inc
				self.food_number += 1
