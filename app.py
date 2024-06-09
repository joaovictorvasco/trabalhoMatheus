import streamlit as st
import pandas as pd
from xgboost import XGBRegressor
import numpy as np
import os

sidebar_logo = "fortune.png"
main_logo = "logo_horizontal.jpg"
background_color = "#0a1931"

# Sidebar logo display
st.sidebar.image(sidebar_logo, width=250)

# Main logo display, centered
st.image(main_logo, width=700, use_column_width=True)

# Creating a colored top bar
st.markdown(f"""
    <div style="background-color:{background_color}; padding:15px; border-radius:10px; box-shadow: 0 16px 8px 0 rgba(0, 0, 0, 0.2);">
        <h1 style="color:white; font-size:50px; text-align:center;">Fortune Card</h1>
    </div>
""", unsafe_allow_html=True)

# Main content
st.write("""
    # Nosso app serve para prever estatisticamente o número de cartões numa determinada partida
""")

# Tabs for content
tab1, tab2 = st.tabs(["Jogos", "Tabela"])

# Tab content
with tab1:
    times = ['Ath Paranaense', 'Atl Goianiense', 'Atlético Mineiro', 'Bahia', 'Botafogo (RJ)', 
             'Corinthians', 'Criciúma', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 
             'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Palmeiras', 
             'Red Bull Bragantino', 'São Paulo', 'Vasco da


