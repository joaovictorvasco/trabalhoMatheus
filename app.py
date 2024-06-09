import streamlit as st
import pandas as pd
from xgboost import XGBRegressor
import numpy as np

# Inicializando o estado da sessão para controlar a visibilidade da resposta
if 'show_result' not in st.session_state:
    st.session_state.show_result = False

sidebar_logo = "fortune.png"
main_logo = "logo_horizontal.jpg"
background_color = "#0a1931"

# Sidebar logo display
st.sidebar.image(sidebar_logo, width=250)
st.sidebar.markdown("""
    <div style="font-size: 20px;"><strong>Aplicativo desenvolvido por:</strong></div>
    <ul style="font-size: 18px; margin-left: 20px;">
        <li>Gabriel Novais</li>
        <li>João Victor Sepulveda</li>
        <li>Pedro Henrique Lapa</li>
    </ul>
""", unsafe_allow_html=True)

# Main logo display, centered
st.image(main_logo, width=700, use_column_width=True)

# Creating a colored top bar
st.markdown(f"""
    <div style="background-color:{background_color}; padding:15px; border-radius:10px; box-shadow: 0 16px 8px 0 rgba(0, 0, 0, 0.2);">
        <h1 style="color:yellow; font-size:50px; text-align:center;">Fortune Card</h1>
    </div>
""", unsafe_allow_html=True)

# Main content
st.markdown("""
    <h2 style="font-size:28px;">Nosso aplicativo utiliza um modelo estatístico para prever o número de cartões em uma determinada partida do Campeonato Brasileiro de 2024.</h2>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Jogos", "Tabela"])

with tab1:
    times = ['Ath Paranaense', 'Atl Goianiense', 'Atlético Mineiro', 'Bahia', 'Botafogo (RJ)', 
             'Corinthians', 'Criciúma', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 
             'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Palmeiras', 
             'Red Bull Bragantino', 'São Paulo', 'Vasco da Gama', 'Vitória']
    times_ordenados = sorted(times)
    
    with st.form(key='prediction_form'):
        op_home = st.selectbox('Escolha uma opção para o time da casa', times_ordenados)
        op_away = st.selectbox('Escolha outra opção para o time visitante', times_ordenados)
        enviar = st.form_submit_button('Enviar')
        
        if enviar:
            if op_home == op_away:
                st.error('Erro: O mesmo time não pode ser escolhido como time da casa e visitante.')
            else:
                st.session_state.show_result = True
                lista = [{'Home': op_home, 'Away': op_away, 'ano_x': 2024}]
                df = pd.DataFrame(lista)
                df['Home'] = df['Home'].astype('category')
                df['Away'] = df['Away'].astype('category')
                model = XGBRegressor()
                model.load_model('modelo.json')
                ypred = model.predict(df)
                
                r2 = -0.0608767415057232
                mae = 2.1616382956885682
                mse = 7.511824680006472

                st.markdown(f"""
                    ### Previsão de Cartões para a Partida
                    **Confronto:** {op_home} vs {op_away}
                    **Previsão de Cartões Total:** {int(np.round(ypred[0], 0))}

                    **Precisão do Modelo:**
                    - \( R^2 \): {r2:.2f} (Um valor negativo indica que o modelo não tem poder preditivo adequado.)
                    - Erro Absoluto Médio (MAE): {mae:.2f}
                    - Erro Quadrático Médio (MSE): {mse:.2f}

                    **Considerações para Apostas:**
                    Dada a baixa confiabilidade das previsões deste modelo, recomendamos cautela ao usar estas informações para suas decisões. Esses números devem ser vistos como estimativas, e é crucial considerar outras fontes e fatores ao tomar decisões baseadas nessas previsões.
                """, unsafe_allow_html=True)

with tab2:
    st.write("Conteúdo da Tabela aqui.")

# Resetar o estado ao mudar de aba
def on_tab_change():
    st.session_state.show_result = False
