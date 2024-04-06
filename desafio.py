menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito efetuado com sucesso!")
        
        else: 
            print("Não foi possível efetuar o depósito! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_numero_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Não foi possível efetuar o saque! O valor solicitado excedeu o saldo disponível.")
        
        elif excedeu_limite:
            print("Não foi possível efetuar o saque! O valor solicitado excedeu o limite disponível.")

        elif excedeu_numero_saques:
            print("Não foi possível efetuar o saque! Número máximo de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque efetuado com sucesso!")

        else: 
            print("Não foi possível efetuar o saque! O valor informado é inválido.")    

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
       break

    else:
        print("Operação inválida! Por favor, selecione corretamente a opção desejada.")

