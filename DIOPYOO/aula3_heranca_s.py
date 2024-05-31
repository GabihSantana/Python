class Veiculo():
    def __init__(self, cor, placa, num_rodas):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}" #Retorna o nome da classe 
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    # Outro construtor dá erro:
    #def __init__(self, carregado):
        #self.carregado = carregado

    def __init__(self, cor, placa, num_rodas, carregado):
        #super chamar a implementação da classe pai
        super().__init__(cor, placa, num_rodas) #init da classe veiculo
        self.carregado = carregado

    def carga(self):
        print(f"{'Sim, estou carregado' if self.carregado else 'Não estou carregado'}")

moto = Motocicleta("branca", "fyt-0563", 2)
carro = Carro("Cinza", "xwh-2354", 4)
caminhao = Caminhao("Azul", "ref-2063", 8, False)

print(caminhao)
print(moto)
print(carro)