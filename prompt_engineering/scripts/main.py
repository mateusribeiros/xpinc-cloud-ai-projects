import os
from csv_analyzer import CSVAnalyzer

# Caminho para a pasta contendo os arquivos CSV
raw_data_path = os.path.join(os.path.dirname(__file__), '../data/raw_data')

# Lista de plataformas a serem analisadas
platforms = ['Meganium_Sales_Data_-_AliExpress', 
             'Meganium_Sales_Data_-_Etsy', 
             'Meganium_Sales_Data_-_Shopee']

# Instanciar o analisador de CSVs
analyzer = CSVAnalyzer(raw_data_path, platforms)

# Gerar o arquivo merge.csv diretamente
merge_file = os.path.join(os.path.dirname(__file__), '../data/raw_data/merge.csv')
analyzer.merge_csvs(merge_file)

# Realizar o tratamento básico dos dados
cleaned_file = os.path.join(os.path.dirname(__file__), '../data/processed_data/Meganium_Sales_Data.csv')
analyzer.clean_data(merge_file, cleaned_file)

raw_data_path2 = os.path.join(os.path.dirname(__file__), '../data/processed_data')
plataform2 = 'Meganium_Sales_Data'

analyzer2 = CSVAnalyzer(raw_data_path2, [plataform2])
analyzer2.analyze_datasets()