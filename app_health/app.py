import streamlit as st
from auth import login_view, is_logged_in
from css import apply_theme
from menu import sidebar_menu

# Konfiguracja strony
st.set_page_config(
    page_title="Wsparcie dla nastroju",
    page_icon="💛",
    layout="wide"
)

apply_theme()

# Jeśli użytkownik nie jest zalogowany → pokaż ekran logowania
if not is_logged_in():
    login_view()
    st.stop()

sidebar_menu()
