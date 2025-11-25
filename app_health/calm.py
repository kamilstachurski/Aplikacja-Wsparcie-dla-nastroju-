import streamlit as st


def show_calm():
    st.header("🔔 Techniki spokoju")

    st.write("### Metoda 5-4-3-2-1")
    st.info("""
    • 5 rzeczy które widzisz  
    • 4 rzeczy które możesz dotknąć  
    • 3 rzeczy które słyszysz  
    • 2 rzeczy które możesz powąchać  
    • 1 rzecz którą możesz posmakować
    """)

    st.write("### Szybkie wskazówki")
    st.success("Zrób przerwę. Wstań, przeciągnij się. To w porządku nic nie robić przez chwilę.")
