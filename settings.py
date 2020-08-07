import pygame

# Variaveis Globais :
X = 0
Y = 1 

# Gameplay
    # Intervalo de tempo que o jogador tem ao apanhar uma maça 
    # para apanhar a proxima para poder receber um bonus de pontos
TEMPO_BONUS = 3

    # Ticks do jogo [FPS]
FPS = 10

# Teclas :
ENTER = 13
W = ord("w")
A = ord("a")
S = ord("s")
D = ord("d") 
F = ord("f")

# Fontes :
pygame.font.init()

TAMANHO_OPCOES = 22
fonteOpcoes = pygame.font.Font("opcoes.ttf", TAMANHO_OPCOES)

TAMANHO_TITULO = 55
fonteTitulo = pygame.font.Font("fonte.ttf", TAMANHO_TITULO)

TAMANHO_SCORE = 20
fonteScore = pygame.font.Font("score.ttf", TAMANHO_SCORE)


    # Header :
#  > Cores 
COR_TEXTO = (180, 180, 180)
COR_LINHA = (90, 90, 90)

#  > Linha 
DISTANCIA_TEXTO = 5
GROSSURA = 4



    # Opções :
#  > Posição
POS_OPCOES = (80, 115)

#  > Espaço
ESPACO = 30

#  > Cores
COR_PONTOS = (18, 18, 18) # Cor dos pontos
COR_OPCOES = tuple([27] * 3) # Cor do texto
COR_CURSOR_MENU = (90, 90, 90) # Cor do cursor que seleciona a opção



    # Cores :
#  > Jogo
COR_BACKGROUND = (40, 44, 46)
COR_SNAKE = (0, 100, 0) 
COR_CABECA = (0, 110, 0)
COR_MACA = (165, 12, 14)
COR_CHAO = (50, 54, 56)
COR_PAREDE = (76, 79, 84) 

COR_CURSOR = (150, 0, 0)

    # Posições Mapa :
# Tamanho dos quadrados do mapa
MAPA_TAMANHO = 20
# Linha que separa os quadrados do jogo
MAPA_INTERVALO = 4 