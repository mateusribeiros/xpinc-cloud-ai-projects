
# Análise de Vendas Meganium - Relatório Estratégico

## Análise Exploratória dos Dados

O arquivo "Meganium_Sales_Data.csv" contém os seguintes campos:
- SKU: Identificador único do produto
- product_sold: Nome do produto vendido
- date: Data da venda
- quantity: Quantidade vendida
- unit_price: Preço unitário
- total_price: Valor total da venda
- currency: Moeda da transação
- site: Plataforma de venda (AliExpress, Etsy, Shopee)
- discount_coupon/discount_value: Informações sobre descontos
- buyer_birth_date/buyer_name: Dados do comprador
- delivery_country: País de entrega
- invoice_id: Identificador único da venda

Não há dados faltantes ou discrepâncias significativas no conjunto fornecido.

## Produtos Mais Populares por País

### Análise Quantitativa

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_csv('Meganium_Sales_Data.csv')

# Agrupar por país e produto para ver as quantidades vendidas
popular_products = df.groupby(['delivery_country', 'product_sold'])['quantity'].sum().unstack()

# Exportar para CSV
popular_products.to_csv('Meganium_Regional_Demand.csv')

# Visualização
plt.figure(figsize=(12, 8))
sns.heatmap(popular_products.fillna(0), annot=True, fmt='g', cmap='YlGnBu')
plt.title('Demanda de Produtos por País')
plt.tight_layout()
plt.savefig('demanda_por_pais.png')
plt.close()
```

### Principais Insights:

1. **Austrália**:
   - Produto mais vendido: NEW MEGANIUM RG28XX (11 unidades)
   - Seguido por: NEW MEGANIUM RG CubeXX (8 unidades)

2. **Canadá**:
   - Produto mais vendido: NEW MEGANIUM RG 40XXV (19 unidades)
   - Alto volume também para: NEW MEGANIUM RG35XX (15 unidades)

3. **França**:
   - Produto mais vendido: NEW MEGANIUM RG35XX (12 unidades)
   - Bom desempenho de: MEGANIUM RG353M (11 unidades)

4. **Alemanha**:
   - Produto mais vendido: NEW MEGANIUM RG28XX (8 unidades)
   - Seguido por: MEGANIUM RG353M (7 unidades)

5. **Japão**:
   - Produto mais vendido: NEW MEGANIUM RG 40XXV (12 unidades)
   - Seguido por: MEGANIUM RG353M (7 unidades)

6. **Reino Unido**:
   - Produto mais vendido: NEW MEGANIUM RG35XX (7 unidades)
   - Seguido por: MEGANIUM RG353M (5 unidades)

7. **Estados Unidos**:
   - Volume menor, mas com preferência por: MEGANIUM RG353M (4 unidades)

## Otimização Logística e Transporte

### 1. Padrões Regionais de Demanda

- **Mercados Premium (Japão, Canadá)**: Tendência para modelos de maior valor (RG 40XXV e RG353M)
- **Mercados de Valor Médio (França, Reino Unido)**: Preferência pelo RG35XX
- **Mercados Sensíveis a Preço (Austrália, Alemanha)**: Maior demanda pelo modelo mais acessível (RG28XX)

### 2. Sugestões de Alocação Inicial por Região:

| Região        | Modelo Prioritário | Modelo Secundário | Observações                     |
|---------------|--------------------|-------------------|---------------------------------|
| Canadá        | RG 40XXV           | RG35XX            | Alta demanda por modelos premium|
| Japão         | RG 40XXV           | RG353M            | Mercado premium consistente     |
| França        | RG35XX             | RG353M            | Mix equilibrado                 |
| Alemanha      | RG28XX             | RG353M            | Sensível a preço               |
| Austrália     | RG28XX             | RG CubeXX         | Demanda por modelos acessíveis |
| Reino Unido   | RG35XX             | RG353M            | Padrão similar à França        |
| EUA           | RG353M             | -                 | Mercado pequeno mas consistente|

### 3. Otimização de Cadeia de Suprimentos:

1. **Pré-alocação Regional**:
   - Enviar containers mistos apenas para regiões com demanda diversificada (França, Reino Unido)
   - Enviar containers especializados para mercados com preferências claras (Japão/Canadá: modelos premium; Alemanha/Austrália: modelos acessíveis)

2. **Estoque em Trânsito**:
   - Manter estoque mínimo de RG28XX e RG35XX em hubs europeus para redistribuição rápida
   - Estocar RG 40XXV e RG353M próximo aos mercados premium (Ásia-Pacífico e América do Norte)

3. **Parcerias Logísticas**:
   - Priorizar acordos com transportadoras que tenham hubs regionais próximos aos mercados-alvo
   - Negociar contratos de longo prazo para rotas de alto volume (Europa-Canadá-Japão)

## Conclusões Estratégicas

1. **Otimização de Produção**:
   - Aumentar capacidade de produção do RG 40XXV para atender demanda do Canadá e Japão
   - Manter produção estável do RG28XX para mercados sensíveis a preço

2. **Estratégia de Distribuição**:
   - Implementar modelo de pré-alocação regional baseado nos padrões identificados
   - Estabelecer hubs regionais estratégicos para reduzir custos de redistribuição

3. **Monitoramento Contínuo**:
   - Implementar sistema de coleta mensal de dados de vendas para ajustar alocações
   - Estabelecer KPIs de giro de estoque por região e modelo

Esta análise permite à Meganium alinhar sua produção e logística com as preferências reais de cada mercado, reduzindo custos operacionais e aumentando a satisfação dos varejistas e consumidores finais.
