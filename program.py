import random
import streamlit as st

st.title("🎲 Random Number Guessing Game")
st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

# session state to store game data
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.max_attempts = 10

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
if st.button("Submit Guess"):
    st.session_state.attempts += 1

    if guess < st.session_state.secret_number:
        st.warning("❌ Too low!")
    elif guess > st.session_state.secret_number:
        st.warning("❌ Too high!")
    else:
        st.success(f"🎉 Congrats! You guessed it in {st.session_state.attempts} attempts.")
        if st.button("Play Again"):
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = 0

    if st.session_state.attempts >= st.session_state.max_attempts and guess != st.session_state.secret_number:
        st.error(f"😢 Out of attempts! The correct number was {st.session_state.secret_number}.")
        if st.button("Try Again"):
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = 0
