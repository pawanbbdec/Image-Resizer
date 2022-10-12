import os
import streamlit as st
from PIL import Image, ImageFilter


def resize_file(files,w,h):
    for file in files:
        img = Image.open(file)
        out = img.resize((w,h))
        st.image(out,caption=file.name)

st.title("Image Resizer")

filter_list = ['No filter','Grayscale','Outline','Inverted Outline','Blurred','Smooth']

with st.form("Resize form"):
    files = st.file_uploader("Select your Images",['jpg','png','bmp','webp'], accept_multiple_files=True, help="Select on Images")
    c1, c2 = st.columns(2)
    h = c1.number_input("Select Image Width", min_value=10, max_value=5000)
    w = c2.number_input("Select Image Height", min_value=10, max_value=5000)
    filter = st.selectbox("Select Image Filter", filter_list)
    btn = st.form_submit_button("Resize Now")

if btn:
    st.success("You submitted the form")
    resize_file(files, w, h)

# streamlit run app.py