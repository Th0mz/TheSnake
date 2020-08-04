from snake import Snake
from mapa import Mapa, X, Y, COR_BACKGROUND

import pygame

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

    # Ecrã
    tamanho_mapa = ((mapa.tamanho[X] * mapa.TAMANHO) + ((mapa.tamanho[X] - 1) * mapa.INTERVALO), \
                    (mapa.tamanho[Y] * mapa.TAMANHO) + ((mapa.tamanho[Y] - 1) * mapa.INTERVALO))

    pos_mapa = (mapa.TAMANHO, 100)

    tamanho = (tamanho_mapa[X] + 2 * pos_mapa[X], tamanho_mapa[Y] + pos_mapa[X] + pos_mapa[Y])
    ecra = pygame.display.set_mode(tamanho)

    titulo = "The Snake"
    fonte = pygame.font.SysFont("Comic Sans MS", 20)
    the_snake = fonte.render(titulo, False, (255, 0, 0))

    text_width, text_height = fonte.size(titulo)
    # Centrar o texto em relação a posição do mapa
    pos_texto = (tamanho[X] // 2 - text_width // 2, pos_mapa[Y] // 2 - text_height // 2)
    
    # FPS
    clock = pygame.time.Clock()
    FPS = 10
    
    # Game loop :
    a_correr = True
    
    while a_correr:
        clock.tick(FPS)
        ecra.fill(COR_BACKGROUND)

        # Titulo
        ecra.blit(the_snake, pos_texto)

        tecla = None
        # Receber eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            # Uma tecla foi primida
            elif evento.type == pygame.KEYDOWN:
                # Funcionalidade para cada tecla
                tecla = chr(evento.key)
                
        # Update da cobra
        a_correr = cobra.update(mapa, tecla)
        
        # Dar display do mapa
        mapa.display(pos_mapa, ecra, cobra)

        # Dar update do ecrã
        pygame.display.update()