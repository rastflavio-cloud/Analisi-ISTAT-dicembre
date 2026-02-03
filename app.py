import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# --- 1. DATI ISTAT DICEMBRE 2025 ---
occ, dis, ina = 24142, 1426, 12518
forza_lavoro = occ + dis
t_occ, t_dis, t_ina = 62.5, 5.6, 33.7

v_occ_c, v_dis_c, v_ina_c = -20, -15, 31
v_occ_t, v_dis_t, v_ina_t = 62, -229, 163

# --- 2. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Analisi Istat Dicembre 2025", layout="wide")
st.title("📊 Analisi Mercato del Lavoro")

# --- 3. MENU A TENDINA CON VALORI NEGATIVI IN ROSSO ---
with st.expander("📝 Leggi Analisi Dettagliata (Dati Terminale)", expanded=True):
    # Funzione per colorare i numeri negativi in rosso (HTML/Markdown)
    def color_val(val, unit="k"):
        color = "red" if val < 0 else "white"
        sign = "+" if val > 0 else ""
        return f"<span style='color:{color}; font-weight:bold;'>{sign}{val}{unit}</span>"

    st.markdown(f"""
    **FORZA LAVORO TOTALE:** {forza_lavoro} mila  
    **TASSO OCCUPAZIONE:** {t_occ}% | **DISOCCUPAZIONE:** {t_dis}% | **INATTIVITÀ:** {t_ina}%
    
    ---
    **ANALISI CONGIUNTURALE (MENSILE)** Variazioni: Occupati {color_val(v_occ_c)} | Disoccupati {color_val(v_dis_c)} | Inattivi {color_val(v_ina_c)}  
    Incidenza Occupazione su Disoccupazione: **133.3%** Incidenza Inattività su Disoccupazione: **206.7%**

    ---
    **ANALISI TENDENZIALE (ANNUALE)** Variazioni: Occupati {color_val(v_occ_t)} | Disoccupati {color_val(v_dis_t)} | Inattivi {color_val(v_ina_t)}  
    Incidenza Occupazione su Disoccupazione: **27.1%** Incidenza Inattività su Disoccupazione: **71.2%**
    """, unsafe_allow_html=True)

# --- 4. FUNZIONE GRAFICI INTERATTIVI (CON COLORI ORIGINALI) ---
def crea_barre_istat(labels, valori, titolo, colori):
    fig = go.Figure(data=[go.Bar(
        x=labels, 
        y=valori, 
        marker_color=colori, 
        text=[f"{v}k" if abs(v) > 100 else f"{v}%" for v in valori],
        textposition='auto',
        textfont=dict(weight='bold')
    )])
    fig.update_layout(
        title=dict(text=titolo, font=dict(size=18, weight='bold')),
        height=450, # Più grande per leggibilità
        margin=dict(l=20, r=20, t=60, b=20),
        yaxis=dict(showgrid=True, zeroline=True, zerolinewidth=2, zerolinecolor='black'),
        dragmode='pan'
    )
    return fig

# --- 5. VISUALIZZAZIONE GRAFICI ---
st.write("### 📈 Visualizzazione Grafica")

# Tassi Generali (Sempre visibile)
col_tassi = st.columns([1, 2, 1])
with col_tassi[1]:
    fig_tassi = crea_barre_istat(['Occ', 'Dis', 'Ina'], [t_occ, t_dis, t_ina], 
                               f"TASSI ATTUALI: {t_occ}% | {t_dis}% | {t_ina}%", 
                               ['#3498db', '#e74c3c', '#95a5a6'])
    st.plotly_chart(fig_tassi, use_container_width=True)

# Tabs Grandi per Analisi Mensile e Annuale
tab1, tab2 = st.tabs(["🔴 ANALISI MENSILE (Congiunturale)", "🟡 ANALISI ANNUALE (Tendenziale)"])

with tab1:
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        # Colore Rosso/Arancione come richiesto
        fig_c = crea_barre_istat(['Occupati', 'Disoccupati', 'Inattivi'], [v_occ_c, v_dis_c, v_ina_c], 
                                "VARIAZIONI ASSOLUTE (Mese)", ['red', 'red', 'orange'])
        st.plotly_chart(fig_c, use_container_width=True)
    with col_m2:
        fig_p_c = px.pie(names=['Inc. Occupazione', 'Inc. Inattività'], values=[133.3, 206.7], 
                         title="INCIDENZA SU CALO DISOCCUPATI (-15k)",
                         color_discrete_sequence=['yellow', 'orange'])
        fig_p_c.update_traces(textinfo='label+percent', textfont_size=14)
        st.plotly_chart(fig_p_c, use_container_width=True)

with tab2:
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        # Colore Giallo/Rosso/Arancione come richiesto
        fig_t = crea_barre_istat(['Occupati', 'Disoccupati', 'Inattivi'], [v_occ_t, v_dis_t, v_ina_t], 
                                "VARIAZIONI ASSOLUTE (Anno)", ['yellow', 'red', 'orange'])
        st.plotly_chart(fig_t, use_container_width=True)
    with col_a2:
        fig_p_t = px.pie(names=['Inc. Occupazione', 'Inc. Inattività'], values=[27.1, 71.2], 
                         title="INCIDENZA SU CALO DISOCCUPATI (-229k)",
                         color_discrete_sequence=['yellow', 'orange'])
        fig_p_t.update_traces(textinfo='label+percent', textfont_size=14)
        st.plotly_chart(fig_p_t, use_container_width=True)
