import pandas as pd
import cx_Oracle
import streamlit as st
import matplotlib.pyplot as plt
from langchain_community.llms import Ollama
import numpy as np


# Configurações de conexão
connection_info = {
    "user": "rm551365",
    "password": "191097",
    "dsn": "oracle.fiap.com.br/orcl"
}

# Função para buscar os dados do banco de dados
def get_data_from_db(query):
    try:
        with cx_Oracle.connect(**connection_info) as connection:
            df = pd.read_sql(query, connection)
        return df
    except cx_Oracle.DatabaseError as e:
        st.error(f"Erro ao buscar dados do banco de dados: {e}")
        return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro


# Função para buscar o fluxo de dados atual
def get_current_flow_data():
    query = """
    SELECT pr.NOME_PROCESSO AS STEP, 
               pr.TIMESTAMP AS DURATION_SECONDS, 
               COUNT(iu.INTERUSERID) AS CLICKS 
        FROM IW_PROCESSOREAL pr 
        JOIN IW_INTERUSER iu ON pr.IW_INTERUSER_INTERUSERID = iu.INTERUSERID 
        GROUP BY pr.NOME_PROCESSO, pr.TIMESTAMP


    """
    return get_data_from_db(query)

# Função para buscar o fluxo de dados de referência
def get_reference_flow_data():
    query = """
    SELECT 
        pi.LOCAL_CLIQUE AS STEP, 
        pi.TEMPO_ESTIMADO AS DURATION_SECONDS, 
        0 AS CLICKS
    FROM 
        IW_PASSOIDEAL pi

    """
    return get_data_from_db(query)

# Função para converter os dados em texto legível para o Ollama
def format_data_for_ollama(df_current, df_reference):
    insights_text = "Comparação de Interações do Usuário:\n\n"

    for i, row in df_current.iterrows():
        ref_row = df_reference.iloc[i] if i < len(df_reference) else None
        insights_text += f"Etapa: {row['STEP']} \nDuração: {row['DURATION_SECONDS']}s \nCliques: {row['CLICKS']}\n"
        if ref_row is not None:
            insights_text += f"Referência - Duração: {ref_row['DURATION_SECONDS']}s, Cliques: {ref_row['CLICKS']}\n"
        else:
            insights_text += "Não há referência disponível.\n"
        insights_text += "\n"

    return insights_text

# Função para gerar insights detalhados usando o modelo Ollama
def generate_detailed_insights(df_current, df_reference):
    model = Ollama(model="costumized_ollama_llama3")  # Configura o modelo que você está usando
    
    # Formata os dados dos DataFrames em texto
    current_data_text = df_current.to_string(index=False)
    reference_data_text = df_reference.to_string(index=False)

    # Prompt personalizado para análise detalhada
    prompt = (
        "Analise os dados de fluxo de referência e o fluxo atual fornecidos. "
        "Identifique discrepâncias, forneça insights e sugira melhorias.\n\n"
        "Dados de Referência:\n"
        f"{reference_data_text}\n\n"
        "Dados Atuais:\n"
        f"{current_data_text}\n"
        "Forneça uma análise detalhada e insights acionáveis em português."
    )

    # Chama o modelo Ollama com o prompt formatado
    response = model.invoke(prompt)
    return response.strip()

def convert_to_seconds(series):
    # Verifica o tipo de dados e converte para segundos
    if pd.api.types.is_timedelta64_dtype(series):
        # Caso já seja timedelta, converte diretamente para segundos
        return series / pd.Timedelta(seconds=1)
    elif pd.api.types.is_datetime64_any_dtype(series):
        # Caso seja datetime, subtrai a origem Epoch para obter segundos
        return (series - pd.Timestamp("1970-01-01")) / pd.Timedelta(seconds=1)
    else:
        # Assume que já está em segundos (float ou int)
        return series.astype(float)
    
