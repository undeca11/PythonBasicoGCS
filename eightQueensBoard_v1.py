import pygame
import sys

# Configurações
TAM_CELULA = 60  # Tamanho de cada célula do tabuleiro
NUM_RAINHAS = 8
LARGURA = TAM_CELULA * NUM_RAINHAS
ALTURA = TAM_CELULA * NUM_RAINHAS

# Solução fixa para as 8 rainhas (linha por coluna)
# Cada valor representa a linha da rainha na respectiva coluna
solucao = [0, 4, 7, 5, 2, 6, 1, 3]

pygame.init()
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Problema das 8 Rainhas")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

def desenhar_tabuleiro():
    for linha in range(NUM_RAINHAS):
        for coluna in range(NUM_RAINHAS):
            if (linha + coluna) % 2 == 0:
                cor = BRANCO
            else:
                cor = PRETO
            rect = pygame.Rect(coluna * TAM_CELULA, linha * TAM_CELULA, TAM_CELULA, TAM_CELULA)
            pygame.draw.rect(screen, cor, rect)

def desenhar_rainhas():
    for coluna, linha in enumerate(solucao):
        center_x = coluna * TAM_CELULA + TAM_CELULA // 2
        center_y =  linha * TAM_CELULA + TAM_CELULA // 2
        radius   = TAM_CELULA // 3
        pygame.draw.circle(screen, VERMELHO, (center_x, center_y), radius)

def main():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        desenhar_tabuleiro()
        desenhar_rainhas()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()