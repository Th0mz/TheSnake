from snake import Snake
from mapa import Mapa

from settings import COR_BACKGROUND, COR_LINHA, COR_TEXTO
from settings import DISTANCIA_TEXTO, GROSSURA, TAMANHO_TITULO
from settings import MAPA_TAMANHO, MAPA_INTERVALO, FPS
from settings import fonteTitulo, fonteScore
from settings import X, Y

import pygame

def game_loop():
    """ Main do jogo """
    # Ler mapa guardado :
    with open("mapa.txt") as ficheiro:
        tamanho = eval(ficheiro.readline())
        paredes = eval(ficheiro.readline())

    # Inicialização do mapa
    pos_inicial = [tamanho[X] // 2, tamanho[Y] // 2] 
    cobra = Snake([pos_inicial, [pos_inicial[X], pos_inicial[Y] - 1]])

    mapa = Mapa(tamanho[X], tamanho[Y], cobra, paredes, False)

    # Calculo das posições / tamanho do mapa em relação ao tamanho  
    #   da janela e calculo do tamanho necessario para a janela
    tamanho_mapa = ((mapa.tamanho[X] * MAPA_TAMANHO) + ((mapa.tamanho[X] - 1) * MAPA_INTERVALO), \
                    (mapa.tamanho[Y] * MAPA_TAMANHO) + ((mapa.tamanho[Y] - 1) * MAPA_INTERVALO))

    pos_mapa = (MAPA_TAMANHO, 120)

    tamanho = (tamanho_mapa[X] + 2 * pos_mapa[X], tamanho_mapa[Y] + pos_mapa[X] + pos_mapa[Y])

    # Ecrã
    ecra = pygame.display.set_mode(tamanho)

    # Header
    titulo = "The Snake"
    the_snake = fonteTitulo.render(titulo, True, COR_TEXTO)

    text_width, text_height = fonteTitulo.size(titulo) # Dimenções do retangulo que involve o texto

    # Centrar o texto em relação a posição do mapa
    pos_texto = (tamanho[X] // 2 - text_width // 2, 10)
    
    # Linha por baixo do titulo
    pos_retangulo = (pos_mapa[X], pos_texto[Y] + text_height + DISTANCIA_TEXTO)
    retangulo = pygame.Rect(pos_retangulo[X], pos_retangulo[Y] , tamanho_mapa[X], GROSSURA) 

    # Score :
    score = "Score :"
    pos_score = (pos_retangulo[X], pos_retangulo[Y] + GROSSURA + 5)
    score_width, score_height = fonteScore.size(score)
    pos_pontos = (pos_score[X] + score_width + 10, pos_score[Y])

    # FPS
    clock = pygame.time.Clock()
    
    
    # Game loop :
    a_correr = True
    
    while a_correr:
        clock.tick(FPS)
        ecra.fill(COR_BACKGROUND)

        # Titulo
        ecra.blit(the_snake, pos_texto)
        pygame.draw.rect(ecra, COR_LINHA, retangulo)

        # Score
        score_texto = fonteScore.render(score, True, (140, 142, 143))
        pontos_texto = fonteScore.render(str(cobra.score), True, COR_TEXTO)
        ecra.blit(score_texto, pos_score)
        ecra.blit(pontos_texto, pos_pontos)

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