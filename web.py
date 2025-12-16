import random
import streamlit as st

# Page setup
st.set_page_config(page_title="🎲 Random Number Game", page_icon="🎮", layout="centered")
st.title("🎲 Random Number Guessing Game")
st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

# Session state for game
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.max_attempts = 10
    st.session_state.bg_color = "white"

# Background color
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {st.session_state.bg_color};
    }}
    </style>
""", unsafe_allow_html=True)

# User input
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    st.session_state.attempts += 1

    if guess < st.session_state.secret_number:
        st.warning("❌ Too low!")
        st.session_state.bg_color = "#FFFACD"  # Light Yellow
    elif guess > st.session_state.secret_number:
        st.warning("❌ Too high!")
        st.session_state.bg_color = "#FFB6C1"  # Light Pink
    else:
        st.success(f"🎉 Congrats! You guessed it in {st.session_state.attempts} attempts.")
        st.session_state.bg_color = "#90EE90"  # Light Green

    if st.session_state.attempts < st.session_state.max_attempts and guess != st.session_state.secret_number:
        st.info(f"🔁 Attempts left: {st.session_state.max_attempts - st.session_state.attempts}")
    elif st.session_state.attempts >= st.session_state.max_attempts and guess != st.session_state.secret_number:
        st.error(f"😢 Out of attempts! The correct number was {st.session_state.secret_number}.")

# Reset / Replay
# Reset / Replay
if st.button("Play Again"):
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.bg_color = "white"
    st.rerun()   # ✅ Use this instead of st.experimental_rerun()
