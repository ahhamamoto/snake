import random

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
    """Classe da comida que nasce no jogo."""

    def __init__(self, color=(255, 225, 255), size=16, width=800, height=640):
        """Construtor, inicia valores de dimensao da janela,
        cor e se foi comido."""
        self.window_width = width
        self.window_height = height
        self.color = color
        self.size = size
        self.eaten = False
        self.calculate_position()
        self.position_x = None
        self.position_y = None

    # desenha comida na tela
    def draw(self, surf):
        """Renderiza a comida na janela."""
        surf.fill(self.color, (self.position_x,
                               self.position_y, self.size, self.size))

    def grow(self):
        """Metodo que faz a comida nascer de novo se for comida."""
        self.calculate_position()
        self.eaten = False

    def calculate_position(self):
        """Calcula a proxima posicao da comida."""
        self.position_x = random.randrange(0,
                                           self.window_width / self.size) * 16
        self.position_y = random.randrange(0,
                                           self.window_height / self.size) * 16

        if self.position_y < 32:
            self.position_y += 32
