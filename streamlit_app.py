import streamlit as st
import random
from google import genai
from google.genai import types

# Настройка страницы под игровой стиль
st.set_page_config(page_title="Чит-код ХАБ", page_icon="🎒", layout="centered")

# --- 1. ПОДКЛЮЧЕНИЕ НАСТОЯЩЕГО ИИ GEMINI ---
# Замени эту строчку на свой секретный ключ из Google AI Studio (://google.com)
API_KEY = "ТВОЙ_КЛЮЧ_СЮДА" 

@st.cache_resource
def init_ai():
    if API_KEY == "ТВОЙ_КЛЮЧ_СЮДА":
        return None
    # Инициализируем официальный клиент Google GenAI
    return genai.Client(api_key=API_KEY)

client = init_ai()

# Жесткая инструкция (Системный промпт), которая заставляет ИИ быть мемным репетитором
SYSTEM_INSTRUCTION = """
Ты — продвинутый ИИ-репетитор для школьников 5-11 классов по имени "Чит-код". 
Твоя цель — объяснять любые школьные предметы (математику, русский, историю, биологию и др.) простым языком, используя актуальный молодежный сленг и мемы. 
Используй слова: 'сигма', 'босс КФС', 'кринж', 'вайб', 'рил', 'тапать', 'база', 'проветриться', 'флексить', 'скибиди' (редко и уместно), примеры из игр (Minecraft, Roblox, Dota 2, Brawl Stars).
Отвечай коротко, емко, без скучных длинных текстов, разбивай мысли на абзацы с эмодзи. Школьники ленивые, длинный текст читать не будут.
Пользователь может использовать команды /Математика, /Русский, /История — подстраивайся под нужный предмет.
"""

# --- 2. СИСТЕМА АВТОРИЗАЦИИ (Всплывающее окно) ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "player_name" not in st.session_state:
    st.session_state.player_name = ""

@st.dialog("🔐 ВХОД В ЧИТ-КОД")
def login_dialog():
    st.write("Добро пожаловать, босс! Придумай ник для Лиги Сигм.")
    input_name = st.text_input("Введи свой никнейм:", placeholder="Например: Sigma_Brawl")
    
    if st.button("🚀 СОЗДАТЬ АККАУНТ", use_container_width=True):
        if input_name.strip() != "":
            st.session_state.player_name = input_name
            st.session_state.logged_in = True
            st.toast(f"Активирован аккаунт: {input_name}! ⚡", icon="✅")
            st.rerun()
        else:
            st.error("Ник не может быть пустым!")

# Принудительный вход при первом открытии сайта
if not st.session_state.logged_in:
    login_dialog()
    st.warning("Авторизуйся, чтобы спасти свой прогресс IQ!")
    st.stop()

# --- 3. ПАМЯТЬ ИГРЫ (После авторизации) ---
if "iq" not in st.session_state:
    st.session_state.iq = 100  # Все начинают со 100 IQ
if "box_stage" not in st.session_state:
    st.session_state.box_stage = "closed"
if "items_left" not in st.session_state:
    st.session_state.items_left = 0
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

# Динамическая система корпусов вместо обычных лиг
def get_school_building(iq):
    if iq < 120: return "🏢 КОРПУС 'Г' (Хозблок новичков) ❌"
    elif iq < 150: return "🏢 КОРПУС 'В' (Обычное крыло) 跑"
    elif iq < 200: return "🏢 КОРПУС 'Б' (Крыло отличников) ⭐"
    else: return "🏛️ КОРПУС 'А' (ГЛАВНОЕ ЗДАНИЕ СИГМ) 👑"

# --- 4. БОКОВОЕ МЕНЮ (Твой левый блок хаба) ---
st.sidebar.title(f"🎒 ЧИТ-КОД ХАБ")
st.sidebar.markdown(f"👤 Ник: **{st.session_state.player_name}**")
st.sidebar.markdown(f"🧠 Рейтинг: **{st.session_state.iq} IQ**")
st.sidebar.markdown(f"🏰 Твой статус: \n`{get_school_building(st.session_state.iq)}`")
st.sidebar.markdown("---")

# Переключатель режимов
mode = st.sidebar.radio("Выбери режим:", ["💬 1. Настоящий ИИ-Помощник", "🎰 2. Мегаящик за IQ"])

st.sidebar.markdown("---")
if st.sidebar.button("👑 VIP ПОДПИСКА (199₽)", use_container_width=True):
    st.sidebar.info("Форма оплаты СБП генерируется... (После 6 марта)")

