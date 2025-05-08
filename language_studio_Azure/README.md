# Laboratório Prático: Azure Speech Studio e Language Studio

> Desafio realizado como parte do curso na DIO (Digital Innovation One) com o objetivo de aplicar e aprofundar conhecimentos práticos em inteligência artificial voltada para **voz e linguagem natural** usando ferramentas da Microsoft Azure.

---

## 🧠 Descrição do Desafio

Este laboratório tem como objetivo explorar, na prática, os serviços do **Azure Speech Studio** e **Language Studio**, com foco na **análise de fala** e **processamento de linguagem natural** (NLP). O projeto visa a consolidação do aprendizado por meio da construção de soluções reais e da documentação das etapas realizadas.

---

## 🎯 Objetivos de Aprendizagem

Ao concluir este desafio, você será capaz de:

- Aplicar os conceitos aprendidos em um ambiente prático;
- Desenvolver soluções com foco em voz e linguagem natural usando IA;
- Documentar os processos técnicos de forma clara e estruturada;
- Utilizar o GitHub para compartilhamento de conhecimento técnico.

---

## 🛠️ Ferramentas Utilizadas

- [Azure Speech Studio](https://speech.microsoft.com/)
- [Azure Language Studio](https://language.cognitive.azure.com/)
- Git & GitHub
- Markdown

---

## 🚀 Etapas Realizadas

### 🔊 1. Azure Speech Studio — Análise de Fala

**Objetivo:** Realizar transcrição automática de voz (Speech to Text) e geração de voz (Text to Speech).

#### Etapas:

1. **Criação de recurso do Speech na Azure**
   - Região: Brazil South
   - Plano: F0 (Gratuito)

2. **Speech to Text**
   - Upload de arquivos de áudio (.wav e .mp3)
   - Teste com diferentes sotaques e velocidades de fala
   - Análise da precisão da transcrição
   - Extração de insights sobre performance e melhorias

3. **Text to Speech**
   - Criação de mensagens personalizadas usando voz neural
   - Testes com diferentes vozes (masculina, feminina, neutra)
   - Ajuste de entonação, pausa e velocidade com SSML (Speech Synthesis Markup Language)

4. **Exportação de resultados**
   - Download dos áudios gerados
   - Registro dos testes em anotações

---

### 🧾 2. Azure Language Studio — Processamento de Linguagem Natural

**Objetivo:** Aplicar técnicas de NLP para extrair informações, detectar sentimentos e entender a estrutura da linguagem.

#### Etapas:

1. **Criação de recurso de Language na Azure**
   - Utilização do plano gratuito (F0)

2. **Text Analytics**
   - Análise de sentimentos (positivo, negativo, neutro)
   - Extração de frases-chave
   - Detecção de idioma
   - Reconhecimento de entidades nomeadas (NER)

3. **Customização (opcional)**
   - Treinamento de modelo de classificação de texto
   - Teste com dados simulados

4. **Comparação dos resultados**
   - Validação dos resultados obtidos com base no contexto dos textos
   - Documentação dos acertos e limitações percebidas

---

## 📒 Anotações e Insights

- A qualidade do áudio afeta diretamente a transcrição no Speech Studio.
- A voz neural oferece resultados muito realistas e personalizáveis.
- O Language Studio apresenta excelente performance para textos simples e curtos, com boa extração de sentimentos.
- É possível integrar essas ferramentas em aplicações reais via API com SDKs em Python, C#, Node.js, entre outros.

---

## 📌 Considerações Finais

Este repositório serve como base de estudos e referência para aplicações futuras com foco em IA, voz e linguagem natural. Mesmo com limitações de crédito na Azure, é possível continuar experimentando via **plano gratuito** ou com alternativas de código aberto.

---

## ✍️ Autor

**Mateus**  
Estudante de tecnologia | Entusiasta em IA e Segurança da Informação  
[GitHub](https://github.com/mateusribeiros) | [LinkedIn](https://linkedin.com/in/mateusribeiros)


