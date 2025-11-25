import streamlit as st
from auth import logout
from mood import show_mood
from history import show_history
from motivation import show_motivation
from relax import show_relax
from calm import show_calm
from help import show_help
from css import apply_theme
from music import show_music
def sidebar_menu():

    if "theme" not in st.session_state:
        st.session_state.theme = "dark"  # domyślny ciemny motyw

    if "username" not in st.session_state:
        st.session_state.username = ""

    st.sidebar.header(f"👋 Witaj, {st.session_state.username}!")
    if st.sidebar.button("🌗 Zmień tryb"):
        st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

    # --- CSS ---
    apply_theme()

    # --- menu nawigacyjne ---
    menu = st.sidebar.radio(
        "📌 Nawigacja",
        ["📝 Dziennik", "📈 Historia", "🌞 Motywacja", "🧘 Odpoczynek", "🔔 Spokój", "📞 Pomoc", "🎵 Muzyka"]
    )

    # --- przycisk wylogowania ---
    if st.sidebar.button("🚪 Wyloguj"):
        logout()

    # --- wyświetlenie sekcji ---
    if menu == "📝 Dziennik":
        show_mood()
    elif menu == "📈 Historia":
        show_history()
    elif menu == "🌞 Motywacja":
        show_motivation()
    elif menu == "🧘 Odpoczynek":
        show_relax()
    elif menu == "🔔 Spokój":
        show_calm()
    elif menu == "📞 Pomoc":
        show_help()
    elif menu == "🎵 Muzyka":
        show_music()
