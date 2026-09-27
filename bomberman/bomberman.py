import pygame
import random

pygame.init()
tela = pygame.display.set_mode((600, 400))
relogio = pygame.time.Clock()
T = 40
paredes = []
caixas = []
for y in range(10):
    for x in range(15):
        r = pygame.Rect(x * T, y * T, T, T)
        if x in (0, 14) or y in (0, 9):
            paredes.append(r)
        elif x % 2 == 0 and y % 2 == 0:
            paredes.append(r)
        elif random.random() < 0.5 and x + y > 3: 
            caixas.append(r)
jogador = pygame.Rect(T, T, T, T)
setas = {
    pygame.K_LEFT: (-1, 0), pygame.K_RIGHT: (1, 0),
    pygame.K_UP: (0, -1), pygame.K_DOWN: (0, 1),
}
bombas = []
fogo = []

def explodir(centro, fim):
    fogo.append([centro, fim])
    for dx, dy in setas.values():
        for n in (1, 2):
            r = centro.move(dx * T * n, dy * T * n)
            if r.colidelist(paredes) >= 0:
                break
            fogo.append([r, fim])
            i = r.collidelist(caixas)
            if i >= 0:
                caixas.pop(i)
                break

rodando = True
while rodando:
    agora = pygame.time.get_ticks()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key in setas:
                dx, dy = setas[evento.key]
                novo = jogador.move(dx * T, dy * T)
                if novo.collidelist(paredes + caixas) < 0:
                    jogador = novo
            if evento.key == pygame.K_SPACE:
                bombas.append([jogador, agora + 2000])

    for bomba in bombas[:]:
        if agora >= bomba[1]:
            bombas.remove(bomba)
            explodir(bomba[0], agora + 500)
    fogo = [f for f in fogo if f[1] > agora]
    if jogador.collidelist([f[0] for f in fogo]) >= 0:
        jogador = pygame.Rect( T, T, T, T)                              

    tela.fill("forestgreen")
    for r in paredes:
        pygame.draw.rect(tela, "slategray", r)
    for r in caixas:
        pygame.draw.rect(tela, "peru", r, 0, 6)
    for r, fim in bombas:
        raio = 13 + agora // 200 % 2 * 4
        pygame.draw.circle(tela, "black", r.center, raio)
        faisca = (r.centerx + 9, r.top + 7)
        pygame.draw.circle(tela, "yellow", faisca, 5)
    for r, fim in fogo:
        pygame.draw.rect(tela,"orange", r)
        pygame.draw.circle(tela, "yellow", r.center, 14)    
    pygame.draw.rect(tela, "deepskyblue", jogador, 0, 12)
    for lado in (-8, 8):
        olho = jogador.move(lado, -4).center
        pygame.draw.circle(tela, "black", olho, 4)        
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()                            