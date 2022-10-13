class Pessoa:
    # define o construtor:
    def __init__(self, nome, renda_anual):
        # inicializa os atributos:
        self.nome = nome
        self.renda_anual = renda_anual

    def calcularIR(self):
        pass

class PessoaFisica(Pessoa):
    def calcularIR(self):
        print(f'{self.nome} por ser uma pessoa Fisica terá de pagar 25% da sua renda anual, totalizando: {self.renda_anual * 0.25 } ')       

class PessoaJuridica(Pessoa):
     def calcularIR(self):
        print(f'{self.nome} por ser uma pessoa Juridica terá de pagar 15% da sua renda anual, totalizando: {self.renda_anual * 0.15 } ')  

from enum import Enum
class PessoaType(Enum): 
    PF = 1
    PJ = 2

class PessoaFactory:

    @staticmethod
    def create(pessoa_type: PessoaType) -> Pessoa:
        if pessoa_type == PessoaType.PJ:
            return PessoaFisica('João', 27000)
        if pessoa_type == PessoaType.PF:
            return PessoaJuridica('Maria', 1000000)
            
        return None

if __name__ == '__main__':
   
    pessoa_1 = PessoaFactory.create(PessoaType.PJ)
    pessoa_2 = PessoaFactory.create(PessoaType.PF)

    pessoa_1.calcularIR()
    pessoa_2.calcularIR()