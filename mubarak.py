import streamlit as st
import random

st.set_page_config(page_title="Eid Mubarak", page_icon="🎉")

st.title("✨ Assalamualaikum ✨")
st.write("Click the button to receive a special Eid blessing!")

blessings = [
    "May this Eid bring happiness and peace to your life. 🌸",
    "Wishing you a blessed and joyous Eid! 🎉",
    "May Allah accept your prayers and grant you prosperity. 🤲",
    "Eid Mubarak! May your home be filled with joy and laughter. 💖",
    "Wishing you and your family health, wealth, and happiness. 💕",
    "May this Eid be a new beginning of greater prosperity. ✨",
    "Allah bless you with endless moments of joy and success. 😊",
    "May your faith be strengthened and your heart filled with peace. 🙏",
    "Eid Mubarak! Stay blessed and enjoy the festivities. 🎊",
    "May all your prayers be answered this Eid and always. 🌟"
]

if st.button("Click Here"):  
    random_blessing = random.choice(blessings)
    st.markdown(f"""
    <h2 style='text-align: center; color: gold;'>
        🎉 Eid Mubarak to You from FAIZEE! 🎉
    </h2>
    <p style='text-align: center; font-size: 20px; color: black;'>
        {random_blessing}
    </p>
    """, unsafe_allow_html=True)
    
    st.balloons()
