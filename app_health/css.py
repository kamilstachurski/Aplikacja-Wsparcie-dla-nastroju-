import streamlit as st

def apply_theme():
    theme = st.session_state.get("theme", "dark")

    if theme == "dark":
        css = """
        <style>

        /* OGÓLNY CIEMNY */
        body, .stApp {
            background-color: #0F0F12 !important;
            color: #F0F0F0 !important;
        }
        * {
            color: #F0F0F0 !important;
        }

        /* SIDEBAR */
        [data-testid="stSidebar"] {
            background-color: #16161A !important;
            border-right: 1px solid #2A2A2E;
        }

        /* CIEMNY — HAMBURGER */
        button[kind="header"] svg path {
            stroke: #fff !important;
        }

        /* PRZYCISKI - CIEMNY */
        .stButton > button {
            background: linear-gradient(135deg, #2A2A2E, #34343A) !important;
            color: #fff !important;
            border: 1px solid #3E3E44 !important;
            border-radius: 10px !important;
            padding: 0.6rem 1rem !important;
            transition: 0.15s ease-in-out !important;
        }

        .stButton > button:hover {
            border-color: #6A6AF4 !important;
            box-shadow: 0 0 10px #6A6AF466 !important;
            background: linear-gradient(135deg, #2A2A2E, #3A3A40) !important;
        }



        /* tło strzałki w trybie ciemnym */
        div[data-testid="collapsedControl"] {
            background: #16161A !important;
            border-radius: 6px !important;
            padding: 4px !important;
            border: 1px solid #2A2A2E !important;
        }

        /* ikona strzałki — jasna */
        div[data-testid="collapsedControl"] button svg path,
        div[data-testid="collapsedControl"] svg path {
            stroke: #FFFFFF !important;
            fill: #FFFFFF !important;
        }
        /* ===== TOOLBAR W  CIEMNYM TRYBIE ===== */
        div[data-testid="stToolbar"] {
            background-color: #0F0F12 !important;
            border-bottom: 1px solid #2A2A2E !important;
        }

        div[data-testid="stToolbar"] * {
            color: #FFFFFF !important;
            fill: #FFFFFF !important;
            stroke: #FFFFFF !important;
        }



        </style>
        """

    else:
        css = """
        <style>

        /* ===== OGÓLNY JASNY ===== */
        body, .stApp {
            background-color: #F5F6F8 !important;
            color: #222 !important;
        }
        * {
            color: #222 !important;
        }
        

        /* SIDEBAR JASNY */
        [data-testid="stSidebar"] {
            background-color: #FFFFFF !important;
            border-right: 1px solid #DDDDDD;
        }

        /* JASNY — HAMBURGER (IKONA) */
        button[kind="header"] svg path {
            stroke: #222 !important;
        }

        /* JASNY PRZYCISKI */
        .stButton > button {
            background: #EFEFF5 !important;
            color: #222 !important;
            border: 1px solid #CFCFD9 !important;
            border-radius: 10px !important;
            transition: 0.15s ease-in-out !important;
        }

        .stButton > button:hover {
            background: #E2E2EC !important;
            border-color: #B5B5C6 !important;
        }

        div[data-testid="collapsedControl"] {
            background: #FFFFFF !important;
            border-radius: 6px !important;
            padding: 4px !important;
            border: 1px solid #DDD !important;
        }

        div[data-testid="collapsedControl"] button svg path,
        div[data-testid="collapsedControl"] svg path {
            stroke: #222 !important;
            fill: #222 !important;
        }

        header[data-testid="stHeader"] {
            background-color: #FFFFFF !important;
            color: #222 !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }

        header[data-testid="stHeader"] * {
            color: #222 !important;
            fill: #222 !important;
            stroke: #222 !important;
        }

        div[data-testid="stToolbar"] {
            background-color: #FFFFFF !important;
            border-bottom: 1px solid #DDDDDD !important;
        }

        div[data-testid="stToolbar"] * {
            color: #222 !important;
            fill: #222 !important;
            stroke: #222 !important;
        }

        .stTextInput input, div[data-baseweb="input"] input {
            color: #FFFFFF !important;
        }

        textarea {
            color: #FFFFFF !important;  /* tekst wpisywany będzie biały */
            background-color: #222222 !important; /* opcjonalnie tło, żeby kontrast był OK */
        }

        div.stSelectbox div[role="listbox"] {
        color: white !important;
        }


        </style>
        """

    st.markdown(css, unsafe_allow_html=True)
