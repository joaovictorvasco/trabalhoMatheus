import streamlit as st
# Criando a barra superior
st.write("""
    <div style="background-color:#f63366;padding:10px;border-radius:200px;">
        <h1 style="color:white;text-align:center;">Fortune Card</h1>
    </div>
""", unsafe_allow_html=True)

# Conteúdo principal
st.write("""
    # Nosso app serve para prever estatisticamente o número de cartões numa determinada partida
""")

tab_jogos = st.tabs(['Jogos'])

times = ['Ath Paranaense', 'Atl Goianiense', 'Atlético Mineiro', 'Bahia', 'Botafogo (RJ)', 
         'Corinthians', 'Criciúma', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 
         'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Palmeiras', 
         'Red Bull Bragantino', 'São Paulo', 'Vasco da Gama', 'Vitória']

# Ordenando a lista de times
times_ordenados = sorted(times)

op_home = st.selectbox('Escolha uma opção p/ time da casa', times_ordenados)
op_away = st.selectbox('Escolha outra opção p/ time visitante', times_ordenados)


