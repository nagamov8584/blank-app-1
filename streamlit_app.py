import streamlit as st
import time
from datetime import datetime
import os

st.title("Day progress")

os.environ['TZ'] = 'Europe/Moscow'
time.tzset()
#time.tzname

progress_text = "Day in progress. Please wait."

day_start = time.struct_time((2025, 3, 4, 
                             9, 0, 0, 
                             3, 51, 0))

day_end = time.struct_time((2025, 3, 4, 
                           18, 0, 0, 
                           3, 51, 0))

day_duration = time.mktime(day_end)-time.mktime(day_start)
day_curtime = time.mktime(time.localtime()) - time.mktime(day_start)
day_progress = day_curtime/day_duration

my_bar = st.progress(day_progress, text=progress_text)
placeholder = st.empty()

st.write(time.localtime())

while True:
    time.sleep(0.100)

    #st.write(day_end)
    #st.write(time.mktime(day_end)-time.mktime(day_start))

    #st.write(time.localtime())
    #day_updtime = (time.mktime(time.localtime()) - day_curtime)/day_duration

    day_curtime = time.mktime(time.localtime()) - time.mktime(day_start)
    day_progress = round(day_curtime/day_duration, 5)

    #st.write(day_curtime)
    #st.write(day_updtime)
    #st.write(day_progress)
    #st.write(day_duration)

    my_bar.progress(day_progress, text=progress_text)
    #with st.empty():
    #placeholder = st.empty()
    placeholder.write(f"Curent progress is: {round(day_progress*100, 3)} %")
    time.sleep(1)
    #st.write(time.asctime(time.localtime()))


