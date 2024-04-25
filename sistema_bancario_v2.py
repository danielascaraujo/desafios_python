def menu():
    menu = """
    ========= Escolha uma opção: =========

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo usuário
    [5] Nova Conta
    [0] Sair

    => """
    return input((menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\nDepósito efetuado com sucesso!")
            
    else: 
        print("\nNão foi possível efetuar o depósito! O valor informado é inválido.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_numero_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nNão foi possível efetuar o saque! Saldo insuficiente")
            
    elif excedeu_limite:
        print("\nNão foi possível efetuar o saque! O valor solicitado excedeu o limite disponível.")

    elif excedeu_numero_saques:
        print("\nNão foi possível efetuar o saque! Número máximo de saques excedido.")
            
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque efetuado com sucesso!")

    else: 
        print("\nNão foi possível efetuar o saque! O valor informado é inválido.")    

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def novo_usuario(usuarios):
    cpf = input("\nDigite o CPF do usuário (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n Usuário já cadastrado ")
        return

    nome = input("\nDigite o nome completo do usuário: ")
    data_nascimento = input("\nDigite a data de nascimento (dd-mm-aaaa): ")
    endereco = input("\nDigite o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\nUsuário cadastrado com sucesso!")

def nova_conta(agencia, numero_conta, usuarios ):
    cpf = input("\Informe o CPF do usuário (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\nConta cadastrada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    return("\nUsuário não encontrado!")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("\nInforme o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)


        elif opcao == "2":
            valor = float(input("\nInforme o valor do saque: "))

            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)


        elif opcao == "3": 
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            novo_usuario(usuarios)
        
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "0":
            break

        else:
            print("Operação inválida! Por favor, selecione corretamente a opção desejada.")

main()
