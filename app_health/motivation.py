import streamlit as st
import random

quotes = [
    "Nigdy się nie poddawaj — wielkie rzeczy wymagają czasu.",
    "Każdy dzień jest nową szansą, aby zacząć od nowa.",
    "Jesteś silniejszy, niż ci się wydaje.",
    "Rób małe kroki, ale codziennie.",
    "Twoje myśli tworzą Twoją rzeczywistość.",
    "Zadbaj dziś o siebie — jutro Ci za to podziękujesz.",
    "To w porażkach kryje się siła, która pozwala wzrastać.",
    "Nie musisz radzić sobie ze wszystkim sam.",
    "Każdy krok naprzód jest sukcesem, nawet jeśli wydaje się mały.",
    "Nie oceniaj siebie za to, że masz gorsze dni.",
    "Czasami najodważniejszym krokiem jest po prostu iść dalej.",
    "Każdy dzień niesie ze sobą nową możliwość.",
    "Daj sobie pozwolenie na odpoczynek i regenerację.",
    "Nie trać nadziei, nawet gdy wszystko wydaje się trudne.",
    "Twoje uczucia są ważne i zasługują na uwagę.",
    "Małe postępy też są warte docenienia.",
    "Nie porównuj się do innych – idź własną drogą.",
    "Uśmiech, nawet mały, może zmienić Twój dzień.",
    "Bądź dla siebie przyjacielem, którego potrzebujesz.",
    "To, co robisz dzisiaj, może poprawić wszystkie Twoje jutra.",
    "Nie musisz być doskonały, aby być wartościowy.",
    "Cisza i spokój pozwalają znaleźć wewnętrzną równowagę.",
    "Twoja wartość nie zależy od tego, jak się dzisiaj czujesz.",
    "Każdy nowy dzień niesie ze sobą możliwość zmiany.",
    "Nie jesteś zdefiniowany przez swoje gorsze dni.",
    "To, że dzisiaj jest ciężko, nie oznacza, że jutro nie może być lepsze.",
    "Wdzięczność nawet za drobne rzeczy potrafi zmienić perspektywę.",
    "Nie bój się prosić o pomoc, kiedy jej potrzebujesz.",
    "Każdy ma prawo do odpoczynku i troski o siebie.",
    "To w trudnych chwilach odkrywamy swoją siłę i wytrwałość.",
    "Nie wszystko zależy od Ciebie – czasem wystarczy po prostu przetrwać."
]

def show_motivation():
    st.header("🌞 Motywacja dnia")


    if "daily_quote" not in st.session_state:
        st.session_state.daily_quote = random.choice(quotes)

    st.success(st.session_state.daily_quote)

    if st.button("🔄 Wylosuj nową inspirację"):
        st.session_state.daily_quote = random.choice(quotes)
        st.rerun()
