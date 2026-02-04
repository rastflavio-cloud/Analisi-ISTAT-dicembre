import streamlit as st

import matplotlib.pyplot as plt

# --- 1. DATABASE COMPLETO DATI ISTAT 2025 ---
database_istat = {
    "Dicembre 2025": {
        "occ": 24142, "dis": 1426, "ina": 12518, "t_occ": 62.5, "t_dis": 5.6, "t_ina": 33.7,
        "v_occ_c": -20, "v_dis_c": -15, "v_ina_c": 31, "v_occ_t": 62, "v_dis_t": -229, "v_ina_t": 163,
        "inc_occ_c": 133.3, "inc_ina_c": 206.7, "inc_occ_t": -27.1, "inc_ina_t": 71.2, "calo_dis_c": "-15k", "calo_dis_t": "-229k"
    },
    "Novembre 2025": {
        "occ": 24188, "dis": 1469, "ina": 12440, "t_occ": 62.6, "t_dis": 5.7, "t_ina": 33.5,
        "v_occ_c": -34, "v_dis_c": -30, "v_ina_c": 72, "v_occ_t": 179, "v_dis_t": -106, "v_ina_t": -35,
        "inc_occ_c": 113.3, "inc_ina_c": 240.0, "inc_occ_t": -168.9, "inc_ina_t": -33.0, "calo_dis_c": "-30k", "calo_dis_t": "-106k"
    },
    "Agosto 2025": {
        "occ": 24170, "dis": 1531, "ina": 12390, "t_occ": 62.6, "t_dis": 6.0, "t_ina": 33.3,
        "v_occ_c": -57, "v_dis_c": 7, "v_ina_c": 60, "v_occ_t": 103, "v_dis_t": -75, "v_ina_t": -2,
        "inc_occ_c": -814.3, "inc_ina_c": 857.1, "inc_occ_t": -137.3, "inc_ina_t": -2.7, "calo_dis_c": "7k", "calo_dis_t": "-75k"
    },
    "Luglio 2025": {
        "occ": 24217, "dis": 1532, "ina": 12322, "t_occ": 62.8, "t_dis": 6.0, "t_ina": 33.2,
        "v_occ_c": 13, "v_dis_c": -74, "v_ina_c": 30, "v_occ_t": 218, "v_dis_t": -114, "v_ina_t": -81,
        "inc_occ_c": -17.6, "inc_ina_c": 40.5, "inc_occ_t": -191.2, "inc_ina_t": -71.1, "calo_dis_c": "-74k", "calo_dis_t": "-114k"
    },
    "Giugno 2025": {
        "occ": 24326, "dis": 1621, "ina": 12200, "t_occ": 62.9, "t_dis": 6.3, "t_ina": 32.8,
        "v_occ_c": 16, "v_dis_c": -71, "v_ina_c": 69, "v_occ_t": 363, "v_dis_t": -94, "v_ina_t": -142,
        "inc_occ_c": -22.5, "inc_ina_c": 97.2, "inc_occ_t": -386.2, "inc_ina_t": -151.1, "calo_dis_c": "-71k", "calo_dis_t": "-94k"
    },
    "Maggio 2025": {
        "occ": 24301, "dis": 1691, "ina": 12119, "t_occ": 62.9, "t_dis": 6.5, "t_ina": 32.6,
        "v_occ_c": 80, "v_dis_c": 113, "v_ina_c": -172, "v_occ_t": 408, "v_dis_t": 15, "v_ina_t": -320,
        "inc_occ_c": 70.8, "inc_ina_c": -152.2, "inc_occ_t": 2720.0, "inc_ina_t": -2133.3, "calo_dis_c": "113k", "calo_dis_t": "15k"
    },
    "Aprile 2025": {
        "occ": 24200, "dis": 1514, "ina": 12361, "t_occ": 62.7, "t_dis": 5.9, "t_ina": 33.2,
        "v_occ_c": 0, "v_dis_c": -48, "v_ina_c": 39, "v_occ_t": 282, "v_dis_t": -209, "v_ina_t": 14,
        "inc_occ_c": 0.0, "inc_ina_c": 81.3, "inc_occ_t": -134.9, "inc_ina_t": 6.7, "calo_dis_c": "-48k", "calo_dis_t": "-209k"
    },
    "Marzo 2025": {
        "occ": 24307, "dis": 1555, "ina": 12248, "t_occ": 63.0, "t_dis": 6.0, "t_ina": 32.9,
        "v_occ_c": -16, "v_dis_c": 32, "v_ina_c": -11, "v_occ_t": 450, "v_dis_t": -208, "v_ina_t": -107,
        "inc_occ_c": -50.0, "inc_ina_c": -34.4, "inc_occ_t": -216.3, "inc_ina_t": -51.4, "calo_dis_c": "32k", "calo_dis_t": "-208k"
    },
    "Febbraio 2025": {
        "occ": 24332, "dis": 1517, "ina": 12254, "t_occ": 63.0, "t_dis": 5.9, "t_ina": 32.9,
        "v_occ_c": 47, "v_dis_c": -79, "v_ina_c": 33, "v_occ_t": 567, "v_dis_t": -342, "v_ina_t": -60,
        "inc_occ_c": -59.5, "inc_ina_c": 41.8, "inc_occ_t": -165.8, "inc_ina_t": -17.5, "calo_dis_c": "-79k", "calo_dis_t": "-342k"
    },
    "Gennaio 2025": {
        "occ": 24222, "dis": 1621, "ina": 12242, "t_occ": 62.8, "t_dis": 6.3, "t_ina": 32.9,
        "v_occ_c": 145, "v_dis_c": -9, "v_ina_c": -146, "v_occ_t": 513, "v_dis_t": -194, "v_ina_t": -158,
        "inc_occ_c": -1611.1, "inc_ina_c": -1622.2, "inc_occ_t": -264.4, "inc_ina_t": -81.4, "calo_dis_c": "-9k", "calo_dis_t": "-194k"
    }
}

