import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# --- 1. DATI ISTAT DICEMBRE 2025 (ORIGINALI) ---
occ, dis, ina = 24142, 1426, 12518
forza_lavoro = occ + dis
t_occ, t_dis, t_ina = 62.5, 5.6, 33.7

# Variazioni Congiunturali (Mensili)
v_occ_c, v_dis_c, v_ina_c = -20, -15, 31
# Variazioni Tendenziali (Annuali)
v_occ_t, v_dis_t, v_ina_t = 62, -229, 163

# --- 2. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Analisi Istat Dicembre 2025", layout="wide")
st.title("📊 Analisi Mercato del Lavoro")

# --- 3. MENU A TENDINA CON TUTTI I DATI E ROSSO PER NEGATIVI ---
with st.expander("📝 ANALISI DETTAGLIATA (Dati Completi)", expanded=True):
    
    def color_val(val, unit=" mila"):
        color = "red" if val < 0 else "#00ff00" # Rosso se negativo, verde fluo se positivo
        sign = "+" if val > 0 else ""
        return f"<span style='color:{color}; font-weight:bold;'>{sign}{val}{unit}</span>"

    st.markdown(f"""
    **FORZA LAVORO TOTALE:** {forza_lavoro} mila  
    **TASSO OCCUPAZIONE:** {t_occ}% | **DISOCCUPAZIONE:** {t_dis}% | **INATTIVITÀ:** {t_ina}%
    
    --- 
    ### --- ANALISI CONGIUNTURALE (ASSOLUTI) ---
    Variazioni: Occupati {color_val(v_occ_c)} | Disoccupati {color_val(v_dis_c)} | Inattivi {color_val(v_ina_c)}  
    * Incidenza Occupazione su Disoccupazione: **133.3%** * Incidenza Inattività su Disoccupazione: **206.7%**

    ---
    ### --- ANALISI TENDENZIALE (ASSOLUTI) ---
    Variazioni: Occupati {color_val(v_occ_t)} | Disoccupati {color_val(v_dis_t)} | Inattivi {color_val(v_ina_t)}  
    * Incidenza Occupazione su Disoccupazione: **-27.1%** * Incidenza Inattività su Disoccupazione: **71.2%**
    """, unsafe_allow_html=True)

# --- 4. FUNZIONE GRAFICI (COLORI E IMPOSTAZIONI ORIGINALI) ---
def crea_barre_istat(labels, valori, titolo, colori):
    fig = go.Figure(data=[go.Bar(
        x=labels, 
        y=valori, 
        marker_color=colori, 
        text=[f"{v}k" if abs(v) > 100 or v < 0 else f"{v}%" for v in valori],
        textposition='auto',
        textfont=dict(weight='bold', size=14)
    )])
    fig.update_layout(
        title=dict(text=titolo, font=dict(size=20, weight='bold')),
        height=500, # Dimensione grande richiesta
        margin=dict(l=20, r=20, t=60, b=20),
        yaxis=dict(zeroline=True, zerolinewidth=3, zerolinecolor='black'),
        dragmode='pan'
    )
    return fig

# --- 5. VISUALIZZAZIONE GRAFICI ---
st.write("### 📈 Visualizzazione Grafica Interattiva")

# Tassi Generali
fig_tassi = crea_barre_istat(['Occ', 'Dis', 'Ina'], [t_occ, t_dis, t_ina], 
                           f"TASSI ATTUALI: {t_occ}% | {t_dis}% | {t_ina}%", 
                           ['#3498db', '#e74c3c', '#95a5a6'])
st.plotly_chart(fig_tassi, use_container_width=True)

# Tabs per le due analisi
tab1, tab2 = st.tabs(["🔴 ANALISI CONGIUNTURALE", "🟡 ANALISI ANNUALE"])

with tab1:
    col_m1, col_m2 = st.columns([1.2, 0.8]) # Colonna grafico più grande
    with col_m1:
        fig_c = crea_barre_istat(['Occupati', 'Disoccupati', 'Inattivi'], [v_occ_c, v_dis_c, v_ina_c], 
                                "ANALISI CONGIUNTURALE (ASSOLUTI)", ['red', 'red', 'orange'])
        st.plotly_chart(fig_c, use_container_width=True)
    with col_m2:
        fig_p_c = px.pie(names=['Inc. Occupazione', 'Inc. Inattività'], values=[133.3, 206.7], 
                         title="INCIDENZA SU DISOCCUPAZIONE (-15k)")
        fig_p_c.update_traces(marker=dict(colors=['yellow', 'orange']), textinfo='label+percent')
        st.plotly_chart(fig_p_c, use_container_width=True)

with tab2:
    col_a1, col_a2 = st.columns([1.2, 0.8])
    with col_a1:
        fig_t = crea_barre_istat(['Occupati', 'Disoccupati', 'Inattivi'], [v_occ_t, v_dis_t, v_ina_t], 
                                "ANALISI TENDENZIALE (ASSOLUTI)", ['yellow', 'red', 'orange'])
        st.plotly_chart(fig_t, use_container_width=True)
    with col_a2:
        fig_p_t = px.pie(names=['Inc. Occupazione', 'Inc. Inattività'], values=[27.1, 71.2], 
                         title="INCIDENZA SU DISOCCUPAZIONE (-229k)")
        fig_p_t.update_traces(marker=dict(colors=['yellow', 'orange']), textinfo='label+percent')
        st.plotly_chart(fig_p_t, use_container_width=True)
