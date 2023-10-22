#LARIRODAS RU: 4467033
def cadastrarPeca(codigo):
    nome = input("Digite o nome da peça: ")
    fabricante = input("Digite o fabricante da peça: ")
    valor = float(input("Digite o valor da peça: "))

    peca = {
        "Código": codigo,
        "Nome": nome,
        "Fabricante": fabricante,
        "Valor": valor
    }

    return peca


def consultarTodasPecas(pecas):
    print("----- Todas as Peças Cadastradas -----")
    for peca in pecas:
        print("Código:", peca["Código"])
        print("Nome:", peca["Nome"])
        print("Fabricante:", peca["Fabricante"])
        print("Valor:", peca["Valor"])
        print("-------------------------------------")


def consultarPecasPorCodigo(pecas):
    codigo = int(input("Digite o código da peça: "))

    for peca in pecas:
        if peca["Código"] == codigo:
            print("----- Peça Encontrada -----")
            print("Código:", peca["Código"])
            print("Nome:", peca["Nome"])
            print("Fabricante:", peca["Fabricante"])
            print("Valor:", peca["Valor"])
            print("---------------------------")
            return

    print("Nenhuma peça encontrada com o código", codigo)


def consultarPecasPorFabricante(pecas):
    fabricante = input("Digite o fabricante da peça: ")

    print("----- Peças do Fabricante", fabricante, "-----")
    for peca in pecas:
        if peca["Fabricante"] == fabricante:
            print("Código:", peca["Código"])
            print("Nome:", peca["Nome"])
            print("Valor:", peca["Valor"])
            print("------------------------------------")


def removerPeca(pecas):
    codigo = int(input("Digite o código da peça a ser removida: "))

    for peca in pecas:
        if peca["Código"] == codigo:
            pecas.remove(peca)
            print("Peça removida com sucesso!")
            return

    print("Nenhuma peça encontrada com o código", codigo)


def sair():
    print("Finalizando programa...")


def main():
    pecas = []
    codigo = 1

    while True:
        print("----- Menu Principal -----")
        print("1. Cadastrar Peça")
        print("2. Consultar Peça")
        print("3. Remover Peça")
        print("4. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            peca = cadastrarPeca(codigo)
            pecas.append(peca)
            codigo += 1
            print("Peça cadastrada com sucesso!")

        elif opcao == "2":
            print("----- Menu de Consulta -----")
            print("1. Consultar Todas as Peças")
            print("2. Consultar Peças por Código")
            print("3. Consultar Peças por Fabricante")
            print("4. Retornar")

            consulta_opcao = input("Digite o número da opção desejada: ")

            if consulta_opcao == "1":
                consultarTodasPecas(pecas)
            elif consulta_opcao == "2":
                consultarPecasPorCodigo(pecas)
            elif consulta_opcao == "3":
                consultarPecasPorFabricante(pecas)
            elif consulta_opcao == "4":
                 main()
            else:
                print("Opção inválida. Tente novamente.")

        elif opcao == "3":
            removerPeca(pecas)

        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

        print()


print('Bem vindo(a) ao controle de estoque da Bicicletaria Lari Rodas RU: 4467033')
main()
