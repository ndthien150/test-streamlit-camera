# import cv2
# import streamlit as st
#
#
# st.title("Camera Application")
# run = st.checkbox('Run')
# Frame_window = st.image([])
# cam = cv2.VideoCapture(1)
#
# while run:
#     ret, frame = cam.read()
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     Frame_window.image(frame)
# else:
#     st.write("Stopped")

import streamlit as st
from webcam import webcam

captured_image = webcam()
if captured_image is None:
    st.write("Waiting for capture...")
else:
    st.write("Got an image from the webcam:")
    st.image(captured_image)