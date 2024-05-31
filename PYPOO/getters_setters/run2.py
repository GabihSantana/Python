class MinhaClasse:
    def __init__(self) -> None:
        self.__valor = None

    #settando o valor
    def setter_valor(self, valor: int) -> None:
        self.__valor = valor
    
    @property #olha para o método como se fosse um atributo da classe
    def getter_valor(self) -> int:
        return self.__valor

my_class = MinhaClasse()
my_class.setter_valor(123)
print(my_class.getter_valor)