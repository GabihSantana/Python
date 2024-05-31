class Animal():
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}" #Retorna o nome da classe 

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)

        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)

        self.cor_bico = cor_bico

class Cachorro(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        super().__init__(cor_pelo = cor_pelo, cor_bico = cor_bico, nro_patas = nro_patas)

        print(Ornitorrinco.__mro__) # Ordem de resolução do python

cachorro = Cachorro(nro_patas = 4, cor_pelo = "Caramelo")
print(cachorro)

ornitorrinco = Ornitorrinco(nro_patas = 4, cor_pelo = "Preto", cor_bico = "Cinza")
print(ornitorrinco)
