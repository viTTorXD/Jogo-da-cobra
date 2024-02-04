import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configuraç~~~~ões do jogo
largura, altura = 640, 480
tamanho_ceula = 20
cor_cobra = (0, 255, 0)
cor_comida = (250, 0, 0)

# Função paeadesenhar a cobra

def desenhar_cobra(cobra):
    for segmento in cobra:
        pygame.draw.rect(screen, cor_cobra, (segmento[0], segmento[1], tamanho_ceula, tamanho_ceula))

# Função para desenhar a comida
def desenhar_comida(comida):
    pygame.draw.pygame.draw.rect(screen, cor_comida, (comida[0], comida[1], tamanho_ceula, tamanho_ceula))

# Função principal do jogo
def jogo():
    clock = pygame.time.Clock()

    # Posição inicial da comida
    comida = (random.randrange(0,largura // tamanho_ceula) * tamanho_ceula)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direcao != (0, 1):
                    direcao = (0, -1)
                elif event.key == pygame.K_DOWN and direcao != (0, -1):
                    direcao = (0, 1)
                elif event.key == pygame.K_LEFT and direcao != (1, 0):
                    direcao = (-1, 0)
                elif event.key == pygame.K_RIGHT and direcao != (-1, 0):
                    direcao = (1, 0)

                    #  Move a cobra
                    cobra = [(cobra[0][0] + direcao[0] * tamanho_ceula, cobra[0][1] + direcao[1] * tamanho_ceula)] + cobra[:-1]

                    # Verificar colisões 
                    if cobra[0] == comida:
                        comida = (random.randrange(0, largura // tamanho_ceula) * tamanho_ceula, random.randrange(0, altura // tamanho_ceula) * tamanho_ceula) 
                        cobra.append(cobra[-1])
                        
                        # Verifica se a cobra colidiu consigo mesma ou com as bordas
        if (cobra[0] in cobra[1:] or
            cobra[0][0] < 0 or cobra[0][0] >= largura or
            cobra[0][1] < 0 or cobra[0][1] >= altura):
            pygame.quit()
            sys.exit()

        # Desenha na tela
        screen.fill((0, 0, 0))
        desenhar_cobra(cobra)
        desenhar_comida(comida)
        pygame.display.flip()

        # Limita a taxa de quadros
        clock.tick(10)

# Inicializa a tela
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha')

# Inicia o jogo
jogo()