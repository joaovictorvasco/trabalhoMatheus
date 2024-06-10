import openpyxl
import lxml
import streamlit as st
import pandas as pd
from xgboost import XGBRegressor
import numpy as np
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

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

# Main content
st.markdown("""
    <h2 style="font-size:28px;">Nosso aplicativo utiliza um modelo estatístico para prever o número de cartões em uma determinada partida do Campeonato Brasileiro de 2024.</h2>
""", unsafe_allow_html=True)
st.markdown("""
    <h2 style="font-size:18px;">Este modelo analisa dados históricos de confrontos entre times, incluindo estatísticas de jogos anteriores, para calcular a probabilidade de cartões amarelos e vermelhos serem dados durante uma partida. Abaixo, selecione os times da casa e visitante e nosso modelo usará esses dados para prever o resultado provável em termos de cartões.</h2>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Jogos", "Tabela", "Calendário"])

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
    st.write("### Tabela do Brasileirão 2024")
    
    # Adicionar CSS para ajustar a largura da tabela
    st.markdown(
        """
        <style>
        .stDataFrame {
            display: flex;
            flex-direction: column;
            width: 100%;
        }
        .stDataFrame > div {
            width: 100% !important;
        }
        .stDataFrame table {
            width: 100% !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Raspar a tabela do Brasileirão do site fbref
    url = "https://fbref.com/en/comps/24/Serie-A-Stats"
    response = requests.get(url)
    time.sleep(5)  # Pausa de 5 segundos entre as requisições
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrar a tabela com o ID específico
    tabela_html = soup.find('table', {'id': 'results2024241_overall'})

    # Ler a tabela HTML com pandas
    if tabela_html:
        tabela_df = pd.read_html(str(tabela_html))[0]
        
        # Remover as colunas indesejadas
        cols_to_drop = ['Attendance', 'Top Team Scorer', 'Goalkeeper', 'Notes', 'Pts/MP', 'xG', 'xGA', 'xGD', 'xGD/90']
        tabela_df = tabela_df.drop(columns=cols_to_drop)

        # Renomear as colunas conforme solicitado
        tabela_df = tabela_df.rename(columns={
            'MP': 'Partidas',
            'W': 'V',
            'D': 'E',
            'L': 'D',
            'GF': 'Gols Pró',
            'GA': 'Gols Sofridos',
            'GD': 'Saldo de Gols',
            'Pts': 'Pontos',
            'Last 5': 'Desempenho',
            'Squad': 'Time',
            'Rk': 'Classificação'
        })

        # Remover o índice
        tabela_df = tabela_df.set_index('Classificação')
        
        # Reordenar as colunas para que 'Time' e 'Pontos' sejam as primeiras
        cols = ['Time', 'Pontos'] + [col for col in tabela_df.columns if col not in ['Time', 'Pontos']]
        tabela_df = tabela_df[cols]
        
        # Ajustar o estilo da tabela para ocupar mais espaço
        st.dataframe(tabela_df, height=750, use_container_width=True)  # Ajuste a altura e largura conforme necessário
    else:
        st.write("Tabela não encontrada.")

with tab3:
    st.write("### Próximos 5 Jogos do Time")
    
    # Selecionar o time
    time_selecionado = st.selectbox('Escolha um time', times_ordenados)
    
    if time_selecionado:
        
            fixtures_df = pd.read_excel('fixtures_df.xlsx', index=False)

            # Remover as colunas indesejadas
            cols_to_drop = ['xG', 'Score', 'Day', 'xG.1', 'Attendance', 'Referee', 'Match Report', 'Notes']
            fixtures_df = fixtures_df.drop(columns=cols_to_drop, errors='ignore')

            # Renomear as colunas conforme solicitado
            fixtures_df = fixtures_df.rename(columns={
                'Wk': 'Rodada',
                'Time': 'Hora',
                'Home': 'Casa',
                'Away': 'Fora',
                'Venue': 'Estádio'
            })

            # Convertendo a coluna de datas para datetime
            fixtures_df['Date'] = pd.to_datetime(fixtures_df['Date'], errors='coerce')

            # Filtrar os próximos jogos do time selecionado
            today = datetime.today()
            proximos_jogos = fixtures_df[((fixtures_df['Casa'] == time_selecionado) | (fixtures_df['Fora'] == time_selecionado)) & (fixtures_df['Date'] >= today)]
            proximos_jogos = proximos_jogos.sort_values(by='Date').head(5)  # Ordenar por data e selecionar os próximos 5 jogos

            st.write(f"Próximos 5 jogos do {time_selecionado}")
            st.dataframe(proximos_jogos)
            
# Resetar o estado ao mudar de aba
def on_tab_change():
    st.session_state.show_result = False

