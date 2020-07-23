from pynput.keyboard import Key, Listener
from keyboard import press_and_release
from game_loop import game_loop
from editar_mapa import edit_loop, header, set_windowSize

X = 0
Y = 1



def sair():
    exit()   


a_selecionar = 0
update = True
exe = False

def menu():
    global a_selecionar, update, exe

    opcoes = [
        { "Display" : "> Jogar", "Funcao" : game_loop},
        { "Display" : "> Editar Mapa", "Funcao" : edit_loop},
        { "Display" : "> Sair", "Funcao" : sair}
    ]

    numero_opcoes = len(opcoes)
    tamanho = (35, 4 + numero_opcoes + 2)
    set_windowSize(tamanho[X], tamanho[Y])

    def tecla_released(key):
        global update, a_selecionar, exe
        if str(key) == "'w'" or key == Key.up:
            a_selecionar = (a_selecionar - 1) % numero_opcoes
            update = True
        if str(key) == "'s'" or key == Key.down:
            a_selecionar = (a_selecionar + 1) % numero_opcoes
            update = True
        if key == Key.enter:
            exe = True

        return False

    while True:

        if exe:
            opcoes[a_selecionar]["Funcao"]()

            # Limpar coisas escritas anteriormente
            for i in range(len(10)):
                press_and_release('esc')
            exe = False
            update = True
            set_windowSize(tamanho[X], tamanho[Y])


        if update:
            header("MENU", tamanho[X])
            # Display Opcoes
            print()
            for i in range(numero_opcoes):
                if i == a_selecionar:
                    print(" "*(tamanho[X]//4) + "\033[1;33;40m{}\033[1;37;40m".format(opcoes[i]["Display"]))
                else:
                    print(" "*(tamanho[X]//4) + "\033[1;30;40m{}\033[1;37;40m".format(opcoes[i]["Display"]))
            
        # Verificara key release
        with Listener(on_release=tecla_released) as listener:
            listener.join()
            
        

