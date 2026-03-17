# 👕 Sistema de Gerenciamento de Pedidos e Estoque

Este sistema é uma solução Desktop desenvolvida em Python para automatizar o controle de estoque e o registro de pedidos de uniformes/camisas. O projeto foi criado para resolver gargalos operacionais, substituindo controles manuais por um fluxo digital eficiente.

## 🚀 Funcionalidades

- **Gestão de Estoque:** Atualização e consulta de quantidades por gênero (Masculino/Feminino) e tamanho (PP ao XGG).
- **Registro de Pedidos:** Cadastro completo de novos pedidos, incluindo validação de data, quantidade e status de termo assinado.
- **Tabelas Dinâmicas:** Visualização de dados processados em Treeviews com suporte a scroll infinito.
- **Arquitetura Modular:** Separação entre componentes de interface e serviços de manipulação de dados.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** [Python 3.x](https://www.python.org/)
- **GUI:** [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) (Interface moderna)
- **Manipulação de Dados:** [Pandas](https://pandas.pydata.org/) (Integração com Excel)
- **Utilitários:** TkCalendar (Seleção de datas) e OpenPyXL (Motor de Excel).

## 📂 Estrutura do Projeto

```text
├── Arts/               # Ícones e recursos visuais
├── Builder/            # Lógica de construção da app (Constructor.py)
├── Interface/          # Arquivos de UI (Frontend, Estoque, Pedidos)
├── Planilhas/          # Base de dados em Excel
├── Services/           # Lógica de negócio e manipulação de arquivos
└── Main.py             # Ponto de entrada da aplicação

🔧 Como Executar
pip install -r requirements.txt
Inicie a aplicação:

Bash
python Main.py
📈 Aprendizados
O desenvolvimento focou em Clean Code e nos princípios SOLID, especialmente na Responsabilidade Única (SRP), garantindo que a lógica de leitura de planilhas nunca se misture com a lógica de renderização da interface.


---

### 3. requirements.txt

Este arquivo contém todas as bibliotecas que seu código importa (Pandas, CustomTkinter, tkcalendar, etc.).

```text
customtkinter
pandas
openpyxl
tkcalendar
babel
