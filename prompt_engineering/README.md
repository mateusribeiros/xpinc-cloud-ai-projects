# Projeto de Prompts para Gerar Insights de Relatórios de Vendas

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-green)]

---

## 🚀 Visão Geral

Este projeto explora o uso de prompts com ferramentas de inteligência artificial para analisar relatórios de vendas e extrair insights valiosos. Por meio de prompts bem estruturados, interpretamos dados de diferentes plataformas, identificamos padrões de comportamento e geramos conclusões que apoiam decisões estratégicas de negócio.

**Objetivos de Aprendizagem**

- Gerar insights estratégicos para a tomada de decisão.
- Aplicar conceitos de IA e análise de dados em um ambiente prático.
- Documentar processos técnicos de forma clara e estruturada.
- Utilizar o GitHub como ferramenta para compartilhar documentação e artefatos do projeto.

---

## 📋 Conteúdo deste README

1. [Cenário de Negócio](#cenário-de-negócio)
2. [Estrutura do Repositório](#estrutura-do-repositório)
3. [Componentes Principais](#componentes-principais)
4. [Resultados e Insights](#resultados-e-insights)
5. [Como Começar](#como-começar)
6. [Inspiração & Próximos Passos](#inspiração--próximos-passos)
7. [Contribuição](#contribuição)
8. [Licença](#licença)

---

## 🎯 Cenário de Negócio

A Meganium fabrica consoles eletrônicos e terceiriza distribuição e vendas para terceiros (AliExpress, Shopee, Etsy). Cada plataforma gera relatórios próprios, resultando em:

- **Dados fragmentados**: CSVs distintos por região e canal.
- **Desafios de qualidade**: duplicatas, formatos inconsistentes e valores ausentes.
- **Necessidade de insights rápidos**: ajuste ágil de produção, marketing e logística.

---

## 🗂️ Estrutura do Repositório

```
project_base/
├── data/
│   ├── raw_data/           # CSVs originais de cada plataforma
│   │   ├── Meganium_Sales_Data_-_AliExpress.csv
│   │   ├── Meganium_Sales_Data_-_Shopee.csv
│   │   ├── Meganium_Sales_Data_-_Etsy.csv
│   │   └── merge.csv       # Base consolidada
│   └── processed_data/     # Dados tratados
│       └── Meganium_Sales_Data.csv
├── prompts/
│   ├── chatgpt/
│   │   ├── gpt_prompt.md   # Resultados do ChatGPT
│   │   └── figures/        # Gráficos gerados pelo ChatGPT
│   └── deepseek/
│       └── deepseek_prompt.md  # Resultados do Deepseek
├── scripts/
│   ├── csv_analyzer.py     # Classe para análise e limpeza de CSVs
│   └── main.py             # Pipeline de ETL e geração de relatórios
├── README.md               # Documentação do projeto
└── requirements.txt        # Dependências Python
```

---

## 📚 Prompts Utilizados

### Prompt Completo Utilizado

**Instrução Principal (Objetivo Claro e Específico):**
Analisar os dados de vendas em `Meganium_Sales_Data.csv` e transformar dados de vendas em informações relevantes para o fabricante; quais são os produtos mais populares em cada país e como consolidar o processo de logística e transporte até o momento da venda.

**Contexto:**
A Meganium é uma empresa global especializada exclusivamente na fabricação de consoles eletrônicos. No entanto, ela não atua na distribuição ou venda direta de seus produtos, delegando essas etapas a terceiros.
Atualmente, a empresa enfrenta um problema logístico: como não tem acesso direto aos dados de vendas e preferências regionais, acaba enviando consoles sem precisão sobre a demanda de cada mercado. Isso resulta em:
- Alocação ineficiente de produtos (ex.: containers com consoles menos desejados em certas regiões);
- Retrabalho e custos adicionais (ex.: necessidade de redistribuição);
- Oportunidades perdidas (ex.: poderiam enviar mais unidades de modelos populares em regiões específicas).
A falta de visibilidade sobre as preferências regionais prejudica a eficiência da cadeia de suprimentos, impactando negativamente a operação global da Meganium.

**Restrições/Limitações:**
- Escopo: Focar exclusivamente em insights para o fabricante (não incluir sugestões para varejistas).
- Nível Técnico: Saída compreensível para diretoria (evitar jargões técnicos).
- O banco de dados `Meganium_Sales_Data.csv` já está tratado e organizado corretamente.
- Não se limitar a análises apenas logísticas.

**Formato de Saída:**
- Visualizações (gráficos, heatmaps de demanda regional).
- Relatório textual com insights estratégicos.
- Novo CSV processado (ex.: `Meganium_Regional_Demand.csv`).
- (Opcional) Código Python para reprodução da análise.

**Conteúdo Principal:**
Disponibilizarei a base `Meganium_Sales_Data.csv` que contém os dados consolidados de vendas das empresas terceiras: Shopee, AliExpress e Etsy. As empresas são identificadas através da coluna `site`. Essa base de dados será o principal instrumento de análise do qual você precisará destrinchar; analise as colunas, estabeleça relações, relevâncias e realize o que é pedido no prompt.

**Tarefa Adicional:**

**Análise Exploratória:**
- Quais colunas existem? (ex.: região, modelo, vendas, estoque);
- Dados faltantes ou discrepâncias.

**Processamento:**
- Como os dados foram agrupados (ex.: por região/modelo);
- Métricas calculadas (ex.: demanda relativa, sazonalidade).

**Artefatos Gerados:**
- Descrição de cada saída (ex.: "Heatmap mostra demanda por modelo na Europa").

**Instrução (Reforçada):**
Analisar os dados de vendas em `Meganium_Sales_Data.csv` e transformar dados de vendas em informações relevantes para o fabricante; quais são os produtos mais populares em cada país e como consolidar o processo de logística e transporte até o momento da venda.

---

## 📈 Resultados e Insights

Os resultados detalhados e insights gerados pelos prompts estão disponíveis nos arquivos abaixo:

- [Resultados via ChatGPT 👇](prompts/chatgpt/gpt_prompt.md)
- [Resultados via Deepseek 👇](prompts/deepseek/deepseek_prompt.md)

---

## ⚙️ Como Começar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio/project_base
   ```
2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Prepare os dados**: coloque os CSVs originais em `data/raw_data/`.
4. **Execute o pipeline**:
   ```bash
   python scripts/main.py
   ```
5. **Visualize os resultados**:
   - Dados tratados em `data/processed_data/`.
   - Gráficos em `prompts/*/figures/`.
   - Insights completos em `prompts/chatgpt/gpt_prompt.md` e `prompts/deepseek/deepseek_prompt.md`.

---

## 🤝 Contribuição

Contribuições são bem-vindas!

1. Faça um fork.
2. Crie uma branch: `git checkout -b minha-feature`.
3. Envie um pull request.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

