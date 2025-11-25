import streamlit as st
import pandas as pd
import hashlib
import os
from streamlit_cookies_manager import EncryptedCookieManager

USERS_FILE = "users.csv"

# -------------------- Menedżer ciasteczek --------------------
cookies = EncryptedCookieManager(
    prefix="mood_app",
    password="supersecretpassword123!"
)

if not cookies.ready():
    st.stop()

# -------------------- Funkcje pomocnicze --------------------
def hash_password(pw: str) -> str:
    return hashlib.sha256(pw.encode()).hexdigest()

def load_users() -> pd.DataFrame:
    if not os.path.exists(USERS_FILE):
        pd.DataFrame(columns=["username", "password"]).to_csv(USERS_FILE, index=False)
    return pd.read_csv(USERS_FILE)

def save_user(username: str, password: str):
    df = load_users()
    df.loc[len(df)] = [username, hash_password(password)]
    df.to_csv(USERS_FILE, index=False)

# -------------------- Funkcje logowania --------------------
def is_logged_in() -> bool:
    if cookies.get("logged_in") == "True" and cookies.get("username"):
        st.session_state.logged_in = True
        st.session_state.username = cookies.get("username")
    return st.session_state.get("logged_in", False)

def logout():
    st.session_state.logged_in = False
    st.session_state.username = ""
    cookies["logged_in"] = "False"
    cookies["username"] = ""
    cookies.save()
    st.rerun()

# -------------------- Interfejs logowania/rejestracji --------------------
def login_view():
    st.markdown("<h1 style='text-align:center;'>💛 Wsparcie dla nastroju</h1>", unsafe_allow_html=True)
    st.subheader("Zaloguj się lub zarejestruj")

    users = load_users()

    mode = "Login" if st.session_state.get("just_registered", False) else st.radio("Menu", ["Login", "Rejestracja"])

    # -------------------- LOGIN --------------------
    if mode == "Login":
        username = st.text_input("Nazwa użytkownika")
        password = st.text_input("Hasło", type="password")

        if st.button("Zaloguj"):
            if username in users.username.values:
                stored_hash = users.loc[users.username == username, "password"].item()
                if hash_password(password) == stored_hash:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    cookies["logged_in"] = "True"
                    cookies["username"] = username
                    cookies.save()
                    st.rerun()  # brak komunikatu sukcesu
                else:
                    st.error("Błędne hasło")
            else:
                st.error("Nie ma takiego użytkownika")

    # -------------------- REJESTRACJA --------------------
    else:
        username = st.text_input("Wybierz nazwę użytkownika")
        password = st.text_input("Wybierz hasło", type="password")

        if st.button("Zarejestruj"):
            if username in users.username.values:
                st.error("Użytkownik już istnieje")
            else:
                save_user(username, password)
                st.session_state.just_registered = True
                st.rerun()
