import pygame
from random import randint
from pygame.locals import *
from sys import exit

pygame.init()

#tamanhos e larguras
largura = 640
altura = 480
x_cobra = largura/2
y_cobra = altura/2
movimento = 1.5
x_controle = movimento
y_controle = 0

x_maca = randint(40, 600)
y_maca = randint(50, 430)

#fonte
font = pygame.font.SysFont('arial', 25, True, True)
pontos = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake')
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 1
morreu = False

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 255,0), (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 1
    x_cobra = largura/2
    y_cobra = altura/2
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    lista_cabeca = []
    lista_cobra = []
    morreu = False

while True:
    relogio.tick(30)
    tela.fill((0,0,0))
    mensagem = f'Pontos {pontos}'
    texto_formatado = font.render(mensagem, True, (0,255,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if x_controle == movimento:
                    pass
                else:
                    x_controle = -movimento
                    y_controle = 0
            if event.key == K_RIGHT:
                if x_controle == -movimento:
                    pass
                else:
                    x_controle = movimento
                    y_controle = 0
            if event.key == K_UP:
                if y_controle == movimento:
                    pass
                else:
                    y_controle = -movimento
                    x_controle = 0
            if event.key == K_DOWN:
                if y_controle == -movimento:
                    pass
                else:
                    y_controle = movimento
                    x_controle = 0

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
    
    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra, y_cobra,20,20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca, y_maca, 15, 15))

    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        comprimento_inicial += 2
        movimento += .1
        
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) >1:
        font2 = pygame.font.SysFont('arial', 20, True, False)
        mensagem = 'Game Over! Pressione a Tecla R para jogar novamente'
        texto_formatado = font2.render(mensagem, True, (0,255,0))
        rect_texto = texto_formatado.get_rect()

        morreu = True
        while morreu: 
            tela.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()                   
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            rect_texto.center = (320,180)            
            tela.blit(texto_formatado, (rect_texto))
            pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]


    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (250, 2))
    pygame.display.update()
