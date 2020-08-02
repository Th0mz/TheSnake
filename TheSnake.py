
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

import pygame  

pygame.init()
ENTER = 13 

# Criar ecrã
tamanho = (300, 250)
ecra = pygame.display.set_mode(tamanho)


# Fonte
pygame.font.init()
fonte = pygame.font.SysFont("Comic Sans MS", 20)

# Configurar ecrã
icon = pygame.image.load("snake.png")
pygame.display.set_caption("The Snake")
pygame.display.set_icon(icon)

# Menu
cursor = 0
update = True
exe = False

cor_display = (0, 0, 0)
cor_highlight = (255, 0, 0)
posY = 100
opcoes = [
    { "nome" : "> Jogar", "exec" : game_loop},
    { "nome" : "> Editar Mapa", "exec" : quit},
    { "nome" : "> Sair", "exec" : quit}
]

num_opcoes = len(opcoes)

a_correr = True
COR_BACKGROUND = (40,43,46)

while a_correr:

    # Receber eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            a_correr = False
        # Uma tecla foi primida
        elif evento.type == pygame.KEYDOWN:
            # Funcionalidade para cada tecla
            if evento.key == ord("s"):
                cursor = (cursor + 1) % num_opcoes
                update = True
            elif evento.key == ord("w"):
                cursor = (cursor - 1) % num_opcoes
                update = True
            elif evento.key == ENTER:
                exe = True

    # Display [Menu]  
    if update:
        ecra.fill(COR_BACKGROUND)
        
        # Display Opções
        for opcao in range(num_opcoes):
            texto = fonte.render(opcoes[opcao]["nome"], False, cor_highlight) if opcao == cursor \
                else fonte.render(opcoes[opcao]["nome"], False, cor_display)

            ecra.blit(texto, (50, posY + (opcao * 20)))

        # Update do ecrã
        update = False
        pygame.display.update()

    # Executar funcionalidade da opção selecionada pelo cursor
    if exe:
        opcoes[cursor]["exec"]()
        update = True
        exe = False
        
        ecra = pygame.display.set_mode(tamanho)


pygame.quit()
 