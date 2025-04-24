import os
import pandas as pd
from tabulate import tabulate

class CSVAnalyzer:
    def __init__(self, raw_data_path, platforms):
        """
        Inicializa o analisador de CSVs com o caminho dos dados e as plataformas.
        """
        self.raw_data_path = raw_data_path
        self.platforms = platforms
        self.dataframes = {}

    def load_csvs(self):
        """
        Carrega os arquivos CSV das plataformas especificadas.
        """
        for platform in self.platforms:
            file_path = os.path.join(self.raw_data_path, f'{platform}.csv')
            if os.path.exists(file_path):
                self.dataframes[platform] = pd.read_csv(file_path)
                print(f"Dados carregados para {platform}.")
            else:
                print(f"Arquivo para {platform} não encontrado.")

    def analyze_datasets(self):
        """
        Realiza uma breve análise dos datasets carregados.
        Se os arquivos CSV ainda não foram carregados, eles serão carregados automaticamente.
        """
        # Verificar se os arquivos foram carregados
        if not self.dataframes:
            print("Os arquivos CSV ainda não foram carregados. Carregando agora...")
            self.load_csvs()

        # Verificar novamente se há dados após tentar carregar
        if self.dataframes:
            for platform, df in self.dataframes.items():
                print(f"\nAnálise para {platform}:")
                print(f"Dimensões: {df.shape}")
                print(f"Colunas: {list(df.columns)}")
                print(f"Primeiras linhas:\n{df.head()}")
        else:
            print("Nenhum dado disponível para análise.")

    def compare_columns(self):
        """
        Compara as colunas entre os datasets e exibe um resumo.
        """
        print("\nResumo da Comparação entre os Datasets:")
        columns_sets = {platform: set(df.columns) for platform, df in self.dataframes.items()}
        comparison_summary = []

        for platform1, columns1 in columns_sets.items():
            for platform2, columns2 in columns_sets.items():
                if platform1 != platform2:
                    common = columns1 & columns2
                    diff1 = columns1 - columns2
                    diff2 = columns2 - columns1
                    comparison_summary.append({
                        "Plataforma 1": platform1,
                        "Plataforma 2": platform2,
                        "Total de Colunas (Plataforma 1)": len(columns1),
                        "Total de Colunas (Plataforma 2)": len(columns2),
                        "Campos em Comum": len(common),
                        "Campos Exclusivos de Plataforma 1": len(diff1),
                        "Campos Exclusivos de Plataforma 2": len(diff2)
                    })

        # Criar um DataFrame para exibir o resumo
        summary_df = pd.DataFrame(comparison_summary)

        # Exibir o resumo em formato tabular
        print(tabulate(summary_df, headers="keys", tablefmt="fancy_grid"))

    def merge_csvs(self, output_file):
        """
        Junta os dados de todos os CSVs carregados e salva em um único arquivo.
        Se os arquivos CSV ainda não foram carregados, eles serão carregados automaticamente.
        """
        # Verificar se os DataFrames já foram carregados
        if not self.dataframes:
            print("Os arquivos CSV ainda não foram carregados. Carregando agora...")
            self.load_csvs()

        # Verificar novamente se há dados após tentar carregar
        if self.dataframes:
            merged_df = pd.concat(self.dataframes.values(), ignore_index=True)
            merged_df.to_csv(output_file, index=False)
            print(f"\nArquivo 'merge.csv' gerado com sucesso em: {output_file}")
        else:
            print("\nNenhum dado foi carregado. O arquivo 'merge.csv' não foi gerado.")

    def clean_data(self, input_file, output_file):
        """
        Realiza o tratamento básico dos dados, como remover duplicados e lidar com valores ausentes.
        """
        if not os.path.exists(input_file):
            print(f"O arquivo {input_file} não foi encontrado.")
            return

        # Carregar o arquivo merge.csv
        df = pd.read_csv(input_file)
        print(f"\nArquivo '{input_file}' carregado com sucesso.")

        # Exibir informações básicas antes do tratamento
        print("\nInformações antes do tratamento:")
        print(df.info())
        print(f"Total de linhas antes do tratamento: {len(df)}")

        # Remover duplicados
        df = df.drop_duplicates()
        print(f"Total de linhas após remover duplicados: {len(df)}")

        # Tratar valores ausentes (exemplo: remover linhas com valores nulos)
        df = df.dropna()
        print(f"Total de linhas após remover valores ausentes: {len(df)}")

        # Exibir informações básicas após o tratamento
        print("\nInformações após o tratamento:")
        print(df.info())

        # Salvar o arquivo tratado
        df.to_csv(output_file, index=False)
        print(f"\nArquivo tratado salvo com sucesso em: {output_file}")