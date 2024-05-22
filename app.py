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
    Nosso app serve para prever estatisticamente o número de cartões numa determinada partida
""")

tab_jogos, tab_juizes, tab_times = st.tabs(['Jogos', 'Juizes', 'Times'])

st.write("""
    <div style="position: absolute; top: 10px; left: 10px;">
        <img src="https://www.google.com/search?q=juiz+futebol+desenho&sca_esv=69d501c9217a3f8b&sca_upv=1&rlz=1C1GCEU_pt-BRBR1111&udm=2&biw=1920&bih=945&sxsrf=ADLYWIIkRe0HYgUAPCRxUgRz9UfITAirlA%3A1716402598437&ei=pjlOZqGeGsrc1sQPoPivuAY&oq=juiz+futebol+dese&gs_lp=Egxnd3Mtd2l6LXNlcnAiEWp1aXogZnV0ZWJvbCBkZXNlKgIIADIFEAAYgAQyBhAAGAgYHkiWFVCgBVieCXABeACQAQCYAXmgAcYEqgEDMC41uAEByAEA-AEBmAIGoALWBMICChAAGIAEGEMYigXCAgQQABgemAMAiAYBkgcDMS41oAfNEQ&sclient=gws-wiz-serp#vhid=OPV06zbO3RGmwM&vssid=mosaic" style="width: 100px;">
    </div>
""", unsafe_allow_html=True)
