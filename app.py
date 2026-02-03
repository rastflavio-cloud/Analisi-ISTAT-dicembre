import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# --- 1. DATI (INVARIATI) ---
occ, dis, ina = 24142, 1426, 12518
t_occ, t_dis, t_ina = 62.5, 5.6, 33.7
v_occ_c, v_dis_c, v_ina_c = -20, -15, 31
v_occ_t, v_dis_t, v_ina_t = 62, -229, 163

# --- 2. CONFIGURAZIONE RESPONSIVE ---
st.set_page_config(page_title="Analisi Istat", layout="centered") # Centered aiuta su mobile

st.title("📊 Analisi Mercato del Lavoro")
st.markdown("### Dati Istat Dicembre 2025")

# --- 3. SEZIONE TASSI (CARTE INTERATTIVE) ---
# Le colonne di Streamlit si impilano automaticamente in verticale su smartphone
col1, col2, col3 = st.columns(3)
col1.metric("Occupazione", f"{t_occ}%")
col2.metric("Disoccupazione", f"{t_dis}%")
col3.metric("Inattività", f"{t_ina}%")

# --- 4. ANALISI TESTUALE (MOBILE FRIENDLY) ---
# Usiamo st.info per evitare lo scrolling laterale
st.info(f"""
**Variazione Mensile (Congiunturale)**
* Occupati: **{v_occ_c}k** | Disoccupati: **{v_dis_c}k** | Inattivi: **+{v_ina_c}k**
* **Incidenza Inattività: 206.7%**

**Variazione Annuale (Tendenziale)**
* Occupati: **+{v_occ_t}k** | Disoccupati: **{v_dis_t}k** | Inattivi: **+{v_ina_t}k**
* **Incidenza Inattività: 71.2%**
""")

# --- 5. GRAFICI ZOOMABILI (PLOTLY) ---

def crea_barre_interattive(labels, valori, titolo, colore):
    fig = go.Figure(data=[go.Bar(x=labels, y=valori, marker_color=colore, text=valori, textposition='auto')])
    fig.update_layout(
        title=titolo,
        margin=dict(l=20, r=20, t=40, b=20),
        height=300,
        yaxis=dict(autorange=True),
        dragmode='pan' # Permette di spostare il grafico con il dito
    )
    return fig

st.subheader("📈 Grafici Interattivi (Pizzica per zoom)")

# Tassi
fig_tassi = crea_barre_interattive(['Occupati', 'Disoccupati', 'Inattivi'], [t_occ, t_dis, t_ina], "Tassi Percentuali", '#3498db')
st.plotly_chart(fig_tassi, use_container_width=True)

# Tabs per risparmiare spazio verticale
tab_mese, tab_anno = st.tabs(["📊 Analisi Mensile", "📅 Analisi Annuale"])

with tab_mese:
    # Barre
    fig_c = crea_barre_interattive(['Occ', 'Dis', 'Ina'], [v_occ_c, v_dis_c, v_ina_c], "Variazioni Mensili (k)", '#e74c3c')
    st.plotly_chart(fig_c, use_container_width=True)
    
    # Torta (Incidenza)
    fig_pie_c = px.pie(names=['Inc. Occupazione', 'Inc. Inattività'], values=[133.3, 206.7], 
                       title="Incidenza su calo Disoccupati (-15k)", color_discrete_sequence=['#f1c40f', '#e67e22'])
    st.plotly_chart(fig_pie_c, use_container_width=True)

with tab_anno:
    # Barre
    fig_t = crea_barre_interattive(['Occ', 'Dis', 'Ina'], [v_occ_t, v_dis_t, v_ina_t], "Variazioni Annuali (k)", '#f39c12')
    st.plotly_chart(fig_t, use_container_width=True)
    
    # Torta (Incidenza)
    fig_pie_t = px.pie(names=['Inc. Occupazione', 'Inc. Inattività'], values=[27.1, 71.2], 
                       title="Incidenza su calo Disoccupati (-229k)", color_discrete_sequence=['#f1c40f', '#e67e22'])
    st.plotly_chart(fig_pie_t, use_container_width=True)
