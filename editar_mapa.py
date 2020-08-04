from snake import Snake
from mapa import Mapa, COR_BACKGROUND

import pygame

X = 0
Y = 1
ENTER = 13


def editar_mapa():
    mapa_X = 10
    mapa_Y = 10

    mapa = Mapa(mapa_X, mapa_Y, Snake([]), [], True)
    return mapa


def edit_loop():
    mapa = editar_mapa()
    cobra = Snake([])

    # Ecrã
    tamanho_mapa = ((mapa.tamanho[X] * mapa.TAMANHO) + ((mapa.tamanho[X] - 1) * mapa.INTERVALO), \
                    (mapa.tamanho[Y] * mapa.TAMANHO) + ((mapa.tamanho[Y] - 1) * mapa.INTERVALO))

    pos_mapa = (mapa.TAMANHO, 100)

    tamanho = (tamanho_mapa[X] + 2 * pos_mapa[X], tamanho_mapa[Y] + pos_mapa[X] + pos_mapa[Y])
    ecra = pygame.display.set_mode(tamanho)

    titulo = "Editar"
    fonte = pygame.font.SysFont("Comic Sans MS", 20)
    the_snake = fonte.render(titulo, False, (255, 0, 0))

    text_width, text_height = fonte.size(titulo)
    # Centrar o texto em relação a posição do mapa
    pos_texto = (tamanho[X] // 2 - text_width // 2, pos_mapa[Y] // 2 - text_height // 2)
    
    # FPS
    clock = pygame.time.Clock()
    FPS = 10

    tamanho = (mapa.tamanho[X] * 3 + 6, mapa.tamanho[Y] + 8)

    # Editar Mapa:
    a_correr = True
    update = True
    
    while a_correr:
        clock.tick(FPS)
        ecra.fill(COR_BACKGROUND)

        # Titulo
        ecra.blit(the_snake, pos_texto)

        # Receber eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            # Uma tecla foi primida
            elif evento.type == pygame.KEYDOWN:
                # Funcionalidade para cada tecla
                    # Movimaneto do cursor
                if evento.key == ord("w"):
                    mapa.move_cursor(0, -1)
                    update = True
                elif evento.key == ord("s"):
                    mapa.move_cursor(0, 1)
                    update = True
                elif evento.key == ord("d"):
                    mapa.move_cursor(1, 0)
                    update = True
                elif evento.key == ord("a"):
                    mapa.move_cursor(-1, 0)
                    update = True

                # Adicionar parece do local selecionado
                elif evento.key == ENTER:
                    mapa.adiciona_parede()
                    update = True
                
                # Guardar mapa e sair do modo de edição
                elif evento.key == ord("f"):
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