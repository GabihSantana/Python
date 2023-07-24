saldo = 0
extrato = ""
numero_saques = 0
VALOR_LIMITE = 500
SAQUE_LIMITE = 3

menu = ("""
     >>>>>>>Selecione uma operação:<<<<<<<

            [1] - Depositar
            [2] - Sacar 
            [3] - Ver extrato
            [4] - Sair

    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    """)

while True:
    print(menu)
    operacao = int(input("Insira o número da operação: "))

    if operacao == 1:

        deposito = float(input("Digite o valor a ser depositado: "))

        if deposito < 0:
            print("Erro na operação - Valor de depósito inválido!")
        else:
            print("""
                Realizando o depósito...
                Deposito realizado!
            """)
            saldo += deposito
            extrato += f"\nDepósito: R$ {deposito:.2f}"

    elif operacao == 2:

        limite_saque = numero_saques >= SAQUE_LIMITE

        if limite_saque:
            print("\nErro na Operação - O limite de saques diário foi atingido!")
            print("Obrigado pela preferência de nossos serviços!")

        else:
            saque = float(input("Digite o valor do saque: "))

            if saque > VALOR_LIMITE:
                print("\nErro na Operação - O valor limite de saque foi atingido!")

            elif saque > saldo:
                print("\nErro na operação - Saldo insuficiente!")
            
            elif saque < 0:
                print("\nErro na operação - Valor de saque inválido!")

            else:
                print("Saque realizado com sucesso!")
                print("Retire o valor no caixa!")

                numero_saques += 1
                saldo -= saque
                extrato += f"\nSaque: R$ {saque:.2f}"
    
    elif operacao == 3:

        print("================= EXTRATO =================\n")
        print("Não houve movimentações na conta bancária" if not extrato else extrato)
        print(f"\n\nSALDO: R$ {saldo:.2f}")
        print("\n\n==============================================\n")

    elif operacao == 4:
        print("\nObrigado pela preferência de nossos serviços!")
        break

    else:
        print("Operação não identificada! - Por favor, selecione uma operação válida")