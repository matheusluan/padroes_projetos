class NPC:
    # define o construtor:
    def __init__(self, nome, saude, forca):
        # inicializa os atributos:
        self.saude = saude
        self.forca = forca
        self.nome = nome
        self.resistencia = 0

    def atacar(self):
        pass

    def atualizar_saude(self, forca):
        self.saude -= forca
        print(f'{self.nome} saude: ', self.saude)

class Dragao(NPC):
    def atacar(self, oponente):
        print(f'{self.nome} atacando com forca {self.forca}')
        oponente.atualizar_saude(self.forca)

class Joker(NPC):
    def atacar(self, oponente: NPC):
        print(f'{self.nome} atacando com forca {self.forca}')
        oponente.atualizar_saude(self.forca)

from enum import Enum
class NpcType(Enum): 
    DRAGAO = 1
    JOKER = 2
    ANFITRIAO = 3

class NpcFactory:

    @staticmethod
    def create(npc_type: NpcType) -> NPC:
        if npc_type == NpcType.DRAGAO:
            return Dragao('dragao', 200, 30)
        if npc_type == NpcType.JOKER:
            return Joker('joker', 140, 20)
            
        return None


if __name__ == '__main__':
    '''
    dragao = Dragao('dragao', 200, 30)
    dragao.atacar()
    joker = Joker('joker', 140, 20)
    joker.atacar()
    '''
    dragao = NpcFactory.create(NpcType.DRAGAO)
    joker = NpcFactory.create(NpcType.JOKER)

    dragao.atacar(joker)
    joker.atacar(dragao)