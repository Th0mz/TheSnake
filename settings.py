import pygame

# Variaveis Globais :
X = 0
Y = 1 

# Teclas :
ENTER = 13
W = ord("w")
A = ord("a")
S = ord("s")
D = ord("d") 
F = ord("f")

# Fontes :
pygame.font.init()

TAMANHO_OPCOES = 20
fonteOpcoes = pygame.font.SysFont("Comic Sans MS", 20)

TAMANHO_TITULO = 55
fonteTitulo = pygame.font.Font("fonte.ttf", TAMANHO_TITULO)


    # Header :
#  > Cores 
COR_TEXTO = (180, 180, 180)
COR_LINHA = (90, 90, 90)

#  > Linha 
DISTANCIA_TEXTO = 5
GROSSURA = 4



    # Opções :
#  > Posição
POS_OPCOES = (50, 115)

#  > Espaço
ESPACO = 30

#  > Cores
COR_DISPLAY = (0, 0, 0) # Cor normal de display
COR_HIGHLIGHT = (255, 0, 0) # Cor quando o cursor está a selecionar a opção



    # Cores :
#  > Jogo
COR_BACKGROUND = (40, 44, 46)
COR_SNAKE = (0, 100, 0) 
COR_CABECA = (0, 110, 0)
COR_MACA = (150, 0, 0)
COR_CHAO = (50, 54, 56)
COR_PAREDE = (76, 79, 84) 

COR_CURSOR = (150, 0, 0)

    # Posições Mapa :
# Tamanho dos quadrados do mapa
MAPA_TAMANHO = 20
# Linha que separa os quadrados do jogo
MAPA_INTERVALO = 4 