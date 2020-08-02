from snake import Snake
from mapa import Mapa, X, Y

import pygame

COR_BACKGROUND = (40,43,46)

def game_loop():
    """ Main do jogo """
    # Ler mapa :
    with open("mapa.txt") as ficheiro:
        tamanho = eval(ficheiro.readline())
        paredes = eval(ficheiro.readline())

    # Inicialização do mapa
    pos_inicial = [tamanho[X] // 2, tamanho[Y] // 2] 
    cobra = Snake([pos_inicial, [pos_inicial[X], pos_inicial[Y] - 1]])

    mapa = Mapa(tamanho[X], tamanho[Y], cobra, paredes, False)

    # Game loop :
    a_correr = True

    # Ecrã
    tamanho = (800, 800)
    ecra = pygame.display.set_mode(tamanho)
    
    # FPS
    clock = pygame.time.Clock()
    
    while a_correr:
        clock.tick(10)
        ecra.fill(COR_BACKGROUND)
                
        # Update da cobra
        a_correr = cobra.update(mapa)
        
        # Dar display do mapa
        mapa.display((100, 100), ecra)

        # Receber eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()

        # Dar update do ecrã
        pygame.display.update()