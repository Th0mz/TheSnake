from mapa import snake_sprite, parar_jogo
from settings import X, Y

CABECA = 0
# Representação interna da cobra
class Snake:
    def __init__(self, corpo):
        self.vel = [1, 0]
        self.corpo = corpo
        self.tamanho = len(self.corpo)

    def update(self, mapa, tecla):
        """ Da update da cobra e se ela morrer
        da return de false parando o game loop 
        """
        self.mudar_diracao(tecla)
        parar = self.mover(mapa)

        return parar


    def mover(self, mapa):
        """ Move a cobra consoante a velocidade que tem e verfica tambem
            se a proxima posicao da cabeca e uma maca ou o proprio corpo
         """
        # Obter nova posicao da cabeça 
        prox_posicaoX = (self.corpo[CABECA][X] + self.vel[X]) % mapa.tamanho[X]
        prox_posicaoY = (self.corpo[CABECA][Y] + self.vel[Y]) % mapa.tamanho[Y]
        prox_posicao = [[prox_posicaoX, prox_posicaoY]]
        # Adicionar cabeca ao inicio da lista [Que representa neste caso a cobra]
        self.corpo = prox_posicao + self.corpo

        if prox_posicao == [mapa.maca]:
            # A posicao da cabeça vai ser a maca
            mapa.mapa[prox_posicao[0][X]][prox_posicao[0][Y]] = snake_sprite
            self.tamanho += 1

            mapa.nova_maca()

        elif self.morreu(mapa.paredes):
            # A posicao da cabeca vai ser o corpo da cobra
            return False
        else:
            # A posicao da cabeça vai vser um espaço vazio
            ultimo_el = self.corpo.pop(-1)
            mapa.update(prox_posicao[0], ultimo_el)
        return True

    def morreu(self, paredes):
        """ Verifica se a cabeca da cobra é igual a alguma 
                    parte do seu corpo """
        for CORPO in range(1, self.tamanho):
            if self.corpo[CABECA] == self.corpo[CORPO]:
                return True
        
        # Verificar se a cabeca esta em uma parede
        return self.corpo[CABECA] in paredes

    def cabeca(self):
        return self.corpo[CABECA]
    
    def mudar_diracao(self, tecla):
        """ Muda a direcao da cobra consoante a tecla pressionada:
                - w : Ir para cima
                - s : Ir para baixo
                - d : Ir para a direita
                - a : Ir para a esquerda
        """

        if tecla == "w" and self.vel != [0, 1]:
            self.vel = [0, -1]
        
        if tecla == "s" and self.vel != [0, -1]:
            self.vel = [0, 1]
        
        if tecla == "d" and self.vel != [-1, 0]:
            self.vel = [1, 0]

        if tecla == "a" and self.vel != [1, 0]:
            self.vel = [-1, 0]
    