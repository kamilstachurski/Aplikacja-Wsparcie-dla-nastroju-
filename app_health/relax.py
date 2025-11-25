import streamlit as st
import time


def show_relax():
    st.header("🧘 Ćwiczenia relaksacyjne")

    st.subheader("1. Oddychanie 4-4-6")

    if st.button("Rozpocznij ćwiczenie"):
        st.write("Oddychaj zgodnie z instrukcją:")

        for i in range(1, 4):
            st.write(f"🌬️ Wdech (4 sekundy) — cykl {i}")
            time.sleep(4)
            st.write("⏸️ Zatrzymaj (4 sekundy)")
            time.sleep(4)
            st.write("😌 Wydech powoli (6 sekund)")
            time.sleep(6)

        st.success("Ćwiczenie zakończone!")

    st.markdown("---")

    st.subheader("2. Relaks mięśni")
    st.info("Zaciskaj i rozluźniaj po kolei dłonie, ramiona, kark, nogi.")
