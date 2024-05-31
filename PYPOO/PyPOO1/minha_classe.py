# Self -> O método está dentro da classe
class MinhaClasse:
    # METODO CONTRUTOR --executa primeiro > Atributo
    def __init__(self, info, elem):
        self.atributo_1 = "meu atributo"
        self.atributo_2 = elem
        self.atributo_3 = [1, 2, "n"]
        self.new_atribute = info
        print(self.new_atribute)

    def metodo_1(self):
        print("Minha ação 1")
        print("Minha ação 2")
        print(self.atributo_2)
        return "Ola mundo"
    
    def metodo_2(self, numero):
        self.metodo_1()
        print(self.atributo_3[1] + numero)

# Objeto         Classe -> instaciamos um objeto
minha_classe = MinhaClasse("info aqui no construtor", 213)

minha_classe.metodo_2(3)

class Pessoa():
    def __init__(self, altura, idade) -> None:
        self.altura = altura     # ATRIBUTOS
        self.idade = idade    # ATRIBUTOS
        print(f"A sua altura é de {self.altura} aos {self.idade} anos")

    # MÉTODOS
    def correr(self):
        print("Você está correndo")

    def comer(self):
        print("Você está comendo")

pessoa = Pessoa("1.54", 43)
pessoa.correr()
pessoa.comer()