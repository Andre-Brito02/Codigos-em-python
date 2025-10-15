def menu_de_opcoes():
    return """

    [c] Cadastrar cliente
    [l] Listar clientes cadastrados
    [d] Depositar
    [e] Extrato
    [s] Sacar
    [q] Sair

    => """
    
def realizar_deposito(saldo, extrato, /):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return extrato, saldo

def realizar_saque(*, saldo, limite, numero_saques, LIMITE_SAQUES, extrato):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque realizado!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return extrato, saldo, numero_saques

def verificar_extrato(saldo,/,*, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")        

def cadastrar_cliente(lista_de_clientes, nome_dos_clientes_cadastrados):
    cliente = {}
    cpf_unicos = []
    
    cliente['nome'] = input("Digite seu nome: ")
    cliente['data_nascimento'] = input("Digite a data de nascimento no formato DD/MM/AAAA: ")
    cpf = input("Digite seu cpf(SOMENTE NÚMEROS): ")
    cpf_unicos, cpf = verifica_cpf(cpf_unicos, cpf)
    cliente['cpf'] = cpf
    nome_dos_clientes_cadastrados.append(cliente['nome'])
    
    logradouro = input("Digite seu logradouro e o número: ")
    bairro = input("Digite seu bairro: ")
    cidade = input("Digite sua cidade: ")
    sigla_estado = input("Digite a sigla do seu estado: ")
    separador = '/'
    cidade_estado = separador.join([cidade.title(),sigla_estado.upper()])
    endereco = f'Logradouro: {logradouro}, Bairro: {bairro}, Cidade/Estado: {cidade_estado}'

    lista_de_clientes.append(cliente)
    lista_de_clientes.append(endereco)
    
    return lista_de_clientes, nome_dos_clientes_cadastrados

def verifica_cpf(cpf_unicos, cpf):
    if cpf not in cpf_unicos:
        print("Validação de CPF concluída, CPF cadastrado\n")
        cpf_unicos.append(cpf)
    else:
        print("CPF já cadastrado no sistema.")
        novo_cpf = input("Digite o cpf correto: ")
        verifica_cpf(cpf_unicos, novo_cpf)
    
    return cpf_unicos, cpf

def listar_todos_clientes(nome_dos_clientes_cadastrados):
    if nome_dos_clientes_cadastrados:
        for indice, nome in enumerate(nome_dos_clientes_cadastrados):
            print(f"{indice+1}: {nome}")
    else:
        print("Sem clientes cadastrados no sistema") 
        
if __name__ == "__main__":
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    lista_de_clientes = []
    nome_dos_clientes_cadastrados = []
    associacao_conta_cliente = []
    
    while True:
        opcao = input(menu_de_opcoes())
        
        match(opcao):
            case "c":
                lista_de_clientes, nome_dos_clientes_cadastrados = cadastrar_cliente(lista_de_clientes, nome_dos_clientes_cadastrados)
            case "d":
                extrato, saldo = realizar_deposito(saldo, extrato)
            case "e":
                verificar_extrato(saldo, extrato=extrato)
            case "s":
                extrato, saldo, numero_saques = realizar_saque(saldo=saldo, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES, extrato=extrato)
            case "l":
                listar_todos_clientes(nome_dos_clientes_cadastrados)
            case "q":
                print("Finalizando a operação. Volte sempre")
                break
            case _:
                print("Operação inválida, por favor selecione novamente a operação desejada.")
