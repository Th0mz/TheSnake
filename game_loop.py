from snake import Snake
from mapa import Mapa, X, Y

from time import sleep

def game_loop():
    """ Main do jogo """
    # Ler mapa :
    with open("mapa.txt") as ficheiro:
        tamanho = eval(ficheiro.readline())
        paredes = eval(ficheiro.readline())

    # Inicialização do mapa
    pos_inicial = [tamanho[X] // 2, tamanho[Y] // 2] 
    cobra = Snake([pos_inicial, [pos_inicial[X], pos_inicial[Y] - 1]])

    mapa = Mapa(tamanho[X], tamanho[Y], cobra, paredes, False)

    # Game loop :
    a_correr = True
    
    while a_correr:
        sleep(0.05)

        a_correr = cobra.update(mapa)
        mapa.display()