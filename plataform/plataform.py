import pygame

pygame.init()
tela = pygame.display.set_mode((600, 400))
relogio = pygame.time.Clock()
MUNDO = 1200
jogador = pygame.Rect(45, 312, 28, 38)
plataformas = [
    pygame.Rect(150, 280, 120, 18),
    pygame.Rect(310, 220, 105, 18),
    pygame.Rect(450, 275, 150, 18),
    pygame.Rect(610, 220, 110, 18),
    pygame.Rect(770, 275, 105, 18),
    pygame.Rect(920, 225, 110, 18),
]
inimigos = [
    {"corpo": pygame.Rect(500, 253, 26, 22),
     "base": plataformas[2], "vel":1},
    {"corpo": pygame.Rect(800, 253, 26, 22),
     "base": plataformas[4], "vel":-1},
]
moedas = [
    pygame.Rect(202, 244, 18, 18),
    pygame.Rect(348, 182, 18, 18),
    pygame.Rect(555, 222, 18, 18),
    pygame.Rect(652, 184, 18, 18),
    pygame.Rect(812, 239, 18, 18),
    pygame.Rect(960, 189, 18, 18),
]
meta = pygame.Rect(1135, 315, 6, 35)
pontos = 0
ganhou = False
fonte = pygame.font.Font(None, 35)
vel_y = 0
no_chao = True
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and no_chao:
                vel_y = -12
                no_chao = False
    teclas = pygame.key.get_pressed()
    jogador.x += 4 * (teclas[pygame.K_RIGHT] - teclas[pygame.K_LEFT])
    jogador.x = max(0, min(572, jogador.x))
    vel_y = min(12, vel_y + 0.7)
    jogador.y += round(vel_y)
    no_chao = False
    if jogador.bottom >= 350:
        jogador.bottom = 350
        vel_y = 0
        no_chao = True                

    tela.fill("#83D4F5")
    pygame.draw.rect(tela, "#9B684B", (0, 350, 600, 50))
    pygame.draw.rect(tela, "#64C85F", (0, 345, 600, 9))
    pygame.draw.rect(tela, "#E0403A", jogador)
    pygame.draw.rect(tela, "#346A9A", (jogador.x, jogador.y+22, 28, 16))
    pygame.draw.circle(tela, "#FFE0A0", (jogador.x+14, jogador.y+13), 9)
    pygame.draw.rect(tela, "#E0403A", (jogador.x+4, jogador.y, 21, 7))
    pygame.draw.rect(tela, "#E0403A", (jogador.x+14, jogador.y+4, 17, 4))
    pygame.draw.rect(tela, "#5A3A2A", (jogador.x+13, jogador.y+17, 12, 3))
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()    
    
