def realizar_deposito(saldo, extrato):

  valor = obter_valor("Informe o valor do depósito: ")

  if valor > 0:

    saldo += valor

    extrato += f"Depósito: R$ {valor:.2f}\n"

  else:

    print("Operação falhou! O valor informado é inválido.")

  return saldo, extrato



def realizar_saque(saldo, extrato, numero_saques, limite_saques):

  valor = obter_valor("Informe o valor do saque: ")

  excedeu_saldo = valor > saldo

  excedeu_limite = valor > limite_saques

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

  else:

    print("Operação falhou! O valor informado é inválido.")

  return saldo, extrato, numero_saques



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



def exibir_extrato(saldo, extrato):

  print("\n================ EXTRATO ================")

  print("Não foram realizadas movimentações." if not extrato else extrato)

  print(f"\nSaldo: R$ {saldo:.2f}")

  print("==========================================")





saldo = 0

limite = 500

extrato = ""

numero_saques = 0

LIMITE_SAQUES = 3



menu = """

[d] Depositar

[s] Sacar

[e] Extrato

[q] Sair

=> """



while True:

  opcao = input(menu)



  if opcao == "d":

    saldo, extrato = realizar_deposito(saldo, extrato)

  elif opcao == "s":

    saldo, extrato, numero_saques = realizar_saque(saldo, extrato, numero_saques, limite)

  elif opcao == "e":

    exibir_extrato(saldo, extrato)

  elif opcao == "q":

    break

  else:

    print("Operação inválida, por favor selecione novamente a operação desejada.")
