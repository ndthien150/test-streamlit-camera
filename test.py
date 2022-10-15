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

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))
