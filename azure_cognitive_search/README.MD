# 💡 Desafio Prático: Organização e Pesquisa de Documentos com IA

> Desafio realizado como parte do curso na DIO com foco em aplicar **técnicas de ingestão de dados e indexação inteligente**, utilizando ferramentas de Inteligência Artificial para extrair conhecimento de grandes volumes de informação.

---

## 🧠 Descrição do Desafio

Este laboratório tem como objetivo aplicar conceitos de **organização e pesquisa de documentos** por meio da **ingestão de conteúdo**, **criação de índices inteligentes** e **exploração dos dados estruturados**. As ferramentas de inteligência artificial utilizadas permitem transformar documentos brutos em fontes consultáveis de conhecimento.

---

## 🎯 Objetivos de Aprendizagem

Ao concluir este desafio, você será capaz de:

- Aplicar técnicas práticas de ingestão e indexação de dados;
- Compreender como IA pode facilitar a organização e extração de informações;
- Documentar os processos técnicos de forma clara e reutilizável;
- Utilizar o GitHub como repositório técnico e de portfólio profissional.

---

## 🛠️ Ferramentas e Tecnologias Utilizadas

- Microsoft Azure Cognitive Search
- Azure Blob Storage
- Azure AI Document Intelligence (ex-Form Recognizer)
- Python (opcional)
- Git & GitHub
- Markdown

---

## 🔄 Etapas Realizadas

### 📥 1. Ingestão de Conteúdo

**Objetivo:** Preparar e enviar documentos para armazenamento e análise.

#### Ações realizadas:

- Criação de um **Azure Blob Storage** para armazenar os arquivos PDF/DOCX.
- Upload de diferentes documentos com variações de estrutura (currículos, contratos, relatórios etc.).
- Testes de compatibilidade com arquivos escaneados e nativos.
- Registro de arquivos processados e estrutura de diretórios utilizada.

---

### 🧠 2. Análise e Extração com AI Document Intelligence

**Objetivo:** Usar IA para entender o conteúdo dos documentos enviados.

#### Ações realizadas:

- Configuração do recurso **Document Intelligence (Form Recognizer)**.
- Aplicação de modelos pré-treinados:
  - Extração de tabelas, campos e parágrafos;
  - Reconhecimento de entidades (datas, valores, nomes).
- Exportação dos resultados em JSON.
- Validação e análise dos campos extraídos automaticamente.

---

### 🗂️ 3. Indexação com Azure Cognitive Search

**Objetivo:** Criar um mecanismo de busca semântica inteligente sobre os documentos.

#### Ações realizadas:

- Criação do serviço **Azure Cognitive Search**.
- Conexão com o Blob Storage como fonte de dados.
- Criação de **Índice inteligente** com campos como: título, conteúdo, autores, datas.
- Criação de um **Indexer automático** para manter os dados atualizados.
- Teste da pesquisa com diferentes termos e filtros.

---

### 🔎 4. Exploração e Visualização

**Objetivo:** Testar a recuperação de documentos e interpretar os resultados da IA.

#### Ações realizadas:

- Utilização do painel de busca integrado da Azure para realizar consultas.
- Análise da relevância dos resultados e ajuste de pesos dos campos.
- Considerações sobre o desempenho e limites da IA em contextos reais.
- Reflexão sobre possíveis aplicações práticas (busca jurídica, currículo, contratos, etc.).

---

## 📒 Anotações e Insights

- A qualidade e formatação dos documentos impactam diretamente a precisão da extração de dados.
- O uso conjunto de **Blob Storage**, **Document Intelligence** e **Cognitive Search** proporciona um pipeline robusto para mineração de conhecimento.
- A estruturação dos índices exige planejamento, pois influencia diretamente a qualidade da busca.
- Mesmo com o plano gratuito da Azure, é possível realizar testes eficientes e gerar valor técnico real.


---

## 📌 Considerações Finais

Este projeto mostra como **IA pode ser aplicada na organização inteligente de documentos**, abrindo espaço para soluções empresariais nas áreas de RH, jurídico, administrativo e educação. O aprendizado prático foi essencial para consolidar o uso de pipelines de ingestão e busca com inteligência artificial.

---

## ✍️ Autor

**Mateus**  
Estudante de Tecnologia | Focado em IA aplicada e Soluções de Automação  
[GitHub](https://github.com/mateusribeiros) | [LinkedIn](https://linkedin.com/in/mateusribeiros)

