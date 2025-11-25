import streamlit as st

# Baza playlist z polskimi kategoriami i spokojną muzyką
MUSIC_DB = {
    "Spokojna": [
        ("🌧️ Deszcz + Ambient", "https://www.youtube.com/watch?v=oP1BoA5IcfU"),
        ("🌙 Ambient do snu", "https://www.youtube.com/embed/1ZYbU82GVz4"),
        ("🎶 Lofi relaksacyjny", "https://www.youtube.com/embed/jfKfPfyJRdk"),
    ],
    "Radosna": [
        ("🌈 Delikatny pozytywny lofi", "https://www.youtube.com/embed/7NOSDKb0HlU"),
        ("😄 Radosny vibe", "https://www.youtube.com/watch?v=hlWiI4xVXKY"),
        ("✨ Pozytywny klasyczny vibe", "https://www.youtube.com/watch?v=6-1QnBtmc4k"),
    ],
    "Relaks": [
        ("🌅 Spokojny wieczór", "https://www.youtube.com/embed/2OEL4P1Rz04"),
        ("🍃 Delikatny ambient", "https://www.youtube.com/embed/-FlxM_0S2lA"),
        ("🎵 Instrumentalny spokój", "https://www.youtube.com/watch?v=O1RaSvzgV5o"),
    ]
}

def show_music():
    st.header("🎵 Muzyka dla Twojego nastroju")
    st.write("Wybierz kategorię muzyki, a ja znajdę coś dla Ciebie:")

    # --- Wybór kategorii ---
    if "music_mood" not in st.session_state:
        st.session_state.music_mood = list(MUSIC_DB.keys())[0]

    theme = st.session_state.get("theme", "dark")
    radio_container = st.container()

    with radio_container:
        mood = st.radio(
            "🎧 Wybierz kategorię",
            list(MUSIC_DB.keys()),
            index=list(MUSIC_DB.keys()).index(st.session_state.music_mood),
            key="music_mood",
            horizontal=True
        )



    # --- Zapamiętany aktualnie wybrany utwór ---
    if "selected_track" not in st.session_state:
        st.session_state.selected_track = None

    if mood:
        st.subheader("✨ Propozycje muzyki:")

        # Lista przycisków dla utworów
        for title, url in MUSIC_DB[mood]:
            if st.button(title):
                st.session_state.selected_track = url

        st.markdown("---")

        if st.session_state.selected_track:
            st.video(st.session_state.selected_track)
