"""
Corrida de algoritmos de ordenação — ideia baseada no vídeo:
"Fiz algoritmos de ordenação competirem entre si."

Cada algoritmo recebe a MESMA lista embaralhada (para ser justo),
e todos avançam ao mesmo tempo, um passo por frame, em painéis lado
a lado. O primeiro a terminar vence a corrida.

Controles:
  ESPAÇO  -> pausa / retoma
  R       -> reinicia a corrida com uma nova lista aleatória
  1-9     -> ajusta quantos passos cada algoritmo dá por frame (velocidade)
  ESC     -> sai
"""

import random
import time

import pygame

from canvas import Panel, BLACK, WHITE
from sorting import ALGORITHMS

DATA_LENGTH = 60
WINDOW_W, WINDOW_H = 1200, 800
STEPS_PER_FRAME = 2

# Bogo sort só entra na corrida se a lista for pequena, senão nunca termina.
RACE_ALGORITHMS = {k: v for k, v in ALGORITHMS.items() if k != "Bogo Sort"}


def make_grid(n_panels, margin=10, header=40):
    """Calcula um grid (linhas x colunas) que caiba n_panels na janela."""
    cols = 3 if n_panels > 4 else 2
    rows = (n_panels + cols - 1) // cols

    cell_w = (WINDOW_W - margin * (cols + 1)) // cols
    cell_h = (WINDOW_H - header - margin * (rows + 1)) // rows

    rects = []
    for idx in range(n_panels):
        row, col = divmod(idx, cols)
        x = margin + col * (cell_w + margin)
        y = header + margin + row * (cell_h + margin)
        rects.append((x, y, cell_w, cell_h))
    return rects


def new_race(steps_per_frame):
    base_data = [random.random() for _ in range(DATA_LENGTH)]

    panels = {}
    generators = {}
    rects = make_grid(len(RACE_ALGORITHMS))

    for (name, algo_fn), rect in zip(RACE_ALGORITHMS.items(), rects):
        data_copy = list(base_data)
        panels[name] = Panel(name, rect, data_copy)
        generators[name] = algo_fn(data_copy)

    return panels, generators, time.time()


def main():
    pygame.init()
    pygame.display.set_caption("Corrida de algoritmos de ordenação")
    screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 16)
    title_font = pygame.font.SysFont("consolas", 22, bold=True)

    steps_per_frame = STEPS_PER_FRAME
    panels, generators, start_time = new_race(steps_per_frame)
    finished_order = []
    paused = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_r:
                    panels, generators, start_time = new_race(steps_per_frame)
                    finished_order = []
                elif pygame.K_1 <= event.key <= pygame.K_9:
                    steps_per_frame = event.key - pygame.K_0

        if not paused:
            for name, gen in list(generators.items()):
                panel = panels[name]
                if panel.finished:
                    continue
                for _ in range(steps_per_frame):
                    try:
                        state, highlighted = next(gen)
                        panel.update(state, highlighted)
                    except StopIteration:
                        panel.mark_finished(time.time() - start_time)
                        finished_order.append(name)
                        break

        screen.fill(BLACK)

        title = f"Corrida de Ordenação — {DATA_LENGTH} elementos  |  ESPACO=pausa  R=reiniciar  1-9=velocidade"
        screen.blit(title_font.render(title, True, WHITE), (10, 8))

        for panel in panels.values():
            panel.draw(screen, font, start_time)

        if finished_order:
            ranking = "Ranking: " + " > ".join(finished_order)
            screen.blit(font.render(ranking, True, WHITE), (10, WINDOW_H - 24))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()