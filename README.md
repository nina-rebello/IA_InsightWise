![Logo Preto](https://i.imgur.com/LyQ6ygf.png)

# InsightWise - Interaction Flow Comparison

This project compares user interaction flows between reference data and real data, generating actionable insights from detected discrepancies.

- **Graphical Interface**: Using `Streamlit`, we created an interactive dashboard that displays comparative bar charts, pie charts, scatter plots, and detailed tables, making it easier to visually analyze differences between flows.
- **AI Model (Ollama - Llama)**: Integration with the Llama model via Ollama provides more complex interpretive insights, helping to understand discrepancies and interaction improvements.
- **Database**: The generated insights are stored in a dedicated table in the Oracle database, enabling future queries. The project uses Oracle SQL Developer for database management and the `cx_Oracle` package to connect with Python.
- **Data Analysis**: With `Pandas` and `Matplotlib`, interaction data (such as time spent and number of clicks) is processed, compared, and visualized, offering a comprehensive and detailed view of interaction flow performance.

InsightWise transforms interaction data into valuable information for optimizing user experience.

## Features

- **Insight Generation:** Compares current interaction flow data with a reference flow and generates insights about detected discrepancies, such as differences in time and number of clicks at each step.
- **Data Visualization:** Displays visual graphs to facilitate the interpretation of differences between the reference flow and the current flow.
  - Comparative bar charts
  - Pie charts showing time distribution
  - Scatter plots showing the relationship between the number of clicks and time spent
  - Detailed comparative tables
- **Temporal and Click Analysis:** Provides visual and textual analysis of time spent and clicks at each step of the interaction flow.
- **AI Model (Llama):** Integration with the Llama AI model to provide more detailed and complex verbal insights.
- **Storage of Insights in Database:** Stores generated insights directly in a dedicated table in the Oracle database, allowing for future queries and backend access for display in various frontend components.

## Technologies Used

- **Python 3.x**
- **Streamlit**
- **Pandas** for data manipulation
- **Matplotlib** for graph visualization
- **Langchain** and **Ollama** for generating detailed insights through AI
- **Oracle SQL Developer**

# Presentation Videos

- [Java Application](https://www.youtube.com/watch?v=SWA94V1H_Y0)
- [Mobile Version](https://youtu.be/B6ZZIZmo8L0)
- [Reflection and Final Product](https://youtu.be/W4cTeR_WAZM)
  
# Repositories

- [Introduction](https://github.com/nina-rebello/InsightWise.git)
- [AI Application](https://github.com/nina-rebello/IA_InsightWise.git)
- [Backend](https://github.com/Santlago/apiinsightwise.git)
- [Frontend](https://github.com/Santlago/insightwise.git)
- [Mobile](https://github.com/FelipeGuedesGoncalves/InsightWiseMobile)
  
## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository

# Create a virtual environment:
```bash
  python -m venv env
```

# Activate the virtual environment:
### On Windows:
```bash
  .\env\Scripts\activate
```

### On Linux/MacOS:
```bash
  source env/bin/activate
```

# Install the dependencies:
```bash
  pip install -r requirements.txt
```

# Run the project with Streamlit:
```bash
streamlit run ia_InsightWise_bd.py
```

The interface will automatically open in your browser. Explore the generated insights, graphs, and comparisons directly through the interface.

## Project Structure

```plaintext
├── ia_InsightWise_bd.py          # Main application script
├── costumized_ollama.txt         # Script for customizing a model in Ollama
└── README.md                     # Project documentation
```


## Example of Use

### Generated Insights
From the comparison of flows, the system generates insights such as:

- "User spent more time on the 'Fill in personal data' step compared to the reference time."
- "The number of clicks on 'Complete registration' was higher than expected."


# Português

 # InsightWise - Comparação de Fluxos de Interação

Este projeto compara fluxos de interação de usuários entre dados de referência e dados reais, gerando insights acionáveis a partir de discrepâncias encontradas.

- **Interface Gráfica**: Utilizando `Streamlit`, criamos um dashboard interativo que exibe gráficos de barras comparativos, gráficos de pizza, gráficos de dispersão e tabelas detalhadas, facilitando a análise visual das diferenças entre os fluxos.
- **Modelo de IA (Ollama - Llama)**: Integração com o modelo Llama via Ollama para fornecer insights interpretativos mais complexos, auxiliando na compreensão das discrepâncias e melhorias de interação.
- **Banco de Dados**: Os insights gerados são armazenados em uma tabela dedicada no banco de dados Oracle, permitindo consultas futuras. O projeto utiliza Oracle SQL Developer para gerenciar o banco e o pacote `cx_Oracle` para conectar com Python.
- **Análise de Dados**: Com o uso de `Pandas` e `Matplotlib`, os dados de interação (como tempo gasto e número de cliques) são processados, comparados e visualizados, fornecendo uma visão ampla e detalhada sobre o desempenho do fluxo de interação.

InsightWise transforma dados de interação em informações valiosas para otimizar a experiência do usuário.

## Funcionalidades

- **Geração de Insights:** Compara os dados atuais de fluxo de interação com um fluxo de referência e gera insights sobre as discrepâncias encontradas, como diferenças de tempo e número de cliques em cada etapa.
- **Visualização de Dados:** Exibe gráficos visuais para facilitar a interpretação das diferenças entre o fluxo de referência e o fluxo atual.
  - Gráficos de barras comparativos
  - Gráficos de pizza mostrando a distribuição de tempo
  - Gráficos de dispersão mostrando a relação entre o número de cliques e o tempo gasto
  - Tabelas comparativas detalhadas
- **Análise Temporal e de Cliques:** Fornece uma análise visual e textual do tempo gasto e dos cliques em cada etapa do fluxo de interação.
- **Modelo de IA (Llama):** Integração com o modelo de IA Llama para fornecer insights verbais mais detalhados e complexos.
- **Armazenamento de Insights no Banco de Dados:** Armazena os insights gerados diretamente em uma tabela dedicada no banco de dados Oracle, permitindo consulta posterior e acesso pelo backend para exibição em diferentes componentes de frontend.

## Tecnologias Utilizadas

- **Python 3.x**
- **Streamlit**
- **Pandas** para manipulação de dados
- **Matplotlib** para visualização de gráficos
- **Langchain** e **Ollama** para geração de insights detalhados através de IA
- **SQL Oralce Developer**


## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

Aqui está o texto formatado em Markdown para você copiar e colar no README do GitHub:

# Crie um ambiente virtual:

```bash
python -m venv env
```

## Ative o ambiente virtual:

### No Windows:
```bash
.\env\Scripts\activate
```

### No Linux/MacOS:
```bash
source env/bin/activate
```

## Instale as dependências:

```bash
pip install -r requirements.txt
```

### Execute o projeto com Streamlit:

```bash
streamlit run streamlit.py
```

A interface será aberta automaticamente no seu navegador. Explore os insights gerados, gráficos e comparações diretamente pela interface.

## Estrutura do Projeto

```plaintext
├── ia_InsightWise_bd.py          # Script principal da aplicação
├── costumized_ollama.txt         # Script para costumização de um modelo no ollama
└── README.md                     # Documentação do projeto
```

## Exemplo de Uso

### Insights Gerados

A partir da comparação dos fluxos, o sistema gera insights como:

- "Usuário gastou mais tempo na etapa 'Preencher dados pessoais' em comparação ao tempo de referência."
- "Número de cliques em 'Finalizar cadastro' foi maior do que o esperado."


