import streamlit as st
import datetime

st.title("📅 Simple Calendar")

# Date picker
selected_date = st.date_input("Pick a date", datetime.date.today())

# Show selected date
st.write(f"You selected: **{selected_date.strftime('%A, %B %d, %Y')}**")
