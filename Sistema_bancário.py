menu ="""
    =====================================
    Sistema bancário
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [x] Sair

    =====================================
    """
saldo = 0
limite = 500
extrato = []
LIMITE_SAQUES = 3
numero_saques = 0

while True:
    print(menu)
    opcao = input("Digite sua opção: ")

    if opcao == "d":
        try:
            valor_deposito = float(input("Digite o valor que deseja depositar: "))
            if valor_deposito > 0:
                saldo += valor_deposito
                extrato += [f"Deposito no valor de R${valor_deposito:.2f} - Saldo: R${saldo:.2f}"]
                print(f"Deposito no valor de R${valor_deposito:.2f} realizado com sucesso!")
            else:
                print("Valor invalido, tente novamente.")
        except ValueError:
            print("Valor invalido, tente novamente.")
    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Numero de saques diários exede o limite")
        else:
            try:
                valor_saque = float(input("Digite o valor que deseja sacar: "))
                if valor_saque > 500:
                    print("Valor do saque exede o limite")
                elif valor_saque > 0 and valor_saque <= saldo:
                    saldo -= valor_saque
                    numero_saques += 1
                    extrato += [f"Saque no valor de R${valor_saque:.2f} - Saldo: R${saldo:.2f}"]
                    print(f"Saque no valor de R${valor_saque:.2f} realizado com sucesso!")
                else:
                    print("Saldo Insuficiente.")
            except ValueError:
                print("Opção invalida, tente novamente.")
    elif opcao == "e":
        print("Extrato da conta:")
        for transacao in extrato:
            print(transacao)
        print(f"Saldo Atual = R${saldo:.2f}")
    elif opcao == "x":
        print("Saindo do sistema...")
        break
    else:
        print("Opção invalida, tente novamente.")
                