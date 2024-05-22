import streamlit as st
st.title('Fortune Card')

with st.sidebar:
  st.header('Fortune Card')
  st.write('Seu aplicativo de cartões')
  st.caption('Criado por Gabriel, João Victor e Pedro Henrique')

st.write('Nosso app serve para prever estatisticamente o número de cartões numa determinada partida')
tab_juizes, tab_times = st.tabs(['Juizes', 'Times'])