# --- 2. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Analisi Istat 2025", layout="wide")
st.title("📊 Analisi Mercato del Lavoro 2025")

# --- 3. SELEZIONE DEL MESE ---
mese = st.selectbox("Seleziona il mese da visualizzare:", list(database_istat.keys()))
d = database_istat[mese]

# --- 4. ANALISI TESTUALE ---
with st.expander(f"📝 ANALISI DETTAGLIATA - {mese}", expanded=True):
    def color_val(val, unit=" mila"):
        color = "red" if val < 0 else "#00ff00" 
        sign = "+" if val > 0 else ""
        return f"<span style='color:{color}; font-weight:bold;'>{sign}{val}{unit}</span>"
    
    def black_bold_val(val, unit=" mila"):
        sign = "+" if val > 0 else ""
        return f"<span style='color:black; font-weight:bold;'>{sign}{val}{unit}</span>"

    st.markdown(f"""
    **FORZA LAVORO TOTALE:** {d['occ'] + d['dis']} mila  
    **TASSO OCCUPAZIONE:** {d['t_occ']}% | **DISOCCUPAZIONE:** {d['t_dis']}% | **INATTIVITÀ:** {d['t_ina']}%
    
    --- 
    ### --- ANALISI CONGIUNTURALE (ASSOLUTI) ---
    Variazioni: Occupati {color_val(d['v_occ_c'])} | Disoccupati {black_bold_val(d['v_dis_c'])} | Inattivi {color_val(d['v_ina_c'])}  
    * Incidenza Occupazione su Disoccupazione: **{d['inc_occ_c']}%**
    * Incidenza Inattività su Disoccupazione: **{d['inc_ina_c']}%**

    ---
    ### --- ANALISI TENDENZIALE (ASSOLUTI) ---
    Variazioni: Occupati {color_val(d['v_occ_t'])} | Disoccupati {black_bold_val(d['v_dis_t'])} | Inattivi {color_val(d['v_ina_t'])}  
    * Incidenza Occupazione su Disoccupazione: **{d['inc_occ_t']}%**
    * Incidenza Inattività su Disoccupazione: **{d['inc_ina_t']}%**
    """, unsafe_allow_html=True)

