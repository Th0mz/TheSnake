from snake import Snake
from mapa import Mapa, X, Y

from time import sleep
from os import system as consola

def set_windowSize(width, height):
    consola("mode con:cols={} lines={}".format(width, height))

def game_loop():
    """ Main do jogo """
    # Ler mapa :
    with open("mapa.txt") as ficheiro:
        tamanho = eval(ficheiro.readline())
        paredes = eval(ficheiro.readline())

    pos_inicial = [tamanho[X] // 2, tamanho[Y] // 2] 
    cobra = Snake([pos_inicial, [pos_inicial[X], pos_inicial[Y] - 1]])

    mapa = Mapa(tamanho[X], tamanho[Y], cobra, paredes, False)

    # Funcoes :

    def header_mapa(nome):
        bordo = "\033[1;31;40m#\033[1;37;40m"
        nome_com_cor = "\033[1;33;40m{}\033[1;37;40m".format(nome)

        consola("cls")
        print("  " + bordo*(mapa.tamanho[X]*3))
        print("  " + bordo + " "*((mapa.tamanho[X] * 3)//2 - len(nome) // 2 - 1) + "{}".format(nome_com_cor) + " "*((mapa.tamanho[X] * 3)//2 - (len(nome) - len(nome)// 2) - 1) + bordo)
        print("  " + bordo*(mapa.tamanho[X]*3))   

        print("    \033[1;33;40mScore\033[1;37;40m : {}".format(cobra.tamanho))

    def debug():
        print()
        print("Cobra : {}   Velocidade : {}   Maca : {}".format(cobra.corpo, cobra.vel, mapa.maca)) 

    # Game loop :

    set_windowSize(mapa.tamanho[X] * 3 + 6, mapa.tamanho[Y] + 8)
    a_correr = True
    
    while a_correr:
        sleep(0.05)
        header_mapa("THE SNAKE")

        a_correr = cobra.update(mapa)
        mapa.display()