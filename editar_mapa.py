from snake import Snake
from mapa import Mapa

from settings import COR_BACKGROUND, COR_LINHA, COR_TEXTO
from settings import DISTANCIA_TEXTO, GROSSURA, TAMANHO_TITULO
from settings import MAPA_TAMANHO, MAPA_INTERVALO
from settings import ENTER, W, A, S, D, F
from settings import fonteTitulo
from settings import X, Y

import pygame


def editar_mapa():
    mapa_X = 10
    mapa_Y = 10

    mapa = Mapa(mapa_X, mapa_Y, Snake([]), [], True)
    return mapa


def edit_loop():
    mapa = editar_mapa()
    cobra = Snake([])

    # Calculo das posições / tamanho do mapa em relação ao tamanho  
    #   da janela e calculo do tamanho necessario para a janela
    tamanho_mapa = ((mapa.tamanho[X] * MAPA_TAMANHO) + ((mapa.tamanho[X] - 1) * MAPA_INTERVALO), \
                    (mapa.tamanho[Y] * MAPA_TAMANHO) + ((mapa.tamanho[Y] - 1) * MAPA_INTERVALO))

    pos_mapa = (MAPA_TAMANHO, 110)

    tamanho = (tamanho_mapa[X] + 2 * pos_mapa[X], tamanho_mapa[Y] + pos_mapa[X] + pos_mapa[Y])

    # Ecrã
    ecra = pygame.display.set_mode(tamanho)

    # Header
    titulo = "Editar"
    
    the_snake = fonteTitulo.render(titulo, False, COR_TEXTO)
    text_width, text_height = fonteTitulo.size(titulo)

    # Centrar o texto em relação a posição do mapa
    pos_texto = (tamanho[X] // 2 - text_width // 2, pos_mapa[Y] // 2 - text_height // 2)
    
    # Linha por baixo do titulo
    retangulo = pygame.Rect(pos_mapa[X], pos_texto[Y] + text_height + DISTANCIA_TEXTO , tamanho_mapa[X], GROSSURA)

    tamanho = (mapa.tamanho[X] * 3 + 6, mapa.tamanho[Y] + 8)

    # Editar Mapa:
    a_correr = True
    update = True
    
    while a_correr:
        ecra.fill(COR_BACKGROUND)

        # Titulo
        ecra.blit(the_snake, pos_texto)
        pygame.draw.rect(ecra, COR_LINHA, retangulo)

        # Receber eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            # Uma tecla foi primida
            elif evento.type == pygame.KEYDOWN:
                # Funcionalidade para cada tecla
                    # Movimaneto do cursor
                if evento.key == W:
                    mapa.move_cursor(0, -1)
                    update = True
                elif evento.key == S:
                    mapa.move_cursor(0, 1)
                    update = True
                elif evento.key == D:
                    mapa.move_cursor(1, 0)
                    update = True
                elif evento.key == A:
                    mapa.move_cursor(-1, 0)
                    update = True

                # Adicionar parece do local selecionado
                elif evento.key == ENTER:
                    mapa.adiciona_parede()
                    update = True
                
                # Guardar mapa e sair do modo de edição
                elif evento.key == F:
                    a_correr = False

        if update:
            mapa.display(pos_mapa, ecra, cobra)
            
            # Update do ecrã
            update = False
            pygame.display.update()

    # Definir novamente as variaveis globais

    # Guardar mapa
    with open("mapa.txt", "w") as ficheiro:
        ficheiro.write(str(mapa.tamanho) + "\n")
        ficheiro.write(str(mapa.paredes))