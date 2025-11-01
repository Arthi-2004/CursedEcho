import streamlit as st
import random
import time
import base64
from responses import get_ai_response

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Cursed Echo 👁️", page_icon="💀", layout="centered")

# ---------- CUSTOM STYLE ----------
st.markdown("""
<style>
body {
    background-color: #000;
    color: #e0e0e0;
    font-family: 'Courier New', monospace;
}
.stTextInput > div > div > input {
    background-color: #0d0d0d;
    color: #ff5555;
    border: 1px solid #222;
    box-shadow: 0 0 10px #ff000020;
}
h1 {
    color: #ff2b2b;
    text-align: center;
    text-shadow: 0 0 15px #ff0000;
}
.whisper {
    color: #a00000;
    font-style: italic;
    text-align: center;
    font-size: 1.1rem;
    text-shadow: 0 0 10px #ff000040;
    transition: all 0.3s ease-in-out;
}
.flicker {
    animation: flicker 0.12s infinite alternate;
}
@keyframes flicker {
    0% { background-color: #000; }
    50% { background-color: #111; }
    100% { background-color: #000; }
}
</style>
""", unsafe_allow_html=True)

# ---------- AUDIO PLAY ----------
def play_audio(file_path, loop=True):
    """Embed and autoplay audio."""
    with open(file_path, "rb") as f:
        audio_bytes = f.read()
    audio_base64 = base64.b64encode(audio_bytes).decode()
    loop_attr = "loop" if loop else ""
    st.markdown(
        f"""
        <audio autoplay {loop_attr}>
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )

# ---------- SESSION STATE ----------
if "messages" not in st.session_state:
    st.session_state.messages = []
if "triggered" not in st.session_state:
    st.session_state.triggered = False
if "music_played" not in st.session_state:
    st.session_state.music_played = False
if "temp_input" not in st.session_state:
    st.session_state.temp_input = ""  # safe variable

# ---------- TITLE ----------
st.title("👁️ Cursed Echo")
st.markdown("<p style='text-align:center;'>Whisper into the void... it whispers back.</p>", unsafe_allow_html=True)

# ---------- CHAT PLACEHOLDER ----------
placeholder = st.empty()

# ---------- INPUT HANDLER ----------
def handle_input():
    user_text = st.session_state.temp_input.strip()
    if not user_text:
        return

    # Append user message
    st.session_state.messages.append({"role": "user", "text": user_text})

    # Pause for effect
    with st.spinner("The void listens..."):
        time.sleep(1.2)

    # Get AI response
    response = get_ai_response(user_text)
    st.session_state.messages.append({"role": "bot", "text": response})

    # Detect trigger words / time to turn creepy
    dark_words = ["blood", "dark", "death", "fear", "alone", "shadow", "night", "curse", "whisper"]
    if len(st.session_state.messages) > 4 or any(word in user_text.lower() for word in dark_words):
        st.session_state.triggered = True

    # Clear input safely
    st.session_state.temp_input = ""

# ---------- CHAT INPUT ----------
st.text_input("💬 Speak your words (if you dare)...", key="temp_input", on_change=handle_input)

# ---------- DISPLAY MESSAGES ----------
chat_html = "<div>"
for msg in st.session_state.messages:
    if msg["role"] == "user":
        chat_html += f"<p style='text-align:right;color:#aaa;'>> {msg['text']}</p>"
    else:
        chat_html += f"<p class='whisper'>👁️ {msg['text']}</p>"
chat_html += "</div>"

# ---------- TRIGGER EFFECT ----------
if st.session_state.triggered:
    chat_html = f"<div class='flicker'>{chat_html}</div>"

    # Play creepy audio once
    if not st.session_state.music_played:
        play_audio("assets/scary-horror-creepy-music-371663.mp3", loop=True)
        time.sleep(1)
        play_audio("assets/ghost-whispers-6030.mp3", loop=False)
        st.session_state.music_played = True

placeholder.markdown(chat_html, unsafe_allow_html=True)
