import pandas as pd


# ETAPA DE EXTRAÇÃO
def extrair(caminho_origem):
    print("Extraindo dados de vendas...")
    vendas = pd.read_csv(caminho_origem)
    return vendas


# ETAPA DE TRANSFORMAÇÃO
def transformar(vendas):
    print("Transformando dados...")
    # Agrupando por 'produto' e 'região', somando as colunas 'preço_unitario' e 'quantidade' usando agg()
    receita_por_produto_regiao = vendas.groupby(['produto', 'região']).agg({
        'preço_unitario': 'sum',
        'quantidade': 'sum'
    }).reset_index()

    # Calculando receita total
    receita_por_produto_regiao['receita_total'] = receita_por_produto_regiao['preço_unitario'] * \
                                                  receita_por_produto_regiao['quantidade']

    # Selecionando colunas relevantes
    resultado = receita_por_produto_regiao[['produto', 'região', 'receita_total']]
    return resultado

# ETAPA DE CARGA
def carregar(resultado, caminho_destino):
    print("Carregando resultados...")
    resultado.to_csv(caminho_destino, index=False)


def main():
    caminho_origem = 'vendas.csv'  # Arquivo de entrada (exemplo)
    caminho_destino = 'resultado_receita.csv'

    vendas = extrair(caminho_origem)
    resultado = transformar(vendas)
    carregar(resultado, caminho_destino)
    print("Processo ETL concluído com sucesso!")


if __name__ == '__main__':
    main()

