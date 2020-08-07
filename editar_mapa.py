from snake import Snake
from mapa import Mapa
from math import sqrt

from settings import COR_BACKGROUND, COR_LINHA, COR_TEXTO
from settings import DISTANCIA_TEXTO, GROSSURA, TAMANHO_TITULO
from settings import MAPA_TAMANHO, MAPA_INTERVALO
from settings import ENTER, W, A, S, D, F
from settings import fonteTitulo
from settings import X, Y

import pygame


mapa_X = 0
mapa_Y = 0
def editar_mapa():
    global mapa_X, mapa_Y
    mapa_X = 15
    mapa_Y = 15

    # Inicializar ecrã
    tamanho = (400, 300)
    ecra = pygame.display.set_mode(tamanho)

    # Fonte
    fonteTexto = pygame.font.SysFont("Comic Sans MS", 30)
    fonteSinais = pygame.font.SysFont("Comic Sans MS", 25)
    fonteTituloMenu = pygame.font.Font("fonte.ttf", 43)

    # Texto que contem o tamanho do mapa e botão para alterar o tamanho do mapa

    def botao(texto, centro, raio, funcionalidade, executar, ecra):
        def rato_porCima(centro, raio):
            posicao_rato = pygame.mouse.get_pos()
            distancia = sqrt((posicao_rato[X] - centro[X])**2 + (posicao_rato[Y] - centro[Y])**2)

            return distancia <= raio

        # Renderizar o botão
        cor = (50, 50, 50) if rato_porCima(centro, raio) else (60, 60, 60)
        pygame.draw.circle(ecra, cor, centro, raio)

        # Sinal 
        sinal = fonteSinais.render(texto, True, COR_TEXTO)
        text_width, text_height = fonteSinais.size(texto)
        posicao_info = (centro[X] - text_width // 2, centro[Y] - text_height // 2)

        ecra.blit(sinal, posicao_info)

        # Executar funcionalidade do botão
        if executar and rato_porCima(centro, raio):
            funcionalidade()
    

    def selecinador_tamanho(texto, valor, posicao, raio, func_aumento, func_diminuicao, executar, ecra):
        texto_display = fonteTexto.render(str(valor), True, (171, 173, 175))
        text_width, text_height = fonteTexto.size(str(valor))
        posicao_info = (posicao[X] - text_width // 2, posicao[Y] - text_height // 2)

        # Informação sobre o tamanho do mapa
        ecra.blit(texto_display, posicao_info)
        
        DISTANCIA_AO_TEXTO = raio // 2  
        # Botão de diminuir
        DISTANCIA_TEXTO_CENTRO = raio + DISTANCIA_AO_TEXTO
        botao("-", (posicao_info[X] - DISTANCIA_TEXTO_CENTRO, posicao[Y]), raio, func_diminuicao, executar, ecra)
        
        # Botão de aumento
        botao("+", (posicao_info[X] + text_width + DISTANCIA_TEXTO_CENTRO, posicao[Y]), raio, func_aumento, executar, ecra)

        # Texto :
        titulo = fonteTituloMenu.render(texto, True, COR_TEXTO)
        text_width, text_height = fonteTituloMenu.size(str(texto))
        posicao_texto = (posicao[X] - text_width // 2, posicao[Y] - text_height // 2 - raio * 2)

        ecra.blit(titulo, posicao_texto)

        # Linha : 
        ESPACO_LINHA_TEXTO = 5
        OFFSET = 30
        linha = pygame.Rect(posicao_texto[X] - OFFSET // 2, posicao[Y] - raio - GROSSURA - ESPACO_LINHA_TEXTO, text_width + OFFSET, GROSSURA)
        pygame.draw.rect(ecra, COR_LINHA, linha)


    # Funções dos botões
    def aumenta_mapaX():
        global mapa_X
        mapa_X += 1

    def aumenta_mapaY():
        global mapa_Y
        mapa_Y += 1

    def diminui_mapaX():
        global mapa_X
        if mapa_X > 1:
            mapa_X -= 1

    def diminui_mapaY():
        global mapa_Y
        if mapa_Y > 1:
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
        selecinador_tamanho("Largura do mapa", mapa_X, (tamanho[X] // 2, (3 *tamanho[Y]) // 9) , 25, aumenta_mapaX, diminui_mapaX, clicado, ecra)
        selecinador_tamanho("Altura do mapa", mapa_Y, (tamanho[X] // 2, (7 *tamanho[Y]) // 9) , 25, aumenta_mapaY, diminui_mapaY, clicado, ecra)

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
    
    editar = fonteTitulo.render(titulo, True, COR_TEXTO)
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