# 🔍 Identificador de Bandeiras de Cartão de Crédito com Regex

Este projeto tem como objetivo desenvolver uma aplicação simples e eficiente capaz de **identificar a bandeira de um cartão de crédito** (Visa, MasterCard, Elo, entre outras) com base no número do cartão informado pelo usuário.

Utilizando **expressões regulares (regex)** e boas práticas de desenvolvimento em Python, a aplicação analisa o número e retorna a respectiva bandeira. O projeto também ilustra como ferramentas de IA, como o **GitHub Copilot**, podem ser utilizadas para aumentar a produtividade e qualidade do código.

---

## 📌 Descrição do Desafio

O desafio propõe a construção de uma aplicação funcional que, a partir do número do cartão, **detecta corretamente a bandeira** utilizando os **BINs (Bank Identification Numbers)**. Esses BINs correspondem aos primeiros dígitos do cartão, que seguem padrões específicos por bandeira.

Durante o processo, o GitHub Copilot foi utilizado como assistente de codificação para:
- Sugerir trechos de código;
- Ajudar na criação de expressões regulares complexas;
- Agilizar o processo de estruturação e validação da lógica.

---

## 🎯 Objetivos de Aprendizagem

Ao concluir este desafio, você será capaz de:

✅ Reproduzir e/ou melhorar um projeto com base em um código existente;  
✅ Aplicar os conceitos aprendidos em um cenário real de validação de dados;  
✅ Documentar seu raciocínio técnico e decisões de forma clara e organizada;  
✅ Utilizar o GitHub como plataforma para versionamento e exposição do seu trabalho.

---

## 🧠 Tecnologias e Conceitos Utilizados

- 🐍 **Python 3.10+**
- ✨ **Expressões Regulares (Regex)**
- 📌 **BIN Ranges (Bank Identification Numbers)**
- 🤖 **GitHub Copilot (IA para desenvolvimento assistido)**
- 🧪 Validação de Entrada e Limpeza de Dados
- 🧹 Boas práticas de organização, tipagem e legibilidade

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```
### 2. Execute o script:
python main.py

### 3. Digite o número do cartão quando solicitado e veja a bandeira identificada.

---

## 🧾 Exemplos de Uso
```bash
Digite o número do cartão: 4111111111111111
Bandeira: Visa

Digite o número do cartão: 5500000000000004
Bandeira: Mastercard

Digite o número do cartão: 340000000000009
Bandeira: American Express
```
---

## 💡 Melhorias Futuras

✅ Implementar verificação de validade com o Algoritmo de Luhn.
✅ Criar uma interface gráfica (GUI) para facilitar o uso por leigos.
✅ Adicionar testes automatizados com pytest.
✅ Disponibilizar como API com Flask ou FastAPI.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias ou novas funcionalidades.

---

## 🧠 Licença

Este projeto está licenciado sob a MIT License. Consulte o arquivo LICENSE para mais detalhes.

---

## ✍️ Autor
Desenvolvido por Mateus Ribeiro.
Com suporte da IA GitHub Copilot 🤖