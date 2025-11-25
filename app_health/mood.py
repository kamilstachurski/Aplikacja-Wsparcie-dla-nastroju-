import pandas as pd
import os
from datetime import datetime
import streamlit as st

def show_mood():
    moods = {
        "😞 Smutny": "😞",
        "😐 Neutralny": "😐",
        "🙂 Dobry": "🙂",
        "😄 Bardzo dobry": "😄"
    }

    selected = st.radio("Jak się czujesz?", list(moods.keys()), horizontal=True)
    note = st.text_area("Notatka:")

    if st.button("Zapisz"):

        if not note.strip():
            note = "(brak notatki)"

        filename = f"{st.session_state.username}_mood.csv"

        # jeśli plik nie istnieje → tworzymy pusty CSV
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            pd.DataFrame(columns=["Data", "Nastrój", "Notatka"]).to_csv(filename, index=False, encoding="utf-8")

        # --- BEZPIECZNE wczytanie CSV ---
        try:
            df = pd.read_csv(filename, encoding="utf-8")
        except pd.errors.EmptyDataError:
            df = pd.DataFrame(columns=["Data", "Nastrój", "Notatka"])

        today = datetime.now().date()

        if "Data" in df.columns and not df.empty:
            df["Data"] = pd.to_datetime(df["Data"])
            exists_today = df["Data"].dt.date == today
        else:
            exists_today = pd.Series([False] * len(df))

        emoticon = moods[selected]

        # nadpis dzisiejszego wpisu
        if exists_today.any():
            df.loc[exists_today, "Data"] = datetime.now()
            df.loc[exists_today, "Nastrój"] = emoticon
            df.loc[exists_today, "Notatka"] = note
        else:
            new_row = pd.DataFrame({
                "Data": [datetime.now()],
                "Nastrój": [emoticon],
                "Notatka": [note]
            })
            df = pd.concat([df, new_row], ignore_index=True)

        df.to_csv(filename, index=False, encoding="utf-8")
        st.success("✅ Zapisano!")