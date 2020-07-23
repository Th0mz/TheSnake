from random import randrange

snake_sprite = "\033[1;32;40mX\033[1;37;40m" 
maca_sprite = "\033[1;31;40mO\033[1;37;40m"
chao_sprite = "\033[1;30;40m.\033[1;37;40m"
chao_cursor = "\033[0;30;47m.\033[1;37;40m"
parede_sprite = "#"
parede_cursor = "\033[0;30;47m#\033[1;37;40m"


X = 0
Y = 1 

def parar_jogo():
    global a_correr
    a_correr = False

class Mapa:
    def __init__(self, tamanho_x, tamanho_y, snake, paredes, edit_mode):
        self.tamanho = (tamanho_x, tamanho_y)
        
        self.paredes = paredes
        self.snake = snake
        self.maca = ["", ""]

        # Inicializar cursor
        if edit_mode:
            self.cursor = [0, 0]
        else:
            self.cursor = ["", ""]

        # Inicializacao do mapa
        self.mapa = []
        self.inicializa_mapa()
        
        if not edit_mode:
            self.nova_maca()

    def inicializa_mapa(self):
        """ Inicializa a lista que representa o mapa adicionando a lista:
                -> "." - Se for um espaco vazio
                -> "X" - Se for a parte de uma cobra
                -> "O" - Se for uma maca 
                -> "#" - Se for uma parede
        """

        for x in range(self.tamanho[X]):
            self.mapa.append([])

            for y in range(self.tamanho[Y]):
                if [x, y] in self.snake.corpo:
                    self.mapa[x].append(snake_sprite)
                elif [x, y] in self.paredes:
                    self.mapa[x].append(parede_sprite)
                elif [x, y] == self.maca:
                    self.mapa[x].append(maca_sprite)
                elif [x, y] == self.cursor:
                    self.mapa[x].append(chao_cursor)
                else:
                    self.mapa[x].append(chao_sprite)
    
    def elemento_mapa(self, pos_x, pos_y):
        """ Dada uma coordenada x, y devolve qual o elemento
            do mapa na posicao x, y  [X, O ou .] """
        return self.mapa[pos_x][pos_y]

    def update(self, pos_add, pos_rm):
        """ Serve para dar update da posicao da cobra no mapa
            removendo o seu ultimo elemento e adicionanto a 
                    nova posicao da sua cabeça"""
        self.mapa[pos_add[X]][pos_add[Y]] = snake_sprite
        self.mapa[pos_rm[X]][pos_rm[Y]] = chao_sprite
    
    def nova_maca(self):
        def update_maca():
            """ Escolhe uma nova posicao random para a maca e
              devolve o elemento que lá se encontra [X, O ou .] 
            """
            self.maca[X] = randrange(self.tamanho[X])
            self.maca[Y] = randrange(self.tamanho[Y])
            return self.elemento_mapa(self.maca[X], self.maca[Y])

        elemento = update_maca()
        while (elemento != chao_sprite):
            elemento = update_maca()

        self.mapa[self.maca[X]][self.maca[Y]] = maca_sprite

    def display(self):
        """ Renderiza o mapa """
        print()
        for y in range(self.tamanho[Y]):
            linha = ""

            for x in range(self.tamanho[X]):
                linha += self.mapa[x][y] + "  "
            print("   " + linha)

    def move_cursor(self, dir_x, dir_y):
        """ Move o cursor """
        cursor_anterior = self.cursor
        self.cursor = [(self.cursor[X] + dir_x) % self.tamanho[X], (self.cursor[Y] + dir_y) % self.tamanho[Y]]

        # Update do mapa
        if self.mapa[cursor_anterior[X]][cursor_anterior[Y]] == chao_cursor:
            self.mapa[cursor_anterior[X]][cursor_anterior[Y]] = chao_sprite
        else:
            self.mapa[cursor_anterior[X]][cursor_anterior[Y]] = parede_sprite

        if self.mapa[self.cursor[X]][self.cursor[Y]] == chao_sprite:
             self.mapa[self.cursor[X]][self.cursor[Y]] = chao_cursor
        else:
            self.mapa[self.cursor[X]][self.cursor[Y]] = parede_cursor
    
    def adiciona_parede(self):
        """ Adiciona uma parede na posicao do cursor """

        if self.cursor in self.paredes:
            self.paredes.remove(self.cursor)
            
            # Update do mapa
            self.mapa[self.cursor[X]][self.cursor[Y]] = chao_cursor
        else:
            self.paredes.append(self.cursor)

            # Update do mapa
            self.mapa[self.cursor[X]][self.cursor[Y]] = parede_cursor