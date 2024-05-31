class Foo():
    def __init__(self, x = None):
        self._x = x

    @property #retornar valor -> property
    def x(self):
        return self._x or 0
    
    @x.setter #settar valor => setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0

foo = Foo(10)
print(foo.x)
foo.x = 10
del foo.x
print(foo.x)

class Pessoa():
    def __init__(self, nome, ano_nasc):
        self._nome = nome
        self._ano_nasc = ano_nasc
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nasc
        
pessoa = Pessoa("Julia", 2005)
print(f"Nome: {pessoa.nome} \t Idade: {pessoa.idade}")