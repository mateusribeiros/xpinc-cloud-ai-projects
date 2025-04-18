# 💾 Criação de Instância SQL Gerenciada no Azure

> Repositório com resumos, anotações e dicas sobre o processo de criação de uma instância de Banco de Dados no Microsoft Azure.

---

## 🧠 Objetivo do Projeto

Este repositório foi criado como parte do desafio prático da **DIO (Digital Innovation One)**. O objetivo é aplicar os conhecimentos adquiridos durante as aulas sobre o **Microsoft Azure** e documentar a experiência técnica na configuração de uma **Instância Gerenciada de SQL**.

---

## 🎯 Objetivos de Aprendizagem

Ao final deste desafio, fui capaz de:

- ✅ Aplicar conceitos aprendidos em um ambiente prático;
- ✅ Criar e configurar uma instância gerenciada de banco de dados SQL no Azure;
- ✅ Documentar cada etapa de forma clara e estruturada;
- ✅ Utilizar o GitHub como ferramenta de versionamento e compartilhamento técnico.

---

## 🛠️ Tecnologias e Ferramentas

- **Microsoft Azure**
- **Azure SQL Managed Instance**
- **Git e GitHub**
- **Markdown**


---

## 🚀 Etapas: Como Criar uma Instância SQL Gerenciada no Azure

Com base na [documentação oficial da Microsoft](https://learn.microsoft.com/pt-br/azure/azure-sql/managed-instance/instance-create-quickstart?tabs=azure-portal), segui o seguinte passo a passo:

### 1. Acesse o Portal Azure

- Vá até [portal.azure.com](https://portal.azure.com) e faça login com sua conta Microsoft.

### 2. Crie um Grupo de Recursos

- Acesse **Grupos de recursos > Criar**.
- Nomeie como `rg-sql-azure` (exemplo).
- Selecione a região desejada.
- Clique em **Revisar + criar** e depois em **Criar**.

### 3. Criar a Instância SQL Gerenciada

- Vá até **Instâncias Gerenciadas SQL > Criar**.
- Preencha os dados:
  - **Assinatura**
  - **Grupo de Recursos**
  - **Nome da instância** (ex: `instancia-sql-lab`)
  - **Região**
  - **Usuário admin e senha**
  - **Camada de preço** (uso gratuito se possível)

### 4. Configurar Rede

- Selecione uma **Rede Virtual** (existente ou nova).
- Configure o DNS gerenciado.
- Ative o **acesso público** se necessário para testes.

### 5. Revisar + Criar

- Verifique os dados e clique em **Criar**.
- Aguarde a implantação da instância (pode levar até 30 minutos).

### 6. Acessar e Testar

- Copie o **nome do host** da instância.
- Use um cliente como SSMS para conectar via:
  - Host: `nomedainstancia.database.windows.net`
  - Usuário/senha definidos

---

## 📝 Notas e Dicas

- 🔐 Habilite regras de firewall para seu IP local.
- 🚫 Não exponha a instância em produção com acesso público.
- 🧪 Para testes rápidos, o acesso remoto pode ser temporariamente liberado.
- 🧹 Lembre-se de excluir a instância e os recursos se não forem mais necessários para evitar custos.

---

## 📎 Recursos Úteis

- [Documentação Oficial Microsoft Learn](https://learn.microsoft.com/pt-br/azure/azure-sql/managed-instance/instance-create-quickstart?tabs=azure-portal)
- [GitHub Markdown Guide](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github)
- [GitHub Quick Start](https://github.com/githubtraining/hellogitworld)

---

## 📬 Entrega

- ✅ Repositório público com README completo
- ✅ Anotações organizadas
- ✅ Capturas de tela na pasta `/images`
- ✅ Submissão realizada via plataforma DIO

---

## 👨‍💻 Autor

**Mateus**  
📍 Bootcamp XP Inc – Cloud com IA  

