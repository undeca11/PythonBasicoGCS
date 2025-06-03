######################################################
###  S C R A P P I N G   P A R A    M O N G O D B  ###
######################################################
### Prof. Filipo Mor - junho de 2025               ###
######################################################

import pandas as pd
from pymongo import MongoClient

# Função para conectar ao MongoDB Atlas
def conectar_mongodb(uri, db_nome):
    print(":::==> Conectando ao MongoD Atlas...")
    client = MongoClient(uri)
    db = client[db_nome]
    print(":::==> Conectado com sucesso!")
    return db

# Verifica se a coleção existe e cria se não existir
def verificar_ou_criar_colecao(db, nome_colecao):
    if nome_colecao not in db.list_collection_names():
        print(F":::==> Collection {nome_colecao} não existe! criando... ")
        db.create_collection(nome_colecao)
    return db[nome_colecao]

# ETAPA DE EXTRAÇÃO
def extrair(caminho_origem):
    print(":::==> Extraindo dados de vendas...")
    vendas = pd.read_csv(caminho_origem)
    return vendas

# ETAPA DE TRANSFORMAÇÃO
def transformar(vendas):
    print(":::==> Transformando dados...")
    resultado = vendas.groupby(['produto', 'região']).agg({
        'preço_unitario': 'sum',
        'quantidade': 'sum'
    }).reset_index()
    resultado['receita_total'] = resultado['preço_unitario'] * resultado['quantidade']
    resultado = resultado[['produto', 'região', 'receita_total']]
    return resultado

# ETAPA DE CARGA NO MongoDB
def carregar_no_mongodb(resultado_df, db, colecao_nome):
    colecao = verificar_ou_criar_colecao(db, colecao_nome)
    # Convertendo DataFrame para dict e inserindo na coleção
    registros = resultado_df.to_dict(orient='records')
    colecao.insert_many(registros)
    print(f":::==> {len(registros)} registros inseridos na coleção '{colecao_nome}'.")

def main():
    caminho_origem = 'vendas.csv'
    mongo_uri = 'sua_string_de_conexao_mongodb_atlas'  # Insira sua conexão aqui
    db_nome = 'Exemplo_scrapping_dados_Vendas'
    colecao_nome = 'vendas_analitico'

    # Conectar ao MongoDB
    db = conectar_mongodb(mongo_uri, db_nome)
    # Executar ETL
    vendas = extrair(caminho_origem)
    resultado = transformar(vendas)
    # Gravar no MongoDB
    carregar_no_mongodb(resultado, db, colecao_nome)
    print("Processo concluído com sucesso!")

if __name__ == '__main__':
    main()

