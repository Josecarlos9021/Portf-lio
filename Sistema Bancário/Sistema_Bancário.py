# Menu inicial
menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair


    => """

# Variáveis
saldo = 0
limite = 500
total_sacado_dia = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Loop infinito
while True:
    opcao = input(menu).lower()

# Lógica do depósito
    if opcao == "d":
        print("\nDepósito...")
        valor = int(input("\nDigite o valor que deseja depositar: "))
        if valor < 0:
            print("\nATENÇÃO! Operação inválida, não é possível depositar saldo negativo.")
        else:
            saldo += valor
            extrato += f"- Deposito: R$ {valor}\n"
            print(f"- Depósito de R$ {valor} realizado com sucesso!")

# Lógica do saque
    elif opcao == "s":
        print("\nSaque...")
        valor = int(input("Digite o valor que deseja sacar: "))
        if valor <= 0:
            print("\nATENÇÃO! Operação inválida, não é possível sacar saldo zerado ou negativo.")
        elif valor > saldo:
            print("- ATENÇÃO! Saldo insuficiente.")
        elif numero_saques >= LIMITE_SAQUES:
            print("- ATENÇÃO! Limite de saques atingidos (máximo 3 saques/dia).")
        elif total_sacado_dia + valor > limite:
            print("- ATENÇÃO! O valor de saque excede o máximo permitido(R$500/dia).")
            print(f"- Você sacou até agora {total_sacado_dia}.")
        else:
            saldo -= valor
            extrato += f"- Saque: R$ {valor}\n"
            numero_saques += 1
            total_sacado_dia += valor
            print(f"- Saque de R$ {valor} realizado com sucesso!")

# Lógica do extrato
    elif opcao == "e":
        print("\nExtrato...")
        print("-"*20)
        if not extrato:
            print("\nNão foram realizadas movimentações.\n")
        else:
            print(f"\n{extrato}")
        print("-"*20)
        print(f"- Saldo da conta bancária: {saldo}.")

# Lógica do break
    elif opcao == "q":
        print("\nSaindo...")
        print("Obrigado por usar nosso serviço. Volte sempre!\n")
        break

# lógica final, caso nenhuma condição for atendida
    else:
        print("\nOpção inválida, por favor, selecione novamente a operação desejada.")