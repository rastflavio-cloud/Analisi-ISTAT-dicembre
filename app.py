import streamlit as st
import matplotlib.pyplot as plt

# --- 1. DATI ISTAT DICEMBRE 2025 ---
occ, dis, ina = 24142, 1426, 12518
t_occ, t_dis, t_ina = 62.5, 5.6, 33.7
v_occ_c, v_dis_c, v_ina_c = -20, -15, 31
v_occ_t, v_dis_t, v_ina_t = 62, -229, 163

# --- 2. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Analisi Istat", layout="wide")
st.title("📊 Analisi Mercato del Lavoro")
st.caption("Dati Dicembre 2025 - Ottimizzato per Mobile")

# --- 3. SEZIONE TASSI (CARD DINAMICHE) ---
# Le colonne su mobile si impilano automaticamente
c1, c2, c3 = st.columns(3)
c1.metric("Occupazione", f"{t_occ}%")
c2.metric("Disoccupazione", f"{t_dis}%")
c3.metric("Inattività", f"{t_ina}%")

# --- 4. ANALISI TESTUALE (Senza scrolling orizzontale) ---
with st.expander("📝 Leggi Analisi Dettagliata", expanded=True):
    st.markdown(f"""
    **Variazione Congiunturale (Mensile):**
    * Occupati: `{v_occ_c}k` | Disoccupati: `{v_dis_c}k` | Inattivi: `+{v_ina_c}k`
    * **Incidenza Inattività: 206.7%**

    **Variazione Tendenziale (Annuale):**
    * Occupati: `+{v_occ_t}k` | Disoccupati: `{v_dis_t}k` | Inattivi: `+{v_ina_t}k`
    * **Incidenza Inattività: 71.2%**
    """)

# --- 5. GRAFICI (Uno per riga per leggibilità mobile) ---
st.subheader("📈 Grafici di Analisi")

# Funzione per creare grafici singoli più grandi e leggibili
def crea_grafico_barre(labels, valori, titolo, color):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(labels, valori, color=color)
    ax.set_title(titolo, fontsize=12, fontweight='bold')
    ax.axhline(0, color='black', linewidth=0.8)
    for i, v in enumerate(valori):
        ax.text(i, v + (0.5 if v > 0 else -1.5), f'{v}', ha='center', fontweight='bold')
    plt.tight_layout()
    return fig

# Visualizzazione sequenziale (ideale per smartphone)
st.pyplot(crea_grafico_barre(['Occ', 'Dis', 'Ina'], [t_occ, t_dis, t_ina], "Tassi Percentuali", ['#3498db', '#e74c3c', '#95a5a6']))

tab1, tab2 = st.tabs(["Mensile", "Annuale"])

with tab1:
    st.pyplot(crea_grafico_barre(['Occ', 'Dis', 'Ina'], [v_occ_c, v_dis_c, v_ina_c], "Variazioni Assolute (Mensili)", 'orange'))
    # Grafico a torta semplificato per mobile
    fig2, ax2 = plt.subplots()
    ax2.pie([133.3, 206.7], labels=['Occ', 'Ina'], autopct='%1.1f%%', colors=['yellow', 'orange'])
    st.write("**Incidenza su calo Disoccupati (-15k)**")
    st.pyplot(fig2)

with tab2:
    st.pyplot(crea_grafico_barre(['Occ', 'Dis', 'Ina'], [v_occ_t, v_dis_t, v_ina_t], "Variazioni Assolute (Annuali)", 'red'))
