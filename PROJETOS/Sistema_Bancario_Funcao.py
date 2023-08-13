import textwrap   

def menu():
    menu = ("""
        >>>>>>> Selecione uma operação: <<<<<<<

                [d] - Depositar
                [s] - Sacar 
                [e] - Ver extrato
                [x] - Sair

        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        """)
    return input(textwrap.dedent(menu))

def depositar(deposito, saldo, extrato):
    if deposito <= 0:
        print("Valor inválido!")
    else:
        print("""
        Realizando depósito...
        Obrigado pela preferência!
        """)

        saldo += deposito
        extrato += f"\nDepósito: R$ {deposito:.2f}"

    return saldo, extrato

def sacar(*, saque, numero_saques, saque_limite, limite, extrato, saldo):    
    valor_invalido = saque > saldo
    valor_limite = saque > limite
    limite_saque = numero_saques >= saque_limite
    
    if valor_invalido:
        print("ERRO - Saldo insuficiente!")

    elif valor_limite:
        print("ERRO - Valor ultrapassou o limite!")

    elif limite_saque:
        print("ERRO - O número máximo de saques diários foi atingido!")
    
    elif saque <= 0:
        print("ERRO - Valor inválido!")
    
    else:
        print("""
        Realizando saque...
        Por favor, retire no caixa.
        Obrigado pela preferência!
        """)

        numero_saques += 1
        saldo -= saque
        extrato += f"\nSaque: R$ {saque:.2f}"

    return saldo, extrato, numero_saques

def exibir_extrato(*, saldo, extrato):
    print("================= EXTRATO =================\n")
    print("Não houve movimentações na conta bancária" if not extrato else extrato)
    print(f"\n\nSALDO: R$ {saldo:.2f}")
    print("\n\n==============================================\n")
    
    return saldo, extrato

saldo = 0
extrato = ""
numero_saques = 0
VALOR_LIMITE = 500
LIMITE_SAQUE = 3    

while True:
    operacao = menu()

    if operacao == 'd':
        deposito = float(input("Valor do depósito: R$ "))
        saldo, extrato = depositar(deposito, saldo, extrato)

    elif operacao == 's':
        saque = float(input("Valor de saque: R$ "))

        saldo, extrato, numero_saques = sacar(
            saque = saque,
            numero_saques = numero_saques,
            saque_limite = LIMITE_SAQUE,
            limite = VALOR_LIMITE,
            extrato = extrato,
            saldo = saldo,
            )

    elif operacao == 'e':
        exibir_extrato(saldo = saldo, extrato = extrato,)

    elif operacao == 'x':
        print("Obrigado pela preferência!")
        break;
    
    else:
        print("Operação não reconhecida!")