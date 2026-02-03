import streamlit as st

import matplotlib.pyplot as plt

# --- 1. DATI ISTAT DICEMBRE 2025 ---
occ, dis, ina = 24142, 1426, 12518
forza_lavoro = occ + dis
t_occ, t_dis, t_ina = 62.5, 5.6, 33.7

v_occ_c, v_dis_c, v_ina_c = -20, -15, 31
v_occ_t, v_dis_t, v_ina_t = 62, -229, 163

# --- 2. INTERFACCIA WEB ---
st.set_page_config(page_title="Analisi Istat Dicembre 2025", layout="wide")
st.title("📊 Analisi Mercato del Lavoro - Dicembre 2025")

# Output dei dati (Stile pulito)
terminal_output = f"""
FORZA LAVORO TOTALE: {forza_lavoro} mila
TASSO OCCUPAZIONE: {t_occ}% | DISOCCUPAZIONE: {t_dis}% | INATTIVITÀ: {t_ina}%

--- ANALISI CONGIUNTURALE (ASSOLUTI) ---
Variazioni: Occupati {v_occ_c} mila | Disoccupati {v_dis_c} mila | Inattivi {v_ina_c} mila
Incidenza Occupazione su Disoccupazione: 133.3%
Incidenza Inattività su Disoccupazione: 206.7%

--- ANALISI TENDENZIALE (ASSOLUTI) ---
Variazioni: Occupati +{v_occ_t} mila | Disoccupati {v_dis_t} mila | Inattivi +{v_ina_t} mila
Incidenza Occupazione su Disoccupazione: 27.1%
Incidenza Inattività su Disoccupazione: 71.2%
"""
st.code(terminal_output, language='text')

# Tabella riassuntiva
st.write("### 📋 Riepilogo Variazioni (mila)")
dati_tabella = {
    "Categoria": ["Occupati", "Disoccupati", "Inattivi"],
    "Congiunturale (Mensile)": [f"{v_occ_c}k", f"{v_dis_c}k", f"{v_ina_c}k"],
    "Tendenziale (Annuale)": [f"+{v_occ_t}k", f"{v_dis_t}k", f"+{v_ina_t}k"]
}
st.table(dati_tabella)

# --- 3. GENERAZIONE GRAFICI ---
st.write("### 📈 Visualizzazione Grafica")
fig = plt.figure(figsize=(15, 12))

# TASSI GENERALI
ax1 = plt.subplot(3, 2, 1)
tassi_val = [t_occ, t_dis, t_ina]
ax1.bar(['Occ', 'Dis', 'Ina'], tassi_val, color=['#3498db', '#e74c3c', '#95a5a6'], width=0.4)
ax1.set_title(f'TASSI ATTUALI: {t_occ}% | {t_dis}% | {t_ina}%')
for i, v in enumerate(tassi_val):
    ax1.text(i, v + 1, f'{v}%', ha='center', fontweight='bold')

# CONGIUNTURALE (Barre)
ax2_bar = plt.subplot(3, 2, 3)
ax2_bar.bar(['Occupati', 'Disoccupati', 'Inattivi'], [v_occ_c, v_dis_c, v_ina_c], color=['red', 'red', 'orange'])
ax2_bar.axhline(0, color='black', linewidth=1)
ax2_bar.set_title('ANALISI CONGIUNTURALE (ASSOLUTI)')
for i, v in enumerate([v_occ_c, v_dis_c, v_ina_c]):
    ax2_bar.text(i, v + (1 if v > 0 else -4), f'{v}k', ha='center', fontweight='bold')

# CONGIUNTURALE (Torta)
ax2_pie = plt.subplot(3, 2, 4)
ax2_pie.pie([133.3, 206.7], labels=['Inc. Occupazione\n133.3%', 'Inc. Inattività\n206.7%'], 
            colors=['yellow', 'orange'], startangle=90)
ax2_pie.set_title('INCIDENZA CONGIUNTURALE SU DISOCCUPAZIONE (-15k)')

# TENDENZIALE (Barre)
ax3_bar = plt.subplot(3, 2, 5)
ax3_bar.bar(['Occupati', 'Disoccupati', 'Inattivi'], [v_occ_t, v_dis_t, v_ina_t], color=['yellow', 'red', 'orange'])
ax3_bar.axhline(0, color='black', linewidth=1)
ax3_bar.set_title('ANALISI TENDENZIALE (ASSOLUTI)')
for i, v in enumerate([v_occ_t, v_dis_t, v_ina_t]):
    ax3_bar.text(i, v + (5 if v > 0 else -25), f'{v:+}k', ha='center', fontweight='bold')

# TENDENZIALE (Torta)
ax3_pie = plt.subplot(3, 2, 6)
ax3_pie.pie([27.1, 71.2], labels=['Inc. Occupazione\n27.1%', 'Inc. Inattività\n71.2%'], 
            colors=['yellow', 'orange'], startangle=90)
ax3_pie.set_title('INCIDENZA TENDENZIALE SU DISOCCUPAZIONE (-229k)')

plt.tight_layout()
st.pyplot(fig)