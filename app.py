import streamlit as st
# Criando a barra superior
st.write("""
    <div style="background-color:#f63366;padding:10px;border-radius:200px;">
        <h1 style="color:white;text-align:center;">Fortune Card</h1>
    </div>
""", unsafe_allow_html=True)

# Conteúdo principal
st.write("""
    # Conteúdo Principal
    Este é o conteúdo principal da página.
""")

st.title('Fortune Card')

st.write('Nosso app serve para prever estatisticamente o número de cartões numa determinada partida')
tab_jogos, tab_juizes, tab_times = st.tabs(['Jogos', 'Juizes', 'Times'])

