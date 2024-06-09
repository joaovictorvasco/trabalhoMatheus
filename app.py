import streamlit as st
import pandas as pd
from xgboost import XGBRegressor
import numpy as np
import os

main_body_logo = "fortune.png"
sidebar_logo = "fortune.png"
background_color = "#0a1931"

# Para exibir um logo na barra lateral, primeiro, chamamos st.sidebar para operações na barra lateral
st.sidebar.image(sidebar_logo, width=250)  # Ajuste a largura conforme necessário

# Criando a barra superior
# Verificando se o arquivo existe
if os.path.exists(main_body_logo):
    st.markdown(f"""
        <div style="background-color:{background_color}; padding:20px; border-radius:20px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); display: flex; justify-content: center; align-items: center;">
            <h1 style="color:white; font-size: 40px; text-align:center; margin: 0;">
                <img src="{main_body_logo}" alt="logo" style="height:60px; vertical-align: middle; margin-right: 10px;">
                Fortune Card
            </h1>
        </div>
    """, unsafe_allow_html=True)
else:
    st.error("O arquivo do logo não foi encontrado. Verifique o caminho!")



# Conteúdo principal
st.write("""
    # Nosso app serve para prever estatisticamente o número de cartões numa determinada partida
""")

# Criando abas
tab1, tab2 = st.tabs(["Jogos", "Tabela"])

# Conteúdo para a aba "Jogos"
with tab1:
    times = ['Ath Paranaense', 'Atl Goianiense', 'Atlético Mineiro', 'Bahia', 'Botafogo (RJ)', 
             'Corinthians', 'Criciúma', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 
             'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Palmeiras', 
             'Red Bull Bragantino', 'São Paulo', 'Vasco da Gama', 'Vitória']
    
    # Ordenando a lista de times
    times_ordenados = sorted(times)
    
    with st.form(key='form'):
        op_home = st.selectbox('Escolha uma opção p/ time da casa', times_ordenados)
        op_away = st.selectbox('Escolha outra opção p/ time visitante', times_ordenados)
        enviar = st.form_submit_button('Enviar')
    
    if enviar:
        if op_home == op_away:
            st.error('Erro: O mesmo time não pode ser escolhido como time da casa e visitante.')
        else:
            lista = [{'Home': op_home, 'Away': op_away, 'ano_x': 2024}]
            df = pd.DataFrame(lista)
            df['Home'] = df['Home'].astype('category')
            df['Away'] = df['Away'].astype('category')
            model = XGBRegressor()
            model.load_model('modelo.json') 
            resultado = model.predict(df)
            st.metric('Nº de cartões predito', int(np.round(resultado[0], 0)))

# Conteúdo para a aba "Tabela"
with tab2:
    st.write("Conteúdo da Tabela aqui.")

