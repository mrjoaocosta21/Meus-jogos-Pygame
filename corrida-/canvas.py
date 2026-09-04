"""
Painel visual de UM algoritmo dentro da corrida.

Cada Panel desenha, dentro de um retângulo (x, y, largura, altura) da
tela, as barras correspondentes ao estado atual da lista daquele
algoritmo, destacando os índices em comparação/troca.
"""

import pygame

BLACK = (18, 18, 18)
WHITE = (235, 235, 235)
BAR_COLOR = (90, 140, 220)
HIGHLIGHT_COLOR = (240, 90, 90)
DONE_COLOR = (90, 210, 130)
GRID_LINE = (60, 60, 60)


class Panel:
    def __init__(self, name, rect, data):
        self.name = name
        self.rect = rect  # (x, y, w, h)
        self.data = data
        self.highlighted = []
        self.finished = False
        self.steps = 0
        self.finish_time = None

    def update(self, data, highlighted):
        self.data = data
        self.highlighted = highlighted
        self.steps += 1

    def mark_finished(self, elapsed):
        self.finished = True
        self.finish_time = elapsed

    def draw(self, screen, font, start_time):
        x, y, w, h = self.rect
        pygame.draw.rect(screen, GRID_LINE, (x, y, w, h), 1)

        n = len(self.data)
        if n == 0:
            return

        bar_w = w / n
        max_val = max(self.data) if max(self.data) > 0 else 1

        for i, value in enumerate(self.data):
            bar_h = (value / max_val) * (h - 30)
            bar_x = x + i * bar_w
            bar_y = y + h - bar_h - 20

            color = BAR_COLOR
            if self.finished:
                color = DONE_COLOR
            elif i in self.highlighted:
                color = HIGHLIGHT_COLOR

            pygame.draw.rect(screen, color, (bar_x, bar_y, max(bar_w - 1, 1), bar_h))

        label = f"{self.name}  |  passos: {self.steps}"
        if self.finished:
            label += f"  |  {self.finish_time:.2f}s"
        text_surf = font.render(label, True, WHITE)
        screen.blit(text_surf, (x + 6, y + 4))


def add_zeros(number, desired_length):
    """Preenche `number` com zeros à esquerda até `desired_length` dígitos."""
    number_str = str(number)
    zeros_to_add = max(0, desired_length - len(number_str))
    if number_str.startswith("-"):
        return "-" + "0" * zeros_to_add + number_str[1:]
    return "0" * zeros_to_add + number_str