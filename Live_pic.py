import streamlit as st
import cv2
import numpy as np
import requests

# Title of the app
st.title( 'Mobile Camera Preview in Streamlit' )

# An empty image container that will hold the frames we'll fetch from the server
frame_window = st.image( [] )
while True:
    # Request the image from the server
    response = requests.get(url="https://100.90.44.90:8080/photo.jpg",verify=False)
    imgNp = np.array(bytearray(response.content), dtype=np.uint8)
    frame = cv2.imdecode(imgNp, cv2.IMREAD_UNCHANGED ) 
    # As OpenCV decodes images in BGR format, we'd convert it to the RGB format
    frame = cv2.cvtColor( frame , cv2.COLOR_BGR2RGB )

    frame_window.image(frame)



