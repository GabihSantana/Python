class Bicicleta :
    # Método construtor / inicializador 
    def __init__(self, cor, modelo, ano, valor) -> None:
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Trim trim")

    def parar(self):
        print("Parando bicicleta")
        print("Biciclata parada")

    def correr(self):
        print("Vrummmmm")

    #print(b1):
    def __str__(self):
        #return f"\nBicicleta: \n Cor: {self.cor}, Modelo: {self.modelo}, Ano: {self.ano}, Valor: R${self.valor}"
            #Automatizado:
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}" #Retorna o nome da classe 
    
    # Método destrutor: __del__ -> instância(obj) é destruída, mas ñ é muito utilizado pois python tem um coletos de lixo que lida com o gerenciamento de memória

b1 = Bicicleta ("azul", "caloi", 2021, 400)
b1.buzinar()
b1.correr()
b1.parar()

Bicicleta .buzinar(b1)

print(b1.cor, b1.ano, b1.modelo, b1.valor)
print(b1)