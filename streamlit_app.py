import streamlit as st

st.set_page_config(page_title="CheatCode: Arena", page_icon="👾", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0E1117; color: #00FF66; font-family: 'Courier New', monospace; }
    h1, h2, h3 { color: #00FF66; text-shadow: 0 0 10px #00FF66; }
    .stButton>button { background-color: #1F2937; color: #00FF66; border: 2px solid #00FF66; box-shadow: 0 0 10px #00FF66; width: 100%; }
    .stButton>button:hover { background-color: #00FF66; color: #0E1117; }
    </style>
""", unsafe_allow_html=True)

st.title("👾 CheatCode: Arena — ИИ-Империя Босса")
st.write("---")

st.sidebar.header("👑 Профиль Лидера")
st.sidebar.success("Статус: В Сети (Stealth Mode)")
st.sidebar.info("Stamina: 100% | XP: 9,999")

tab1, tab2 = st.tabs(["⚔️ Кибер-Дуэли Метавидения", "🔊 Голос ИИ-Валеры"])

with tab1:
    st.header("Раунд 1: Стычка у РФЛ против Жирного")
    st.write("Ситуация: Жирный стягивает на твой хитбокс трёх защитников и бегает с ворованным мячом ЧМ-2026. Твой брат кричит 'Шик!' на фланге. Твои действия?")
    
    choice = st.radio("Выбери тактический промпт:", [
        "А) Слепо пойти на таран корпусом бокса",
        "Б) Включить Метавидение, подстроиться под хаос брата и выдать убойный пас пяткой",
        "В) Уйти пешком с поля за лимонадом за 32 рублей"
    ])
    
    if st.button("Выполнить маневр"):
        if "Б" in choice:
            st.balloons()
            st.success("🔥 СЧЁТ 10:0! Идеальный перехват Итоши Рина! Защита Жирного уничтожена всухую, мяч в сетке!")
        else:
            st.error("💥 SYSTEM CRASH! Твой хитбокс улетел в текстуры, Stamina слита в ноль. Перезагрузи процессор!")

with tab2:
    st.header("🔊 Пакет Аудио-Вещания")
    st.write("Запускай угарный голос Валеры прямо на ходу со своего Айфона!")
    st.audio("https://soundhelix.com")

st.write("---")
st.caption("© 2026 CheatCode Corporation. Базы данных запечатаны. Пятидневный ультиматум тикает.")
import streamlit as st

st.set_page_config(page_title="CheatCode: Arena", page_icon="👾", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0E1117; color: #00FF66; font-family: 'Courier New', monospace; }
    h1, h2, h3 { color: #00FF66; text-shadow: 0 0 10px #00FF66; }
    .stButton>button { background-color: #1F2937; color: #00FF66; border: 2px solid #00FF66; box-shadow: 0 0 10px #00FF66; width: 100%; }
    .stButton>button:hover { background-color: #00FF66; color: #0E1117; }
    </style>
""", unsafe_allow_html=True)

st.title("👾 CheatCode: Arena — ИИ-Империя Босса")
st.write("---")

st.sidebar.header("👑 Профиль Лидера")
st.sidebar.success("Статус: В Сети (Stealth Mode)")
st.sidebar.info("Stamina: 100% | XP: 9,999")

tab1, tab2 = st.tabs(["⚔️ Кибер-Дуэли Метавидения", "🔊 Голос ИИ-Валеры"])

with tab1:
    st.header("Раунд 1: Стычка у РФЛ против Жирного")
    st.write("Ситуация: Жирный стягивает на твой хитбокс трёх защитников и бегает с ворованным мячом ЧМ-2026. Твой брат кричит 'Шик!' на фланге. Твои действия?")
    
    choice = st.radio("Выбери тактический промпт:", [
        "А) Слепо пойти на таран корпусом бокса",
        "Б) Включить Метавидение, подстроиться под хаос брата и выдать убойный пас пяткой",
        "В) Уйти пешком с поля за лимонадом за 32 рублей"
    ])
    
    if st.button("Выполнить маневр"):
        if "Б" in choice:
            st.balloons()
            st.success("🔥 СЧЁТ 10:0! Идеальный перехват Итоши Рина! Защита Жирного уничтожена всухую, мяч в сетке!")
        else:
            st.error("💥 SYSTEM CRASH! Твой хитбокс улетел в текстуры, Stamina слита в ноль. Перезагрузи процессор!")

with tab2:
    st.header("🔊 Пакет Аудио-Вещания")
    st.write("Запускай угарный голос Валеры прямо на ходу со своего Айфона!")
    st.audio("https://soundhelix.com")

st.write("---")
st.caption("© 2026 CheatCode Corporation. Базы данных запечатаны. Пятидневный ультиматум тикает.")
