def menu():
    print ("""
    ======================================
        Selecione uma operação:

        [a]: ADICIONAR UM ITEM NA LISTA
        [r]: REMOVER UM ITEM DA LISTA
        [v]: VER OS ITENS DA LISTA
        [x]: Sair
    =======================================
    """)
    sel = input(": ")
    return sel

def op_adc():
    add = input("\nO que deseja adicionar?: ")

    if to_do.count(add) >= 1:
        ask = input("\nDeseja adicionar esse item novamente?(S/N) ")

        if ask == 's' or ask == 'S':
            to_do.append(add)
            print("\nItem adicionado novamente em sua lista!")
        else:
            print("\nItem cancelado!")

    else:
        to_do.append(add)

        

def op_rmv():
    remv = input("\nO que deseja remover?: ")
    to_do.remove(remv)

    return to_do

def op_see():
    for Item, *lista in enumerate(to_do):
        print(f"\n{Item} -", *lista, end = "\n")

    if (len(to_do) == 0):
        print("\nLista vazia!")

to_do = [ ]

while True:
    op = menu()

    if op == 'a':
        op_adc()

    elif op == 'r':
        to_do = op_rmv()

    elif op == 'v':
        op_see()
        
    elif op == 'x':
        print("\nObrigada por utilizar nossos serviços!")
        break

    else:
        break