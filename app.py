import streamlit as st
import matplotlib.pyplot as plt

# --- 1. DATABASE COMPLETO DATI ISTAT 2025 ---
database_istat = {
    "Dicembre 2025": {"occ": 24142, "dis": 1426, "ina": 12518, "t_occ": 62.5, "t_dis": 5.6, "t_ina": 33.7, "v_occ_c": -20, "v_dis_c": -15, "v_ina_c": 31, "v_occ_t": 62, "v_dis_t": -229, "v_ina_t": 163, "inc_occ_c": 133.3, "inc_ina_c": 206.7, "inc_occ_t": -27.1, "inc_ina_t": 71.2},
    "Novembre 2025": {"occ": 24188, "dis": 1469, "ina": 12440, "t_occ": 62.6, "t_dis": 5.7, "t_ina": 33.5, "v_occ_c": -34, "v_dis_c": -30, "v_ina_c": 72, "v_occ_t": 179, "v_dis_t": -106, "v_ina_t": -35, "inc_occ_c": 113.3, "inc_ina_c": 240.0, "inc_occ_t": -168.9, "inc_ina_t": -33.0},
    "Agosto 2025": {"occ": 24170, "dis": 1531, "ina": 12390, "t_occ": 62.6, "t_dis": 6.0, "t_ina": 33.3, "v_occ_c": -57, "v_dis_c": 7, "v_ina_c": 60, "v_occ_t": 103, "v_dis_t": -75, "v_ina_t": -2, "inc_occ_c": -814.3, "inc_ina_c": 857.1, "inc_occ_t": -137.3, "inc_ina_t": -2.7},
    "Luglio 2025": {"occ": 24217, "dis": 1532, "ina": 12322, "t_occ": 62.8, "t_dis": 6.0, "t_ina": 33.2, "v_occ_c": 13, "v_dis_c": -74, "v_ina_c": 30, "v_occ_t": 218, "v_dis_t": -114, "v_ina_t": -81, "inc_occ_c": -17.6, "inc_ina_c": 40.5, "inc_occ_t": -191.2, "inc_ina_t": -71.1},
    "Giugno 2025": {"occ": 24326, "dis": 1621, "ina": 12200, "t_occ": 62.9, "t_dis": 6.3, "t_ina": 32.8, "v_occ_c": 16, "v_dis_c": -71, "v_ina_c": 69, "v_occ_t": 363, "v_dis_t": -94, "v_ina_t": -142, "inc_occ_c": -22.5, "inc_ina_c": 97.2, "inc_occ_t": -386.2, "inc_ina_t": -151.1},
    "Maggio 2025": {"occ": 24301, "dis": 1691, "ina": 12119, "t_occ": 62.9, "t_dis": 6.5, "t_ina": 32.6, "v_occ_c": 80, "v_dis_c": 113, "v_ina_c": -172, "v_occ_t": 408, "v_dis_t": 15, "v_ina_t": -320, "inc_occ_c": 70.8, "inc_ina_c": -152.2, "inc_occ_t": 2720.0, "inc_ina_t": -2133.3},
    "Aprile 2025": {"occ": 24200, "dis": 1514, "ina": 12361, "t_occ": 62.7, "t_dis": 5.9, "t_ina": 33.2, "v_occ_c": 0, "v_dis_c": -48, "v_ina_c": 39, "v_occ_t": 282, "v_dis_t": -209, "v_ina_t": 14, "inc_occ_c": 0.0, "inc_ina_c": 81.3, "inc_occ_t": -134.9, "inc_ina_t": 6.7},
    "Marzo 2025": {"occ": 24307, "dis": 1555, "ina": 12248, "t_occ": 63.0, "t_dis": 6.0, "t_ina": 32.9, "v_occ_c": -16, "v_dis_c": 32, "v_ina_c": -11, "v_occ_t": 450, "v_dis_t": -208, "v_ina_t": -107, "inc_occ_c": -50.0, "inc_ina_c": -34.4, "inc_occ_t": -216.3, "inc_ina_t": -51.4},
    "Febbraio 2025": {"occ": 24332, "dis": 1517, "ina": 12254, "t_occ": 63.0, "t_dis": 5.9, "t_ina": 32.9, "v_occ_c": 47, "v_dis_c": -79, "v_ina_c": 33, "v_occ_t": 567, "v_dis_t": -342, "v_ina_t": -60, "inc_occ_c": -59.5, "inc_ina_c": 41.8, "inc_occ_t": -165.8, "inc_ina_t": -17.5},
    "Gennaio 2025": {"occ": 24222, "dis": 1621, "ina": 12242, "t_occ": 62.8, "t_dis": 6.3, "t_ina": 32.9, "v_occ_c": 145, "v_dis_c": -9, "v_ina_c": -146, "v_occ_t": 513, "v_dis_t": -194, "v_ina_t": -158, "inc_occ_c": -1611.1, "inc_ina_c": -1622.2, "inc_occ_t": -264.4, "inc_ina_t": -81.4},
}

# --- 2. CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Analisi Istat 2025", layout="wide")
st.title("📊 Analisi Mercato del Lavoro 2025")

mese = st.selectbox("Seleziona il mese:", list(database_istat.keys()))
d = database_istat[mese]

# --- 3. ANALISI TESTUALE ---
with st.expander(f"📝 ANALISI DETTAGLIATA - {mese}", expanded=True):
    def color_val(val):
        c = "red" if val < 0 else "#00ff00"
        return f"<span style='color:{c}; font-weight:bold;'>{val:+} mila</span>"
    
    # Disoccupazione in nero grassetto
    dis_str = f"<span style='color:black; font-weight:bold;'>{d['v_dis_c']:+} mila</span>"

    st.markdown(f"""
    **TASSO OCCUPAZIONE:** {d['t_occ']}% | **DISOCCUPAZIONE:** {d['t_dis']}% | **INATTIVITÀ:** {d['t_ina']}%
    
    ---
    **VARIAZIONE MENSILE:** Occ {color_val(d['v_occ_c'])} | **Dis {dis_str}** | Ina {color_val(d['v_ina_c'])}
    * Incidenza Occ: **{d['inc_occ_c']}%** | Incidenza Ina: **{d['inc_ina_c']}%**
    """, unsafe_allow_html=True)

# --- 4. GRAFICI ---
c_occ, c_dis, c_ina = '#3498db', '#e74c3c', '#95a5a6' # Celeste, Rosso, Grigio

def plot_pie(occ_v, dis_v, ina_v, occ_i, ina_i, title):
    fig, ax = plt.subplots()
    vals = [abs(occ_v), abs(dis_v), abs(ina_v)]
    labs = [f"Occ ({occ_v}k)\nInc: {occ_i}%", f"Dis ({dis_v}k)", f"Ina ({ina_v}k)\nInc: {ina_i}%"]
    ax.pie(vals, labels=labs, colors=[c_occ, c_dis, c_ina], autopct='%1.1f%%', startangle=90, textprops={'fontweight':'bold'})
    ax.set_title(title, fontweight='bold')
    return fig

tab1, tab2 = st.tabs(["🔴 MENSILE", "🟡 ANNUALE"])
with tab1:
    st.pyplot(plot_pie(d['v_occ_c'], d['v_dis_c'], d['v_ina_c'], d['inc_occ_c'], d['inc_ina_c'], "ripartizione delle variazioni occupati e inattivi"))
with tab2:
    st.pyplot(plot_pie(d['v_occ_t'], d['v_dis_t'], d['v_ina_t'], d['inc_occ_t'], d['inc_ina_t'], "ripartizione delle variazioni occupati e inattivi"))
