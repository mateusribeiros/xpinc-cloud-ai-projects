# 🚀 Desafio: Criando e Configurando uma Máquina Virtual no Microsoft Azure

Este repositório foi criado como parte do desafio da DIO, com o objetivo de consolidar os aprendizados sobre a criação e configuração de máquinas virtuais na plataforma Microsoft Azure. Aqui você encontrará um conjunto de anotações, resumos, dicas práticas e capturas de tela que documentam todo o processo.

---

## 🧠 Objetivos do Projeto

- ✅ Praticar a criação de uma máquina virtual no Azure de forma prática e objetiva.
- ✅ Documentar o processo técnico com clareza e organização.
- ✅ Compartilhar conhecimento técnico por meio do GitHub, estimulando a colaboração e o aprendizado contínuo.

---

## 💡 O que você vai encontrar aqui?

📄 **Resumo dos Conceitos**  
📌 Anotações sobre o portal do Azure, recursos e boas práticas.

⚙️ **Passo a Passo da Criação de VM**  
📌 Etapas detalhadas com comandos, configurações e observações importantes.

🧩 **Dicas e Problemas Comuns**  
📌 Sugestões úteis para evitar erros e agilizar o processo de criação.

🖼 **Capturas de Tela (opcional)**  
📌 Registro visual do processo, disponível na pasta `/images`.

---

## 🔧 Tecnologias e Ferramentas Utilizadas

- Microsoft Azure (Portal)
- Git & GitHub
- Markdown
- Sistema Operacional: Windows/Linux

---

## 📌 Etapas Realizadas

1. Acesso e login no [Portal Azure](https://portal.azure.com)
2. Navegação até o recurso "Máquinas Virtuais"
3. Criação de uma nova VM com:
   - Imagem: Windows Server 2019
   - Tamanho: B1s (uso gratuito elegível)
   - Autenticação via usuário/senha
   - Configuração de rede e regras de entrada
4. Acesso remoto via RDP
5. Testes e verificações básicas de funcionamento

---

## 📝 Anotações Técnicas

- **Importante:** Sempre verifique as regiões disponíveis e os custos antes de criar recursos!
- Use o grupo de recursos para organizar tudo relacionado à VM.
- Lembre-se de revisar as políticas de segurança para portas abertas como RDP (porta 3389).
- Exclua recursos após o uso para evitar cobrança indevida.

---

## 📚 Recursos Úteis

- [Criar uma VM no Azure (Microsoft Learn)](https://learn.microsoft.com/pt-br/azure/virtual-machines/windows/quick-create-portal)
- [GitHub Markdown Guide](https://www.markdownguide.org/basic-syntax/)
- [GitBook - Formação GitHub Certification](https://app.gitbook.com/o/-MqNYsZ0tk5CEzRx2QZl/s/github)
- [Documentação oficial do GitHub](https://docs.github.com/)

---
## 📌 Etapas Realizadas

1. **Acesse o portal do Azure**  
   - Vá para [https://portal.azure.com](https://portal.azure.com) e faça login com sua conta Microsoft.

2. **Crie uma nova máquina virtual**  
   - No menu lateral ou na barra de pesquisa, digite **"Máquinas virtuais"**.  
   - Clique em **Criar** > **Máquina Virtual**.

3. **Configure as informações básicas**  
   - **Assinatura**: selecione sua assinatura ativa.  
   - **Grupo de recursos**: crie um novo ou selecione um existente.  
   - **Nome da máquina virtual**: ex. `vm-windows-teste`.  
   - **Região**: escolha a mais próxima ou com suporte gratuito.  
   - **Imagem**: selecione **Windows Server 2019 Datacenter**.  
   - **Tamanho**: selecione um plano como o `B1s` (elegível para uso gratuito).  
   - **Autenticação**: escolha **Senha** e defina um **nome de usuário** e **senha**.

4. **Configuração de portas de entrada**  
   - Permita a **porta 3389 (RDP)** para acesso remoto à VM via Área de Trabalho Remota.

5. **Revise e crie a VM**  
   - Clique em **Revisar + Criar**, verifique os dados e então clique em **Criar**.  
   - Aguarde a finalização da implantação (pode levar alguns minutos).

6. **Acesse a VM criada**  
   - Após criada, vá até a página da VM e clique em **Conectar** > **Área de Trabalho Remota**.  
   - Baixe o arquivo `.rdp`, abra-o e insira as credenciais criadas.

7. **Testes e encerramento**  
   - Confirme que você acessou a VM com sucesso.  
   - Faça os testes necessários (instalação de apps, comandos etc.).  
   - Ao final, **exclua a máquina virtual e o grupo de recursos** para evitar cobranças futuras.


---


## 🚀 Conclusão

Este repositório representa minha jornada prática com o Azure e o GitHub. Foi uma excelente oportunidade para aplicar os conceitos em um ambiente real, compreender melhor a computação em nuvem e aprimorar minhas habilidades com versionamento e documentação técnica.

---

📨 **Autor:** [Mateus Ribeiro](https://github.com/mateusribeiros)


