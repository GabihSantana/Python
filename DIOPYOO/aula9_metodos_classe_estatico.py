class Pessoa:
    def __init__(self, nome = None, idade = None):
        self.nome = nome 
        self.idade = idade

    @classmethod
    def calcular_idade(cls, ano, mes, dia, nome):
        print(cls)
        idade = 2024 - ano
        return cls(nome, idade) 
    
    @staticmethod
    def maior_idade(idade):
        return idade >= 18
    
p1 = Pessoa.calcular_idade(2005, 3, 21, "Gabi") 
print(p1.nome, p1.idade)

print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(14))
