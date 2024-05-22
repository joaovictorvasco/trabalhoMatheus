import streamlit as st
st.title('Fortune Card')

with st.sidebar:
  st.header('Vasco')
  st.write('Seu aplicativo')
  st.caption('Criado por')

st.write('Nosso app serve para prever estatisticamente o número de cartões numa determinada partida')
tab_juizes, tab_times = st.tabs(['Juizes', 'Times'])
