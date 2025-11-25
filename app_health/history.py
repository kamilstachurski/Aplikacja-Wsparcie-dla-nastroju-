import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

if "username" not in st.session_state:
    st.session_state.username = ""


def show_history():
    st.header("📈 Historia nastroju")

    file_name = f"{st.session_state.username}_mood.csv"

    # brak pliku lub pusty plik
    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        try:
            pd.DataFrame(columns=["Data", "Nastrój", "Notatka"]).to_csv(file_name, index=False, encoding="utf-8")
        except PermissionError:
            st.error(f"Nie mogę zapisać pliku {file_name}. Zamknij go w innym programie lub sprawdź uprawnienia.")
            return
        st.info("Brak zapisanych wpisów — dodaj swój pierwszy 😊")
        return

    # --- wczytanie pliku z obsługą pustych danych i kodowania ---
    try:
        df = pd.read_csv(file_name, encoding="utf-8")
    except pd.errors.EmptyDataError:
        df = pd.DataFrame(columns=["Data", "Nastrój", "Notatka"])
        st.info("Brak danych — dodaj swój pierwszy wpis 😊")
        return
    except UnicodeDecodeError:
        st.error("Błąd odczytu pliku – sprawdź kodowanie CSV (powinno być UTF-8).")
        return

    if df.empty:
        st.info("Brak danych — wypełnij pierwszy wpis 😊")
        return

    # konwersja daty i sortowanie
    if "Data" in df.columns:
        df["Data"] = pd.to_datetime(df["Data"], errors="coerce")
        df = df.sort_values("Data")
    else:
        st.error("Brak kolumny 'Data' — sprawdź format pliku!")
        return

    # wyświetlanie tabeli z ostatnimi wpisami — tylko wybrane kolumny
    st.write("### Ostatnie wpisy")
    st.dataframe(df.tail(10)[["Data", "Nastrój", "Notatka"]], use_container_width=True)

    mood_map = {
        "😞": 1,
        "😐": 5,
        "🙂": 7,
        "😄": 10
    }

    # konwersja emotek na liczby (tylko do wykresu)
    df["MoodValue"] = df["Nastrój"].map(mood_map)

    st.write("### 📉 Zmiany nastroju w czasie")

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(
        df["Data"],
        df["MoodValue"],
        linewidth=2,
        marker="o",
        markersize=7
    )

    # ustawienie stałej osi Y od 1 do 10, wartości całkowite
    ax.set_ylim(1, 10)
    ax.set_yticks(range(0, 12))

    # ustawienie polskiego formatu daty na osi X
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d.%m.%Y"))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())

    ax.set_xlabel("Data", fontsize=12)
    ax.set_ylabel("Poziom nastroju", fontsize=12)
    ax.grid(True, alpha=0.3)

    plt.xticks(rotation=45)
    st.pyplot(fig)
