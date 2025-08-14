import textwrap as tw

def menu_conta(): 
    menu_conta = """
    =====================================
    Sistema bancário
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [x] Sair

    =====================================
    Digite uma opção -> """
    return input(tw.dedent(menu_conta))

def menu_inicial(): 
    menu_inicial = """
    =====================================
    Sistema bancário
    
    [c] Cadastrar Usuário
    [b] Criar Conta Bancária
    [a] Acessar conta
    [x] Sair

    =====================================
    Digite uma opção -> """
    return input(tw.dedent(menu_inicial))

def cadastrar_usuario(usuarios):
    print("""
          ===================
          Cadastro de usuário
          ===================    
    """)
    try:
        
        cpf_entrada = input("Qual o CPF do usuário? (somente numeros) ")

        if cpf_entrada in usuarios.keys():
            print("Erro! Usuário ja cadastrado.")
            return

        nome = input("Digite o seu nome completo: ")
        data_nascimento = input("Digite o sua data de nascimento: (dd-mm-aaaa)")
        endereco = input("Digite o seu endreço completo: (Logradouro, Numero - Bairro - Cidade/UF)")

        usuarios[cpf_entrada] = {"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}

        print("""
            ==================
            Usuário Cadastrado 
            ==================    
        """)   

    except ValueError:
        print("Ocorreu um erro ao inserir o CPF, tente novamente.")

def criar_conta(usuarios):
    print("""
          =================
          Criação de contas
          =================    
    """)
    try:    

        cpf = input("Digite o CPF do usuário: ")

        if cpf not in usuarios.keys():
            print("Usuário não consta no banco de dados do banco, criação de contas não realizado")
            return

        numero_conta, agencia = gerar_numero_conta()
        if numero_conta and agencia:
            print("""
                =========================
                Conta criada com sucesso!
                ========================= 
            """)    
            return {"agencia": agencia, "numero_conta": numero_conta, "cpf": cpf, "dados": {"saldo": 0, "limite": 500, "extrato": [], "LIMITE_SAQUES": 3, "numero_saques": 0}}
    except ValueError:
        return

def gerar_numero_conta():
    numero_conta_inicial = 0
    agencia = "0001"
    numero_conta = numero_conta_inicial + 1
    return numero_conta, agencia

def main():
    usuarios= {}
    contas = []

    while True:
        opcao = menu_inicial()

        if opcao == "c":
            cadastrar_usuario(usuarios)

        elif opcao == "b":
            conta = criar_conta(usuarios)
            if conta:
                contas.append(conta)
        
        elif opcao == "a":
            print("""
                =============
                Acessar conta
                =============    
            """)
            cpf_titular = input("Digite o CPF do titular: ")

            for conta in contas:
                cpf = conta.get("cpf")

                if cpf == cpf_titular:
                    print(f"""
                        ============================
                        Agencia: {conta.get("agencia")}
                        C/C: {conta.get("numero_conta")}
                        Titular: {usuarios.get(cpf).get("nome")}
                        ============================    
                    """)

                else:
                    print("Não há contas nesse CPF.")
                    continue
                print(usuarios)
                print(contas)
                escolha_numero_conta = int(input("Digite o numero da conta que deseja acessar: "))

                for conta in contas:
                    if escolha_numero_conta == conta.get("numero_conta") and conta.get("cpf") == cpf_titular:
                        acessar_conta(conta)

        elif opcao == "x":
            print("Saindo do sistema...")
            break

def acessar_conta(conta):
    while True:
        opcao = menu_conta()     

        if opcao == "d":
            try:
                valor_deposito = float(input("Digite o valor que deseja depositar: "))
                if valor_deposito > 0:
                    conta["dados"]["saldo"] += valor_deposito
                    conta["dados"]["extrato"] += [f"Deposito no valor de R${valor_deposito:.2f} - Saldo: R${conta["dados"]["saldo"]:.2f}"]
                    print(f"Deposito no valor de R${valor_deposito:.2f} realizado com sucesso!")
                else:
                    print("Valor invalido, tente novamente.")
            except ValueError:
                print("Valor invalido, tente novamente.")

        elif opcao == "s":

            if conta["dados"]["numero_saques"] >= conta["dados"]["LIMITE_SAQUES"]:
                print("Numero de saques diários exede o limite")

            else:

                try:
                    valor_saque = float(input("Digite o valor que deseja sacar: "))

                    if valor_saque > 500:
                        print("Valor do saque exede o limite")

                    elif valor_saque > 0 and valor_saque <= conta["dados"]["saldo"]:
                        conta["dados"]["saldo"] -= valor_saque
                        conta["dados"]["numero_saques"] += 1
                        conta["dados"]["extrato"] += [f"Saque no valor de R${valor_saque:.2f} - Saldo: R${conta["dados"]["saldo"]:.2f}"]
                        print(f"Saque no valor de R${valor_saque:.2f} realizado com sucesso!")

                    else:
                        print("Saldo Insuficiente.")

                except ValueError:
                    print("Opção invalida, tente novamente.")

        elif opcao == "e":

            print("Extrato da conta:")
            for transacao in conta["dados"]["extrato"]:
                print(transacao)
            print(f"Saldo Atual = R${conta["dados"]["saldo"]:.2f}")

        elif opcao == "x":
            print("Saindo da conta...")
            break

        else:
            print("Opção invalida, tente novamente.")

main()
                