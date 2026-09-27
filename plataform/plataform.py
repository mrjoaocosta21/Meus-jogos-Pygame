import pygame

pygame.init()
tela = pygame.display.set_mode((600, 400))
relogio = pygame.time.Clock()
jogador = pygame.Rect(45, 312, 28, 38)
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

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
    