# --- 5. РАБОТА ИГРОВЫХ РЕЖИМОВ ---

# Режим 1: Живой ИИ-Чат
if mode == "💬 1. Настоящий ИИ-Помощник":
    st.title("💬 Настоящий ИИ-Помощник")
    st.write("Задавай любые вопросы по домашке! Используй `/Предмет` в начале для точности.")
    st.markdown("---")
    
    # Отображаем историю чата
    for msg in st.session_state.chat_messages:
        with st.chat_message(msg["role"]):
            st.write(msg["text"])
            
    # Поле ввода сообщений
    if user_input := st.chat_input("Напиши: /Математика что такое дроби"):
        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.chat_messages.append({"role": "user", "text": user_input})
        
        # Запрос к живому ИИ Gemini
        with st.chat_message("assistant"):
            if client is None:
                ai_reply = "❌ Ошибка: Ты забыл вставить настоящий API_KEY в код! Замени строчку 'ТВОЙ_КЛЮЧ_СЮДА' на реальный ключ из Google AI Studio."
                st.write(ai_reply)
            else:
                with st.spinner("ИИ разгоняет мозг..."):
                    try:
                        # Отправляем запрос модели gemini-2.5-flash с нашей инструкцией сленга
                        response = client.models.generate_content(
                            model='gemini-2.5-flash',
                            contents=user_input,
                            config=types.GenerateContentConfig(
                                system_instruction=SYSTEM_INSTRUCTION,
                                temperature=0.7
                            )
                        )
                        ai_reply = response.text
                        st.write(ai_reply)
                        st.session_state.iq += 2  # Даем +2 IQ за то, что школьник просто учится!
                    except Exception as e:
                        ai_reply = f"💥 Что-то пошло не так при запросе к ИИ: {e}"
                        st.write(ai_reply)
                        
        st.session_state.chat_messages.append({"role": "assistant", "text": ai_reply})
        st.rerun()

# Режим 2: Открытие Мегаящиков за IQ
elif mode == "🎰 2. Мегаящик за IQ":
    st.title("🎰 СИМУЛЯТОР МЕГАЯЩИКА")
    st.write("Рискни интеллектом ради крутого дропа! Стоимость открытия: **20 IQ**.")
    
    if st.session_state.box_stage == "closed":
        # Рисуем ящик из эмодзи-аарта
        megabox_art = "🟪🟪🟪🟪🟪\n🟪🟥🟨🟥🟪\n🟪🟥🟨🟥🟪\n🟪🟪🟪🟪🟪"
        st.markdown(f"<pre style='font-size: 20px; line-height: 1.2; text-align: center;'>{megabox_art}</pre>", unsafe_allow_html=True)
        
        if st.button("🚀 ОТКРЫТЬ ЯЩИК ЗА 20 IQ 🚀", use_container_width=True):
            if st.session_state.iq >= 100:  # Не даем упасть ниже несгораемых 80 IQ после траты 20 баллов
                st.session_state.iq -= 20
                st.session_state.items_left = 3
                st.session_state.box_stage = "opening"
                st.rerun()
            else:
                st.error("❌ Слишком низкий IQ! Корпус 'Г' запрещает тратить баллы. Иди качай мозги в чат!")
                
    elif st.session_state.box_stage == "opening":
        st.markdown(f"<h3 style='text-align: center; color: yellow;'>⚡ Осталось кликов: {st.session_state.items_left} ⚡</h3>", unsafe_allow_html=True)
        if st.button("👉 ТАПНИ ПО ЯЩИКУ! 👈", use_container_width=True):
            if st.session_state.items_left > 1:
                st.toast("Выпало: +50 очков силы 🔋", icon="🎁")
                st.session_state.items_left -= 1
                st.rerun()
            else:
                st.session_state.box_stage = "drop"
                st.rerun()
                
    elif st.session_state.box_stage == "drop":
        st.balloons() # Салют на весь экран!
        skins = ["👑 Скин: 'Гигачад-Ломоносов'", "🌌 Тема чата: 'Неоновый Скибиди'", "🔥 Огненный Никнейм"]
        st.success(f"🎉 ТЕБЕ ВЫПАЛО: {random.choice(skins)}!")
        if st.button("Забрать в инвентарь", use_container_width=True):
            st.session_state.box_stage = "closed"
            st.rerun()
