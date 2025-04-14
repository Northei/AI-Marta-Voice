import streamlit as st
from PIL import Image
import os

# ======= КОНСТАНТИ =========
CONFIG = {
    "button_start_text": "▶️ Почати розмову",
    "button_stop_text": "⏹ Завершити розмову",
    "column_proportions": [3, 2],
    "avatar_path": "marta_avatar.jpg"
}

# ======= НАЛАШТУВАННЯ СТОРІНКИ =========
st.set_page_config(
    page_title="Марта — Класика без відступів",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ======= СТИЛІ =========
css_styles = """
<style>
html, body {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    overflow: hidden;
}
/* Загальні змінні */
:root {
    --bg-color: rgb(217, 217, 217); /* Фон сторінки - світлий */
    --text-color: #212529;
    --button-bg: rgb(178, 178, 178); /* Фон колонок - темніший */
    --button-start-bg: rgb(167, 167, 167); /* Фон кнопки Почати - темно-сірий */
    --button-stop-bg: rgb(150, 200, 120); /* Фон кнопки Завершити - зелений */
    --border-radius: 8px;
    --column-gap: 0.5rem;
}

/* Глобальні стилі */
body {
    background-color: var(--bg-color);
    color: var(--text-color);
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

/* Контейнер для колонок */
.main > div {
    padding: 0 !important;
}
[data-testid="column"] {
    padding: 0.5rem;
    background-color: var(--button-bg);
    border-radius: var(--border-radius);
}

/* Ліва колонка */
[data-testid="column"]:first-child {
    width: 60%;
}

/* Права колонка */
[data-testid="column"]:last-child {
    width: 40%;
}

/* Кнопки */
.stButton > button {
    width: 100%;
    font-size: 18px;
    padding: 0.75em;
    border-radius: var(--border-radius);
    display: block;
    margin: 0 auto;
}
.stButton > button[key="start_button"] {
    background-color: var(--button-start-bg) !important;
}
.stButton > button[key="stop_button"] {
    background-color: var(--button-stop-bg) !important;
}

/* Блоки */
.block-container {
    padding-top: 2rem;
}

/* Горизонтальні блоки */
[data-testid="stHorizontalBlock"] > div {
    background-color: var(--button-bg);
    padding: 0.5rem;
    border-radius: 1px;
}
</style>
"""
st.markdown(css_styles, unsafe_allow_html=True)

# ======= УТИЛІТИ =========
def load_image(image_path):
    """Завантажує зображення або повертає None, якщо файл не знайдено."""
    if os.path.exists(image_path):
        return image_path
    else:
        st.warning(f"Файл '{image_path}' не знайдено.")
        return None

# ======= РОЗМІТКА =========
if "conversation_active" not in st.session_state:
    st.session_state.conversation_active = False

main_left, main_right = st.columns(CONFIG["column_proportions"], gap="small")

with main_right:
    st.markdown("### ШІ Асистент Марта")
    avatar_image = load_image(CONFIG["avatar_path"])
    if avatar_image:
        st.image(avatar_image, use_container_width=True)
    
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if not st.session_state.conversation_active:
        if st.button(CONFIG["button_start_text"], key="start_button"):
            st.session_state.conversation_active = True
            st.rerun()
    else:
        if st.button(CONFIG["button_stop_text"], key="stop_button"):
            st.session_state.conversation_active = False
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.info("Марта слухає і готова до роботи!")

with main_left:
    st.markdown("### Робоча область")
    st.markdown("Тут буде інформація, відповіді GPT, таблиці тощо.")