import os
import random
from dados import Dados


def escolha_lista_dados(escolhas):
    lista_dados = Dados()
    resultado = []
    for escolha in escolhas:
        if escolha == 1:
            resultado.append("Nome: " + random.choice(lista_dados.nomes))
        elif escolha == 2:
            resultado.append("Email: " + random.choice(lista_dados.emails))
        elif escolha == 3:
            resultado.append("Telefone: " + random.choice(lista_dados.telefones))
        elif escolha == 4:
            resultado.append("Cidade: " + random.choice(lista_dados.cidades))
        elif escolha == 5:
            resultado.append("Estado: " + random.choice(lista_dados.estados))
        else:
            print("Erro: Contate o programador")
            exit()
    return resultado


"""
Como criar e modificar arquivos:
'w' -> Usado somente para escrever algo
'a' -> Usado para acrescentar algo
'r' -> Usado somente para ler algo
'r+' -> Usado para ler e escrever algo
"""


def modificar_criar_arquivos(file, mode, dados):
    with open(file, mode, encoding="utf-8", newline="") as arquivo_txt:
        try:
            arquivo_txt.write("-" * 20 + os.linesep)
            for dado in dados:
                arquivo_txt.write(str(dado) + os.linesep)
            print(f"Arquivos adicionados com sucesso {file}")
        except Exception as error:
            print(f"Ocorreu um erro: {error}")
