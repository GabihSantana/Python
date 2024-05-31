class Pessoa:
    #   Método construtor:
    def __init__(self, altura, cpf) -> None:
        #   Atributos:
        self.altura = altura
        self.__cpf = cpf #Identificar q está trabalhando com atributos privados

    #   Métodos
    def apresentar(self):
        print(f"Olá! Minha altura: {self.altura}")
        self.__coletar_documento()# Método privado só é acessado dentro da própria classe
    
    # Declarar o método com 2_ -> está escondendo (private)
    # Métodos privados só são acessados dentro da própria classe
    def __coletar_documento(self):
        print(f"Meu documento: {self.__cpf}")

Jorge = Pessoa("1.70","dsferedfers")
Jorge.__cpf = "rewedf"
print(Jorge.__cpf)
Jorge.apresentar()