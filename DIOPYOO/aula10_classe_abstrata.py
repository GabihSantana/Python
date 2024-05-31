# Normal - Herança:
#class ControleRemoto:
#    def ligar(self):
#        print("TV ligada")
#
#    def desligar(self):
#        print("TV desligada")
#
#class ControleTV(ControleRemoto):
#    pass
#
#controle = ControleTV()
#controle.ligar()
#controle.desligar()

# Abstrata:
from abc import ABC, abstractmethod, abstractproperty

# ControleRemoto > Pai e Padrão de conteúdo
class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass
    
    #PROPRIEDADE
    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    # Por extender a classe controle remoto, é obrigado ter os 2 metodos
    def ligar(self):
        print("Ligando a TV")
    
    def desligar(self):
        print("Desligando a TV")

    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
    
    def desligar(self):
        print("Desligando a TV")

    @property
    def marca(self):
        return "Samsung"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)
