from time import sleep
from dados import dados


def programa_dados_input():
    options = [1, 2, 3, 4, 5]
    while True:
        print()
        print("Escolha uma ou mais opções abaixo a serem geradas aleatóriamente")
        option = input(
            """Digite sua(s) escolha(s) separadas por vírgula 

                        [1] - Nome
                        [2] - E-mail
                        [3] - Telefone
                        [4] - Cidade
                        [5] - Estado 
                        [0] - parar

                        Escolha sua opção: """
        )
        option_user = [int(escolha) for escolha in option.split(",")]
        # Verificar se a opção escolhida é 0. Caso seja encerra o programa
        if 0 in option_user:
            print(f"Sua escolha foi: {option}. Programa sendo finalizado..")
            sleep(2)
            exit()

        # Verificar se todas as opções escolhidas estão em 'options'
        if all(opt in options for opt in option_user):
            return option_user
        else:
            print("Opções inválidas. Por favor, escolha novamente.")


def programa_dados_processos():
    option = programa_dados_input()
    if not None in option:
        escolher_options = dados.escolha_lista_dados(option)
        options = ["s", "n"]
        while True:
            print()
            option_salvar = input(
                "Você gostaria de salvar dados em um arquivo de texto? (s/n)"
            ).lower()

            if option_salvar in options:
                break  # Sai do loop se a opção inserida for válida
            else:
                print(
                    "Opção inválida. Por favor, escolha 's' para sim ou 'n' para não."
                )

        # O código continua aqui após a escolha válida do usuário
        if option_salvar == "s":
            print()
            print("Salvando dados em um arquivo de texto...")
            dados.modificar_criar_arquivos(dados.Dados.file_path, "a", escolher_options)
            print(escolher_options)
        else:
            print()
            print("Não será salvo em um arquivo de texto.")
            print("Imprimindo o dados gerados..")
            print()
            for option_user in escolher_options:
                print(option_user)
