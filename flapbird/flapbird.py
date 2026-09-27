import pygame 
import random

pygame.init()
tela = pygame.display.set_mode((600, 400))
relogio = pygame.time.Clock()
emoji = pygame.font.SysFont("segoeuiemoji", 36)
passaro = emoji.render("\U0001F424", 1, "white")
passaro = pygame.transform.flip(passaro, True, False)
fonte = pygame.font.Font(None, 60)
y = 200
vel = 0
canos = []
quadro = 0
pontos = 0

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                vel = -9

    vel += 0.8
    y += vel
    corpo = pygame.Rect(100, y, 40, 34)

    quadro += 1
    if quadro % 45 == 0:
        buraco = random.randint(60, 250)
        canos.append(pygame.Rect(600, 0, 60, buraco))
        baixo = buraco + 140
        canos.append(pygame.Rect(600, baixo, 60, 400))
    for cano in canos:
        cano.x -= 4
        if cano.top == 0 and cano.right == 100:
            pontos += 1
    canos = [c for c in canos if c.right > 0]

    fora = corpo.top < 0 or corpo.bottom > 400
    if fora or corpo.collidelist(canos) >= 0:
        y, vel, pontos = 200, 0, 0
        canos.clear()            

    tela.fill("skyblue")
    for cano in canos:
        pygame.draw.rect(tela, "forestgreen", cano)
        pygame.draw.rect(tela, "darkgreen", cano, 4)                
    pos = passaro.get_rect(center=corpo.center)
    tela.blit(passaro, pos)
    placar = fonte.render(str(pontos), 1, "white")
    tela.blit(placar, placar.get_rect(midtop=(300, 15)))
    pygame.display.flip()
    relogio.tick(30)
    
pygame.quit()    