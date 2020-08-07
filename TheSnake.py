
#!######################################################################
#!  ___________.__               _________              __             #
#! \__     ___/|  |__   ____    /   _____/ ____ _____  |  | __ ____    #
#!    |    |   |  |  \_/ __ \   \_____  \ /    \\__  \ |  |/ // __ \   #
#!    |    |   |   Y  \  ___/   /        \   |  \/ __ \|    <\  ___/   #
#!    |____|   |___|  /\___  > /_______  /___|  (____  /__|_ \\___  >  #
#!                 \/     \/          \/     \/     \/     \/    \/    #
#!######################################################################

#  -> Autor : Tomás Tavares
#  -> Descricao : Jogo da snake

from game_loop import game_loop
from editar_mapa import edit_loop
from time import time

from settings import COR_BACKGROUND, COR_LINHA, COR_TEXTO
from settings import DISTANCIA_TEXTO, GROSSURA, TAMANHO_TITULO
from settings import POS_OPCOES, ESPACO, COR_PONTOS, COR_CURSOR_MENU, COR_OPCOES
from settings import ENTER, W, S
from settings import fonteTitulo, fonteOpcoes
from settings import X, Y

import pygame  

# Inicializar Pygame :
pygame.init() 

# Criar ecrã
tamanho = (300, 230)
ecra = pygame.display.set_mode(tamanho)

# Configurar ecrã
icon = pygame.image.load("snake.png")
pygame.display.set_caption("The Snake")
pygame.display.set_icon(icon)

# Menu :
exe = False

#   Opções :
opcoes = [
    { "nome" : "Jogar", "exec" : game_loop},
    { "nome" : "Editar Mapa", "exec" : edit_loop},
    { "nome" : "Sair", "exec" : quit}
]

num_opcoes = len(opcoes)


# Header :

titulo = "Menu"
the_snake = fonteTitulo.render(titulo, True, COR_TEXTO)
text_width, text_height = fonteTitulo.size(titulo) # Dimenções do retangulo que involve o texto

# Centrar o texto em relação a posição do mapa
pos_texto = (tamanho[X] // 2 - text_width // 2, 100 // 2 - text_height // 2)

# Linha por baixo do titulo    
retangulo = pygame.Rect(20, pos_texto[Y] + text_height + DISTANCIA_TEXTO , tamanho[X] - 20 * 2, GROSSURA) 

# Cursor
DISTANCIA_CURSOR = 6
blink_speed = 15
cursor = 0
cursor_texto = fonteOpcoes.render("<", True, COR_CURSOR_MENU)

moveu = True
iniciar_timer = True
tempo_inicial = 0


# Main loop :
a_correr = True

while a_correr:

    # Receber eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            a_correr = False
        # Uma tecla foi primida
        elif evento.type == pygame.KEYDOWN:
            # Funcionalidade para cada tecla
            if evento.key == S:
                moveu = True
                iniciar_timer = True
                cursor = (cursor + 1) % num_opcoes
            elif evento.key == W:
                moveu = True
                iniciar_timer = True
                cursor = (cursor - 1) % num_opcoes
            elif evento.key == ENTER:
                exe = True

    # Display [Menu]  
    #   Background
    ecra.fill(COR_BACKGROUND)

    #   Titulo [Header]
    ecra.blit(the_snake, pos_texto)
    pygame.draw.rect(ecra, COR_LINHA, retangulo)
    
    #   Display Opções
    for opcao in range(num_opcoes):
        texto = fonteOpcoes.render(opcoes[opcao]["nome"], True, COR_OPCOES)

        pos_opcao = (POS_OPCOES[X], POS_OPCOES[Y] + (opcao * ESPACO))
        ecra.blit(texto, pos_opcao)
        text_width, text_height = fonteOpcoes.size(opcoes[opcao]["nome"])

        pygame.draw.circle(ecra, COR_PONTOS, (pos_opcao[X] - 13, pos_opcao[Y] + text_height // 2), 5)

        if opcao == cursor and (int(time() * 10) % blink_speed < (blink_speed // 2) or moveu):
            ecra.blit(cursor_texto, (pos_opcao[X] + text_width + DISTANCIA_CURSOR, pos_opcao[Y]))

    if moveu:
        if iniciar_timer:
            tempo_inicial = time()
            iniciar_timer = False

        tempo = time()
        if tempo - tempo_inicial >= 0.5:
            moveu = False

    # Executar funcionalidade da opção selecionada pelo cursor
    if exe:
        opcoes[cursor]["exec"]()
        exe = False
        
        ecra = pygame.display.set_mode(tamanho)

    # Update do ecrã
    pygame.display.update()


# Fechar as funcionalidades do pygame [Programa termina]
pygame.quit()
pygame.font.quit()  
 