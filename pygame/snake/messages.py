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

class Messages():
	def __init__(self):
		self.data = {'deaths': 0, 'time': time.time(), 'max_score': 0}
		self.font = pygame.font.Font( pygame.font.get_default_font(), 16)
		self.messages = {
			'time': self.font.render('Time elapsed: ' + str(0), 1, COLORS['black']),
			'speed': self.font.render('Speed: ' + str(0), 1, COLORS['black']),
			'deaths': self.font.render('Deaths: ' + str(0), 1, COLORS['black']),
			'score': self.font.render('Score: ' + str(0), 1, COLORS['black']),
			'max_score': self.font.render('Max Score: ' + str(0), 1, COLORS['black'])
		}

	def update_time(self):
		self.messages['time'] = self.font.render('Time elapsed: ' + str(int(time.time() - self.data['time'])), 1, COLORS['black'])

	def update_speed(self, speed):
		self.messages['speed'] = self.font.render('Speed: ' + str((100 - speed) / 5), 1, COLORS['black'])

	def update_deaths(self):
		self.data['deaths'] += 1
		self.messages['deaths'] = self.font.render('Deaths: ' + str(self.data['deaths']), 1, COLORS['black'])

	def update_score(self, score):
		self.messages['score'] = self.font.render('Score: ' + str(score), 1, COLORS['black'])

	def update_max_score(self, score):
		self.data['max_score'] = score
		self.messages['max_score'] = self.font.render('Max Score: ' + str(self.data['max_score']), 1, COLORS['black'])

	def draw(self, screen):
		screen.blit(self.messages['time'], (15, 8))
		screen.blit(self.messages['speed'], (180, 8))
		screen.blit(self.messages['deaths'], (314, 8))
		screen.blit(self.messages['score'], (450, 8))
		screen.blit(self.messages['max_score'], (628, 8))
