class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self):
        print("Removendo a instância da classe")

    def latir(self):
        print("auau")


c1 = Cachorro("Pin", "Caramelo")
c1.latir()
print("a")
del c1 # sempre será executado no final, aq estou forçando para ser executado no meio
print("a")
print("a")
print("a")