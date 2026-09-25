import pygame 

pygame.init()
tela = pygame.display.set_mode((600, 400))
relogio = pygame.time.Clock()
emoji = pygame.font.SysFont("segoeuiemoji", 36)
passaro = emoji.render("\U0001F424", 1, "white")
passaro = pygame.transform.flip(passaro, True, False)
y = 200
vel = 0

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

    tela.fill("skyblue")                
    pos = passaro.get_rect(center=corpo.centr)