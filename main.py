menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-
Opção: """

saldo = 0
limite = 500
extrato = ""
nmr_saques = 0
LIMITES_SAQUES = 3
print("============SISTEMA BANCÁRIO============")
while True:
    opcao = int(input(menu))
    print("---"*10)
    if opcao == 1:
        valor = float(input("Informe o valor a ser depósitado: R$"))
        print("---"*10)

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            print(f"Valor R${valor:.2f} Depositado na conta com sucesso")
            print("=-"*30)
        else:
            print("ERRO! O valor informado é inválido, insira um valor válido")
        print("\nRetornando ao menu...")

    elif opcao == 2:
        valor = float(input("Digite o valor a ser sacado: R$"))
        print("---"*10)

        if LIMITES_SAQUES > 0:
            if valor <= limite:
                if valor <= saldo:
                    LIMITES_SAQUES -= 1
                    saldo -= valor
                    extrato += f"Depósito: R${valor:.2f}\n"
                    print(" SUCESSO\n",f"Saque feito no valor de R${valor}")
                    print("---"*10)
                else:
                    print(" ERRO!\n","Saldo insuficiênte")
                    print("---"*10)
            else:
                print(" ERRO!\n","Valor limite de saque excedido")
                print("---"*10)
        else:
            print(" ERRO!\n","Limite de saques por dia excedido")
        print("\nRetornando ao menu...")


    elif opcao == 3:
        print("==============EXTRATO==============")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("="*30)
        print("\nRetornando ao menu...")

    elif opcao == 4:
        print("Saindo...")
        break
    else:
        print("Opção INVÁLIDA! Selecione uma opção válida")
        print("---"*10)
        print("\nRetornando ao menu...")




        
