import streamlit as st
import cv2
from datetime import datetime
from datetime import date
import calendar


my_date = date.today()
weekday = calendar.day_name[my_date.weekday()]

st.title("Motion Detector")
start_button = st.button("Start Camera")

if start_button:
    stream_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.putText(img=frame, text=weekday, org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1,
                    color=(20, 100, 100),
                    thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=str(datetime.now()), org=(50, 80),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(20, 100, 100),
                    thickness=2, lineType=cv2.LINE_AA)
        stream_image.image(frame)
