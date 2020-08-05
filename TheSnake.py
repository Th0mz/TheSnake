
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

from settings import COR_BACKGROUND, COR_LINHA, COR_TEXTO
from settings import DISTANCIA_TEXTO, GROSSURA, TAMANHO_TITULO
from settings import POS_OPCOES, ESPACO, COR_DISPLAY, COR_HIGHLIGHT
from settings import ENTER, W, S
from settings import fonteTitulo, fonteOpcoes
from settings import X, Y

import pygame  

# Inicializar Pygame :
pygame.init() 

# Criar ecrã
tamanho = (300, 250)
ecra = pygame.display.set_mode(tamanho)

# Configurar ecrã
icon = pygame.image.load("snake.png")
pygame.display.set_caption("The Snake")
pygame.display.set_icon(icon)

# Menu :
cursor = 0
update = True
exe = False

#   Opções :
opcoes = [
    { "nome" : "> Jogar", "exec" : game_loop},
    { "nome" : "> Editar Mapa", "exec" : edit_loop},
    { "nome" : "> Sair", "exec" : quit}
]

num_opcoes = len(opcoes)


# Header :

titulo = "Menu"
the_snake = fonteTitulo.render(titulo, False, COR_TEXTO)
text_width, text_height = fonteTitulo.size(titulo) # Dimenções do retangulo que involve o texto

# Centrar o texto em relação a posição do mapa
pos_texto = (tamanho[X] // 2 - text_width // 2, 100 // 2 - text_height // 2)

# Linha por baixo do titulo    
retangulo = pygame.Rect(20, pos_texto[Y] + text_height + DISTANCIA_TEXTO , tamanho[X] - 20 * 2, GROSSURA) 


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
                cursor = (cursor + 1) % num_opcoes
                update = True
            elif evento.key == W:
                cursor = (cursor - 1) % num_opcoes
                update = True
            elif evento.key == ENTER:
                exe = True

    # Display [Menu]  
    if update:
        # Background
        ecra.fill(COR_BACKGROUND)

        # Titulo [Header]
        ecra.blit(the_snake, pos_texto)
        pygame.draw.rect(ecra, COR_LINHA, retangulo)
        
        # Display Opções
        for opcao in range(num_opcoes):
            texto = fonteOpcoes.render(opcoes[opcao]["nome"], False, COR_HIGHLIGHT) if opcao == cursor \
                else fonteOpcoes.render(opcoes[opcao]["nome"], False, COR_DISPLAY)

            ecra.blit(texto, (POS_OPCOES[X], POS_OPCOES[Y] + (opcao * ESPACO)))

        # Update do ecrã
        update = False
        pygame.display.update()

    # Executar funcionalidade da opção selecionada pelo cursor
    if exe:
        opcoes[cursor]["exec"]()
        update = True
        exe = False
        
        ecra = pygame.display.set_mode(tamanho)


# Fechar as funcionalidades do pygame [Programa termina]
pygame.quit()
 