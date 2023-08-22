import textwrap   

def menu():
    menu = ("""
        >>>>>>> Selecione uma operação: <<<<<<<
                [c] - Criar Conta Corrente
                [u] - Usuário
                [l] - Listar Conta
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
    listar(conta)
    print("------------------------")
    print("\n\nNão houve movimentações na conta bancária" if not extrato else extrato)
    print(f"\n\nSALDO: R$ {saldo:.2f}")
    print("\n\n==============================================\n")
    
    return saldo, extrato

def cadastro_usuario(usuario):
    cpf = input("Informe seu CPF (somente os números): ")
    usuarios = verificar_usuario(cpf, usuario)


    if usuarios:
        input("\nO CPF informado já pertence a um usuário! ")
        return

    else:
        nome = input("Informe o nome completo: ")
        data_nasc = input("Informe a data de Nascimento (dd-mm-aaaa): ")
        end = print("Informe o endereço ")
        log = input("Logradouro: ")
        num = input("Número: ")
        bai = input("Bairro: ")
        cid = input("Cidade: ")
        es = input("Estado: ")
        end = log, num, bai, cid, es

        usuario.append({"nome": nome, "data_nasc": data_nasc, "cpf": cpf, "end": end})
        print("=== Usuário cadastrado com sucesso!===")

def verificar_usuario(cpf, usuarios):
    verificar_usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return verificar_usuario[0] if verificar_usuario else None

def conta_corrente(AG, numero_conta, usuario):
    cpf = input("Informe o CPF (somente os números): ")
    usuarios = verificar_usuario(cpf, usuario)

    if usuarios:
        print("\n === Conta criada com sucesso! === ")
        return({"ag": AG, "nmr": numero_conta, "usuario": usuario})

    print("\nUsuário não cadastrado - Criação de conta encerrada!")


def listar(conta):
    print("Agência:", conta["ag"])
    print("C/C:", conta["nmr"])

    for titular in conta["usuario"]:
        print("Titular:", titular['nome'])

saldo = 0
extrato = ""
numero_saques = 0
usuario = [ ]
conta = [ ]
numero_conta = 1
VALOR_LIMITE = 500
LIMITE_SAQUE = 3
AG = "0001"

while True:
    operacao = menu()

    if operacao == "c":
        conta = conta_corrente(AG, numero_conta, usuario)

        if conta:
            numero_conta = numero_conta + 1

    elif operacao == 'l':
        listar(conta)

    elif operacao == 'u':
        cadastro_usuario(usuario)

    elif operacao == 'd':
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
        exibir_extrato(saldo = saldo, extrato = extrato)

    elif operacao == 'x':
        print("Obrigado pela preferência!")
        break
    
    else:
        print("Operação não reconhecida!")