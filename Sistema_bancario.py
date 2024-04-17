import textwrap
import os

def realizar_deposito(usuario):
    valor = obter_valor("Informe o valor do depósito: ")
    if valor > 0:
        if 'contas' in usuario and usuario['contas']:
            conta = usuario['contas'][0]  # Vamos assumir que o usuário tem apenas uma conta por enquanto
            conta['saldo'] += valor
            conta['extrato'] += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Usuário não possui conta associada.")
    else:
        print("Operação falhou! O valor informado é inválido.")


def realizar_saque(usuario, limite_saques):
    valor = obter_valor("Informe o valor do saque: ")
    excedeu_saldo = valor > usuario['saldo']
    excedeu_limite = valor > limite_saques
    excedeu_saques = usuario['numero_saques'] >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        usuario['saldo'] -= valor
        usuario['extrato'] += f"Saque: R$ {valor:.2f}\n"
        usuario['numero_saques'] += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

def obter_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor >= 0:
                return valor
            else:
                print("O valor deve ser maior ou igual a zero.")
        except ValueError:
            print("Valor inválido. Por favor, insira um número válido.")

def exibir_extrato(usuario):
    if 'contas' in usuario and usuario['contas']:
        conta = usuario['contas'][0]  # Vamos assumir que o usuário tem apenas uma conta por enquanto
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not conta['extrato'] else conta['extrato'])
        print(f"\nSaldo: R$ {conta['saldo']:.2f}")
        print("==========================================")
    else:
        print("Usuário não possui conta associada.")

def nova_conta(usuarios):
    cpf = input("Digite o CPF do titular da conta: ")
    if cpf not in usuarios:
        print("CPF não encontrado.")
        return
    
    # Buscar o nome associado ao CPF informado
    nome_titular = usuarios[cpf]['nome']
    
    numero_conta = input("Digite o número da conta: ")
    
    # Verificar se o número da conta já existe para este usuário
    if 'contas' in usuarios[cpf]:
        for conta in usuarios[cpf]['contas']:
            if conta['numero'] == numero_conta:
                print("Essa conta já está cadastrada para este usuário.")
                return
    
    saldo_inicial = float(input("Digite o saldo inicial da conta: "))
    
    # Criar a conta e vinculá-la ao CPF do usuário
    if 'contas' not in usuarios[cpf]:
        usuarios[cpf]['contas'] = []
    usuarios[cpf]['contas'].append({'nome': nome_titular, 'numero': numero_conta, 'saldo': saldo_inicial, 'extrato': '', 'numero_saques': 0})
    print("Conta criada com sucesso!")


def criar_usuario(usuarios):
    nome = input("Digite o nome: ")
    data_nascimento = input("Digite a data de nascimento (DD-MM-AAAA): ")
    print("Antes do loop de verificação do CPF")  # Mensagem de depuração
    while True:
        cpf = input("Digite o seu CPF: ")
        if cpf in usuarios:
            print("CPF já cadastrado. Por favor, digite outro CPF.")
        else:
            break
    print("Depois do loop de verificação do CPF")  # Mensagem de depuração
    endereco = input("Digite o seu endereço: ")
    usuarios[cpf] = {'nome': nome, 'data_nascimento': data_nascimento, 'endereco': endereco}
    print("Usuário criado com sucesso!")

def listar_contas(usuarios):
    print("\n================ LISTA DE CONTAS ================")
    for cpf, dados in usuarios.items():
        if 'contas' in dados:
            for conta in dados['contas']:
                print(f"CPF: {cpf}, Nome: {dados['nome']}, Data de Nascimento: {dados['data_nascimento']}, Endereço: {dados['endereco']}, Número da Conta: {conta['numero']}, Saldo: {conta['saldo']:.2f}")
    print("==================================================")

limite_saques = 3
usuarios = {}

def menu():
    menu = """\n
    ================== MENU ==================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar contas
    [nu]\tNovo Usuário
    [q]\tSair
    =>"""
    os.system('clear')  # Limpa o buffer do terminal
    return input(textwrap.dedent(menu))

while True:
    print("Antes de exibir o menu")  # Mensagem de depuração
    opcao = menu()  # Exibir o menu
    print("Depois de exibir o menu")  # Mensagem de depuração

    if opcao == "d":
        cpf = input("Digite o CPF do titular da conta: ")
        if cpf in usuarios:
            realizar_deposito(usuarios[cpf])
        else:
            print("CPF não encontrado.")
    elif opcao == "s":
        cpf = input("Digite o CPF do titular da conta: ")
        if cpf in usuarios:
            realizar_saque(usuarios[cpf], limite_saques)
        else:
            print("CPF não encontrado.")
    elif opcao == "e":
        cpf = input("Digite o CPF do titular da conta: ")
        if cpf in usuarios:
            exibir_extrato(usuarios[cpf])
        else:
            print("CPF não encontrado.")
    elif opcao == "nc":
        nova_conta(usuarios)
    elif opcao == "lc":
        listar_contas(usuarios)
    elif opcao == "nu":
        print("Antes de criar usuário")  # Mensagem de depuração
        criar_usuario(usuarios)
        print("Depois de criar usuário")  # Mensagem de depuração
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
