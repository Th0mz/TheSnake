from os import system as consola
from keyboard import is_pressed
from pynput.keyboard import Key, Listener

from snake import Snake
from mapa import Mapa

X = 0
Y = 1

def set_windowSize(width, height):
    consola("mode con:cols={} lines={}".format(width, height))

def header(nome, tamanho_X):
    bordo = "\033[1;31;40m#\033[1;37;40m"
    nome_com_cor = "\033[1;33;40m{}\033[1;37;40m".format(nome)

    consola("cls")
    print("  " + bordo*(tamanho_X - 5))
    print("  " + bordo + " "*((tamanho_X - 5)//2 - len(nome) // 2  - 1) + "{}".format(nome_com_cor) + " "*((tamanho_X - 5)//2 - (len(nome) - len(nome)// 2) - 1) + bordo)
    print("  " + bordo*(tamanho_X - 5))

mapa_X = 0
mapa_Y = 0
def editar_mapa():
    global mapa_X, mapa_Y

    tamanho = (51, 10)
    set_windowSize(tamanho[X], tamanho[Y])
    header("EDITAR MAPA", tamanho[X])
    input()
    try:
        mapa_X = eval(input(" > Introduz o \033[1;33;40mdimenção segundo x\033[1;37;40m do mapa: "))
        mapa_Y = eval(input(" > Introduz o \033[1;33;40mdimenção segundo y\033[1;37;40m do mapa: "))
    except:
        editar_mapa()

    mapa = Mapa(mapa_X, mapa_Y, Snake([]), [], True)

    return mapa

a_correr = True
update = True
adiciona_parede = False
mover = False
mover_dir = [0, 0]

def edit_loop():
    mapa = editar_mapa()
    global a_correr, update, adiciona_parede, mover_dir, mover

    def tecla_released(key):
        global update, a_correr, mover_dir, adiciona_parede, mover

        if str(key) == "'w'" or key == Key.up:
            mover_dir = [0, -1]
            mover = True
            update = True
        if str(key) == "'s'" or key == Key.down:
            mover_dir = [0, 1]
            mover = True
            update = True
        if str(key) == "'a'" or key == Key.left:
            mover_dir = [-1, 0]
            mover = True
            update = True
        if str(key) == "'d'" or key == Key.right:
            mover_dir = [1, 0]
            mover = True
            update = True
        if key == Key.enter:
            adiciona_parede = True
            update = True
        if str(key) == "'f'":
            a_correr = False
        
        return False

    tamanho = (mapa.tamanho[X] * 3 + 6, mapa.tamanho[Y] + 8)
    set_windowSize(tamanho[X], tamanho[Y])
    while a_correr:

        if update:
            if adiciona_parede:
                mapa.adiciona_parede()
                adiciona_parede = False

            if mover:
                mapa.move_cursor(mover_dir[X], mover_dir[Y])
                mover = False
            
            header("EDITAR", tamanho[X])
            print("  > Clica no \033[1;33;40mf\033[1;37;40m para guardar\n     a edicao do mapa e sair")
            mapa.display()
            update = False

        # Verifica key released
        with Listener(on_release=tecla_released) as listener:
            listener.join()

    # Definir novamente as variaveis globais
    a_correr = True
    update = True
    adiciona_parede = False
    mover = False
    mover_dir = [0, 0]

    # Guardar mapa
    with open("mapa.txt", "w") as ficheiro:
        ficheiro.write(str(mapa.tamanho) + "\n")
        ficheiro.write(str(mapa.paredes))