from snake import Snake
from mapa import Mapa
from math import sqrt

from settings import COR_BACKGROUND, COR_LINHA, COR_TEXTO
from settings import DISTANCIA_TEXTO, GROSSURA, TAMANHO_TITULO
from settings import MAPA_TAMANHO, MAPA_INTERVALO
from settings import ENTER, W, A, S, D, F
from settings import fonteTitulo, fonteOpcoes
from settings import X, Y

import pygame


mapa_X = 0
mapa_Y = 0
def editar_mapa():
    mapa_X = 10
    mapa_Y = 10

    # Inicializar ecrã
    tamanho = (300, 250)
    ecra = pygame.display.set_mode(tamanho)

    # Texto que contem o tamanho do mapa e botão para alterar o tamanho do mapa

    def botao(centro, raio, funcionalidade, executar, ecra):
        def rato_porCima(centro, raio):
            posicao_rato = pygame.mouse.get_pos()
            distancia = sqrt((posicao_rato[X] - centro[X])**2 + (posicao_rato[Y] - centro[Y])**2)

            return distancia <= raio

        # Renderizar o botão
        cor = (255, 255, 255) if rato_porCima(centro, raio) else (0, 0, 0)
        pygame.draw.circle(ecra, cor, centro, raio)

        # Executar funcionalidade do botão
        if executar and rato_porCima(centro, raio):
            funcionalidade()
    

    def selecinador_tamanho(texto, posicao, raio, func_aumento, func_diminuicao, executar, ecra):
        texto_display = fonteOpcoes.render(str(texto), False, COR_TEXTO)
        text_width, text_height = fonteOpcoes.size(str(texto))
        posicao_texto = (posicao[X] - text_width // 2, posicao[Y] - text_height // 2)

        # Informação sobre o tamanho do mapa
        ecra.blit(texto_display, posicao_texto)
        
        DISTANCIA_AO_TEXTO = 5
        # Botão de diminuir
        botao((posicao_texto[X] - raio - DISTANCIA_AO_TEXTO, posicao[Y]), 10, func_diminuicao, executar, ecra)
        
        # Botão de aumento
        botao((posicao_texto[X] + text_width + raio + DISTANCIA_AO_TEXTO, posicao[Y]), 10, func_aumento, executar, ecra)

    # Funções dos botões
    def aumenta_mapaX():
        global mapa_X
        mapa_X += 1

    def aumenta_mapaY():
        global mapa_Y
        mapa_Y += 1

    def diminui_mapaX():
        global mapa_X
        if mapa_X >= 1:
            mapa_X -= 1

    def diminui_mapaY():
        global mapa_Y
        if mapa_Y >= 1:
            mapa_Y -= 1

    # Display loop :
    a_correr = True
    update = True

    while a_correr:
        clicado = False

        # Receber eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            
            # Verificar se o botão do rato foi clicado
            elif evento.type == pygame.MOUSEBUTTONUP:
                clicado = True

            # Uma tecla foi primida
            elif evento.type == pygame.KEYDOWN:
                if evento.key == ENTER:
                    a_correr = False

        # Update dos conteúdos do ecrã
        #    Update do background
        ecra.fill(COR_BACKGROUND)

        # Display do texto
        selecinador_tamanho(mapa_X, (50, tamanho[Y] // 2), 10, aumenta_mapaX, diminui_mapaX, clicado, ecra)
        selecinador_tamanho(mapa_Y, (250, tamanho[Y] // 2), 10, aumenta_mapaY, diminui_mapaY, clicado, ecra)

        #    Dar update do ecrã
        pygame.display.update()
        update = False
        

    
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
    
    editar = fonteTitulo.render(titulo, False, COR_TEXTO)
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
        ecra.blit(editar, pos_texto)
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

    # Guardar mapa
    with open("mapa.txt", "w") as ficheiro:
        ficheiro.write(str(mapa.tamanho) + "\n")
        ficheiro.write(str(mapa.paredes))