# 📒 Notas e Dicas sobre o Azure

## ☁️ Azure - Visão Geral
Azure é a plataforma de computação em nuvem da Microsoft, oferecendo serviços como:
- Máquinas Virtuais (VMs)
- Banco de Dados (SQL, Cosmos DB)
- Armazenamento em Nuvem
- Kubernetes (AKS)
- Redes Virtuais

## 💻 Criação de VM - Pontos Chave
- Ao criar a VM, escolha regiões com suporte e gratuidade (como "Leste dos EUA").
- Tamanho B1s é ideal para testes (baixa performance, mas gratuito).
- Configurar o disco OS padrão (geralmente SSD) e manter a rede padrão para início.
- Habilite a RDP (porta 3389) para VMs Windows; SSH (porta 22) para Linux.

## 🛡 Segurança
- Após terminar os testes, exclua a VM e o grupo de recursos.
- Use nomes de usuário fortes e senhas complexas.
- Se possível, restrinja o IP de acesso ao RDP para seu IP público.

## 🧠 Dica Extra
Use o Azure Resource Manager (ARM) para automatizar a criação de recursos no futuro com templates!

