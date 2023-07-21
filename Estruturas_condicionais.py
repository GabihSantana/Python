MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Infome sua idade: \n"))

if idade >= MAIOR_IDADE:
    print("Maior de Idade - Pode tirar a CNH!")

elif idade == IDADE_ESPECIAL:
    print("Pode dirigir acompanhado com alguém que possui CNH")

else:
    print("Menor de Idade - Não pode tirar CNH")