# --- 5. GRAFICI STATICI (MATPLOTLIB) ---
st.write(f"### 📈 Grafici {mese}")
colors_std = ['#3498db', '#e74c3c', '#95a5a6']

# Grafico Tassi
fig1, ax1 = plt.subplots(figsize=(10, 4))
ax1.bar(['Occ', 'Dis', 'Ina'], [d['t_occ'], d['t_dis'], d['t_ina']], color=colors_std, width=0.5)
ax1.set_title(f"TASSI ATTUALI ({mese})", fontweight='bold')
for i, v in enumerate([d['t_occ'], d['t_dis'], d['t_ina']]):
    ax1.text(i, v + 1, f"{v}%", ha='center', fontweight='bold')
st.pyplot(fig1)

tab1, tab2 = st.tabs(["🔴 ANALISI MENSILE", "🟡 ANALISI ANNUALE"])

with tab1:
    c1, c2 = st.columns(2)
    with c1:
        fig_c, ax_c = plt.subplots(figsize=(8, 6))
        v_c = [d['v_occ_c'], d['v_dis_c'], d['v_ina_c']]
        ax_c.bar(['Occupati', 'Disoccupati', 'Inattivi'], v_c, color=colors_std)
        ax_c.axhline(0, color='black', linewidth=1.5)
        ax_c.set_title("VARIAZIONE MENSILE (k)", fontweight='bold')
        for i, v in enumerate(v_c):
            ax_c.text(i, v + (1 if v > 0 else -3), f"{v}k", ha='center', fontweight='bold')
        st.pyplot(fig_c)
    with c2:
        fig_p1, ax_p1 = plt.subplots(figsize=(8, 6))
        labels_c = [f"Inc. Occ\n{d['inc_occ_c']}%", f"Inc. Ina\n{d['inc_ina_c']}%"]
        ax_p1.pie([abs(d['inc_occ_c']), abs(d['inc_ina_c'])], labels=labels_c, 
                  colors=['#3498db', '#95a5a6'], startangle=90, autopct='%1.1f%%', textprops={'fontweight':'bold'})
        ax_p1.set_title(f"INCIDENZA SU VAR. DISOCCUPATI ({d['v_dis_c']}k)", fontweight='bold')
        st.pyplot(fig_p1)

with tab2:
    c3, c4 = st.columns(2)
    with c3:
        fig_t, ax_t = plt.subplots(figsize=(8, 6))
        v_t = [d['v_occ_t'], d['v_dis_t'], d['v_ina_t']]
        ax_t.bar(['Occupati', 'Disoccupati', 'Inattivi'], v_t, color=colors_std)
        ax_t.axhline(0, color='black', linewidth=1.5)
        ax_t.set_title("VARIAZIONE ANNUALE (k)", fontweight='bold')
        for i, v in enumerate(v_t):
            ax_t.text(i, v + (5 if v > 0 else -20), f"{v:+}k", ha='center', fontweight='bold')
        st.pyplot(fig_t)
    with c4:
        fig_p2, ax_p2 = plt.subplots(figsize=(8, 6))
        labels_t = [f"Inc. Occ\n{d['inc_occ_t']}%", f"Inc. Ina\n{d['inc_ina_t']}%"]
        ax_p2.pie([abs(d['inc_occ_t']), abs(d['inc_ina_t'])], labels=labels_t, 
                  colors=['#3498db', '#95a5a6'], startangle=90, autopct='%1.1f%%', textprops={'fontweight':'bold'})
        ax_p2.set_title(f"INCIDENZA SU VAR. DISOCCUPATI ({d['v_dis_t']}k)", fontweight='bold')
        st.pyplot(fig_p2)