# Função para comparar os dados do banco
def compare_db_data():
    df_current = get_current_flow_data()
    df_reference = get_reference_flow_data()

    # Converte DURATION_SECONDS para segundos em ambos os DataFrames
    df_current['DURATION_SECONDS'] = convert_to_seconds(df_current['DURATION_SECONDS'])
    df_reference['DURATION_SECONDS'] = convert_to_seconds(df_reference['DURATION_SECONDS'])



    # Exibir DataFrames para verificação
    st.subheader('Fluxo de Dados Atual')
    st.dataframe(df_current)
    st.subheader('Fluxo de Dados de Referência')
    st.dataframe(df_reference)

    insights = []

    # Verificar diferenças no número de etapas
    if len(df_current) != len(df_reference):
        insights.append(f"Número de etapas diferentes: {len(df_current)} no fluxo atual, {len(df_reference)} no de referência.")

    # Comparar cada etapa
    for i, row in df_current.iterrows():
        if i < len(df_reference):
            ref_row = df_reference.iloc[i]

            if row['DURATION_SECONDS'] > ref_row['DURATION_SECONDS']:
                insights.append(f"Usuário gastou {row['DURATION_SECONDS']}s em '{row['STEP']}', mais que o tempo de referência de {ref_row['DURATION_SECONDS']}s.")
            elif row['DURATION_SECONDS'] < ref_row['duration_seconds']:
                insights.append(f"Usuário gastou {row['DURATION_SECONDS']}s em '{row['STEP']}', menos que o tempo de referência de {ref_row['DURATION_SECONDS']}s.")

            if row['CLICKS'] != ref_row['CLICKS'] and ref_row['CLICKS'] > 0:
                insights.append(f"Usuário clicou {row['CLICKS']} vezes, diferente dos {ref_row['CLICKS']} esperados.")
        else:
            insights.append(f"Não há etapa correspondente no fluxo de referência.")
    
    return insights, df_current, df_reference

# Função para armazenar insights gerados no banco de dados
def save_insights_to_db(df_current, df_reference, insights_text):
    try:
        with cx_Oracle.connect(**connection_info) as connection:
            cursor = connection.cursor()
            # Inserção dos insights gerados
            for i, row in df_current.iterrows():
                ref_row = df_reference.iloc[i] if i < len(df_reference) else None

                # Converte valores numpy para tipos Python nativos
                duration_seconds = row['DURATION_SECONDS'].item() if isinstance(row['DURATION_SECONDS'], (np.integer, np.floating)) else row['DURATION_SECONDS']
                clicks = row['CLICKS'].item() if isinstance(row['CLICKS'], (np.integer, np.floating)) else row['CLICKS']
                ref_duration_seconds = ref_row['DURATION_SECONDS'].item() if ref_row is not None and isinstance(ref_row['DURATION_SECONDS'], (np.integer, np.floating)) else None
                ref_clicks = ref_row['CLICKS'].item() if ref_row is not None and isinstance(ref_row['CLICKS'], (np.integer, np.floating)) else None

                # Inserir cada insight
                cursor.execute("""
                    INSERT INTO INSIGHTS (
                        STEP, DURATION_SECONDS, CLICKS,
                        REFERENCE_DURATION_SECONDS, REFERENCE_CLICKS, INSIGHT_TEXT
                    ) VALUES (:step, :duration_seconds, :clicks,
                              :ref_duration_seconds, :ref_clicks, :insight_text)
                """, {
                    "step": row['STEP'],
                    "duration_seconds": duration_seconds,
                    "clicks": clicks,
                    "ref_duration_seconds": ref_duration_seconds,
                    "ref_clicks": ref_clicks,
                    "insight_text": insights_text
                })
            
            # Confirma as inserções
            connection.commit()
            st.success("Insights armazenados no banco de dados com sucesso!")
    except cx_Oracle.DatabaseError as e:
        st.error(f"Erro ao salvar insights no banco de dados: {e}")


# Interface do Streamlit
st.title('Dashboard de Comparação de Interações')
st.write('Comparação entre fluxo de referência e fluxo atual.')

# Gerar insights com dados do banco
insights, df_current, df_reference = compare_db_data()

# Exibir insights
st.subheader('Insights Gerados')
for insight in insights:
    st.write(f"- {insight}")

# Gerar insights detalhados
detailed_insights = generate_detailed_insights(df_current, df_reference)

# Exibir insights do Ollama
st.subheader('Insights Gerados pelo Ollama')
st.write(detailed_insights)

# Chamando a função para armazenar os dados na tabela
save_insights_to_db(df_current, df_reference, detailed_insights)