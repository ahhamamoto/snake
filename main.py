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

from game import *

SCREEN_DIMENSION = 800, 640

COLORS = {
		'black': (0, 0, 0),
		'white': (255, 255, 255),
		'red': (255, 0, 0),
		'green': (0, 255, 0),
		'blue': (0, 0, 255),
		'gray': (84, 84, 84)
	}


if __name__ == '__main__':
	game = Game()
	game.main()
