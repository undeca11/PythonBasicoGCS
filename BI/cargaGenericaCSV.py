###################################################################
###  L O A D E R   C S V   P A R A   M O N G O D B   A T L A S  ###
###################################################################
### Prof. Filipo Mor - junho de 2025                            ###
###################################################################

import os
import csv
from pymongo import MongoClient

# Configurações
MONGO_URI = 'sua_string_de_conexao_mongodb_atlas'  # Sua string de conexão do MongoDB Atlas
NOME_BANCO_DE_DADOS = 'CargaCSVGenerica'  # Nome do seu banco de dados


def conectar_mongodb(uri, db_nome):
    client = MongoClient(uri)
    db = client[db_nome]
    return db


def carregar_csv_para_mongodb(caminho_csv, db):
    # Extrair o nome do arquivo (sem a extensão) para usar como nome da coleção
    nome_arquivo = os.path.basename(caminho_csv)
    nome_colecao = os.path.splitext(nome_arquivo)[0]

    print(f"Iniciando a carga do arquivo '{nome_arquivo}' para a coleção '{nome_colecao}'...")

    colecao = db[nome_colecao]
    total_linhas = 0

    try:
        with open(caminho_csv, 'r', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)

            # Processar e inserir em lotes para melhor desempenho
            batch = []
            batch_size = 1000  # Tamanho do lote (ajuste conforme necessário)

            for linha in leitor_csv:
                batch.append(linha)
                total_linhas += 1

                if len(batch) >= batch_size:
                    colecao.insert_many(batch)
                    print(f"Inseridas {total_linhas} linhas na coleção '{nome_colecao}'.")
                    batch = []  # Limpar o lote

            # Inserir as linhas restantes, caso haja
            if batch:
                colecao.insert_many(batch)
                print(f"Inseridas {total_linhas} linhas na coleção '{nome_colecao}'.")

            print(f"Arquivo '{nome_arquivo}' carregado com sucesso para a coleção '{nome_colecao}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao carregar o arquivo: {e}")


def main():
    # Solicitar o caminho do arquivo CSV ao usuário
    caminho_csv = input("Por favor, insira o caminho completo para o arquivo CSV: ")

    # Conectar ao MongoDB
    db = conectar_mongodb(MONGO_URI, NOME_BANCO_DE_DADOS)

    # Carregar o CSV para o MongoDB
    carregar_csv_para_mongodb(caminho_csv, db)


if __name__ == "__main__":
    main()

