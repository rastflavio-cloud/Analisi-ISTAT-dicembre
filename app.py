import streamlit as st
import matplotlib.pyplot as plt

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
        color = "red" if val < 0 else "#00ff00" 
        sign = "+" if val > 0 else ""
        return f"<span style='color:{color}; font-weight:bold;'>{sign}{val}{unit}</span>"

    st.markdown(f"""
    **FORZA LAVORO TOTALE:** {forza_lavoro} mila  
    **TASSO OCCUPAZIONE:** {t_occ}% | **DISOCCUPAZIONE:** {t_dis}% | **INATTIVITÀ:** {t_ina}%
    
    --- 
    ### --- ANALISI CONGIUNTURALE (ASSOLUTI) ---
    Variazioni: Occupati {color_val(v_occ_c)} | Disoccupati {color_val(v_dis_c)} | Inattivi {color_val(v_ina_c)}  
    * Incidenza Occupazione su Disoccupazione: **133.3%**
    * Incidenza Inattività su Disoccupazione: **206.7%**

    ---
    ### --- ANALISI TENDENZIALE (ASSOLUTI) ---
    Variazioni: Occupati {color_val(v_occ_t)} | Disoccupati {color_val(v_dis_t)} | Inattivi {color_val(v_ina_t)}  
    * Incidenza Occupazione su Disoccupazione: **-27.1%**
    * Incidenza Inattività su Disoccupazione: **71.2%**
    """, unsafe_allow_html=True)

# --- 4. FUNZIONE GRAFICI STATICI (MATPLOTLIB) ---
st.write("### 📈 Visualizzazione Grafica (Statica)")

# Tassi Generali (Grafico Fisso)
fig1, ax1 = plt.subplots(figsize=(10, 5))
t_labs = ['Occ', 'Dis', 'Ina']
t_vals = [t_occ, t_dis, t_ina]
ax1.bar(t_labs, t_vals, color=['#3498db', '#e74c3c', '#95a5a6'], width=0.5)
ax1.set_title(f"TASSI ATTUALI: {t_occ}% | {t_dis}% | {t_ina}%", fontsize=14, fontweight='bold')
for i, v in enumerate(t_vals):
    ax1.text(i, v + 1, f"{v}%", ha='center', fontweight='bold')
st.pyplot(fig1)

# Tabs per le due analisi
tab1, tab2 = st.tabs(["🔴 ANALISI CONGIUNTURALE", "🟡 ANALISI ANNUALE"])

with tab1:
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        fig_c, ax_c = plt.subplots(figsize=(8, 6))
        c_vals = [v_occ_c, v_dis_c, v_ina_c]
        ax_c.bar(['Occupati', 'Disoccupati', 'Inattivi'], c_vals, color=['red', 'red', 'orange'])
        ax_c.axhline(0, color='black', linewidth=1.5)
        ax_c.set_title("ANALISI CONGIUNTURALE (ASSOLUTI)", fontweight='bold')
        for i, v in enumerate(c_vals):
            ax_c.text(i, v + (1 if v > 0 else -3), f"{v}k", ha='center', fontweight='bold')
        st.pyplot(fig_c)
    with col_m2:
        fig_p1, ax_p1 = plt.subplots(figsize=(8, 6))
        ax_p1.pie([133.3, 206.7], labels=['Inc. Occupazione\n133.3%', 'Inc. Inattività\n206.7%'], 
                  colors=['yellow', 'orange'], startangle=90, autopct='%1.1f%%')
        ax_p1.set_title("INCIDENZA SU DISOCCUPAZIONE (-15k)", fontweight='bold')
        st.pyplot(fig_p1)

with tab2:
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        fig_t, ax_t = plt.subplots(figsize=(8, 6))
        t_vals_arr = [v_occ_t, v_dis_t, v_ina_t]
        ax_t.bar(['Occupati', 'Disoccupati', 'Inattivi'], t_vals_arr, color=['yellow', 'red', 'orange'])
        ax_t.axhline(0, color='black', linewidth=1.5)
        ax_t.set_title("ANALISI TENDENZIALE (ASSOLUTI)", fontweight='bold')
        for i, v in enumerate(t_vals_arr):
            ax_t.text(i, v + (5 if v > 0 else -20), f"{v:+}k", ha='center', fontweight='bold')
        st.pyplot(fig_t)
    with col_a2:
        fig_p2, ax_p2 = plt.subplots(figsize=(8, 6))
        ax_p2.pie([27.1, 71.2], labels=['Inc. Occupazione\n27.1%', 'Inc. Inattività\n71.2%'], 
                  colors=['yellow', 'orange'], startangle=90, autopct='%1.1f%%')
        ax_p2.set_title("INCIDENZA SU DISOCCUPAZIONE (-229k)", fontweight='bold')
        st.pyplot(fig_p2)
