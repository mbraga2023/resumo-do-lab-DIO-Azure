
## ☁️ **Características Básicas da Azure Cloud**

---

### ⚖️ **Elasticidade**
- A capacidade de **aumentar ou reduzir recursos automaticamente** conforme a demanda.
- Exemplo: seu site recebe muitos acessos em horários de pico → Azure ajusta os recursos para manter o desempenho.

---

### 📈 **Escalabilidade**
- Azure permite **escalar verticalmente** (aumentar recursos de uma máquina) ou **horizontalmente** (adicionar mais máquinas).
- É possível fazer isso **manual ou automaticamente** (Auto Scale).

---

### 🔄 **Alta Disponibilidade (High Availability)**
- Serviços são projetados para ficarem **sempre acessíveis**, mesmo em caso de falhas.
- Redundância e replicação geográfica garantem continuidade do serviço.

---

### 🕒 **SLA (Service Level Agreement)**
- Acordos de nível de serviço com **garantias de disponibilidade**, geralmente:
  - 99,9% (1 região)
  - 99,99% (com redundância entre zonas)
- Define o quanto o serviço pode ficar fora do ar sem penalização.

---

### 🔐 **Segurança**
- Criptografia de dados **em repouso e em trânsito**.
- Autenticação multifator, firewalls, rede virtual isolada, RBAC (controle de acesso baseado em função).
- Serviços como **Azure Security Center** e **Microsoft Defender for Cloud**.

---

### 🗺️ **Zonas de Disponibilidade**
- São **localizações físicas distintas** dentro de uma região (data centers separados).
- Garantem resiliência contra falhas locais (energia, rede, hardware).

---

### 🧩 **Modelos de Nuvem**

#### ☁️ Nuvem Pública
- Infraestrutura compartilhada entre clientes (multi-tenant).
- Alta escalabilidade e custo mais baixo.

#### 🏢 Nuvem Privada
- Infraestrutura dedicada, mais controle e segurança.
- Pode ser local ou hospedada por terceiros.

#### 🌐 Nuvem Híbrida
- Combinação entre pública e privada.
- Exemplo: dados sensíveis ficam na privada, aplicações na pública.

---

### 💰 **Custos**
- Modelo **pay-as-you-go**: paga pelo que usa.
- Também há **reservas e planos com desconto** para uso contínuo.
- Ferramentas de gerenciamento de custos: **Azure Cost Management**.

---

### 📜 **Governança**
- Conjunto de políticas e regras para garantir o **uso adequado e seguro** dos recursos em nuvem.
- Ferramentas:
  - **Azure Policy** – cria regras de conformidade.
  - **Azure Blueprints** – modelos de governança e compliance.
  - **RBAC** – controle de permissões.

---

### 🛠️ **Outras Características Importantes**

| Característica | Descrição |
|----------------|-----------|
| **Resiliência** | Capacidade de se recuperar de falhas rapidamente. |
| **Monitoramento** | Ferramentas como Azure Monitor e Log Analytics para visibilidade completa. |
| **Automação** | Scripts, runbooks e pipelines para automatizar tarefas (Azure Automation, DevOps). |
| **Compliance** | Atende a centenas de normas: ISO, SOC, GDPR, LGPD etc. |

---

- **IaaS (Infrastructure as a Service)**:  
  Fornece infraestrutura de TI básica como servidores, redes, armazenamento e máquinas virtuais. Você gerencia o sistema operacional, aplicativos e dados.  
  👉 *Exemplo:* Amazon EC2, Microsoft Azure VM.

- **PaaS (Platform as a Service)**:  
  Oferece uma plataforma pronta para desenvolvimento, onde você só se preocupa com o código. A infraestrutura e o sistema operacional são gerenciados pelo provedor.  
  👉 *Exemplo:* Google App Engine, Heroku.

- **SaaS (Software as a Service)**:  
  É o software pronto para uso, acessado via internet. O provedor cuida de tudo.  
  👉 *Exemplo:* Gmail, Microsoft 365, Dropbox.

Beleza! Aqui vai uma **tabela comparativa** com um pouco mais de detalhe, mas ainda de forma clara:

| **Modelo** | **O que é?** | **Responsável pelo quê?** | **Exemplos** |
|------------|--------------|----------------------------|--------------|
| **IaaS** (Infrastructure as a Service) | Infraestrutura de TI na nuvem. Recursos como servidores, redes e armazenamento são fornecidos sob demanda. | Você gerencia: sistema operacional, aplicativos, dados. <br>Provedor gerencia: hardware, rede, virtualização. | Amazon EC2, Microsoft Azure VM, Google Compute Engine |
| **PaaS** (Platform as a Service) | Plataforma para desenvolvimento e hospedagem de aplicações. Ideal para desenvolvedores. | Você gerencia: código da aplicação, dados. <br>Provedor gerencia: infraestrutura, sistema operacional, runtime. | Google App Engine, Heroku, Microsoft Azure App Services |
| **SaaS** (Software as a Service) | Software pronto para uso, via navegador ou app. Nenhuma preocupação com infraestrutura ou instalação. | Provedor gerencia tudo: infraestrutura, aplicação, dados (em parte). <br>Usuário apenas utiliza. | Gmail, Dropbox, Salesforce, Microsoft 365 |

