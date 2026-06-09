import streamlit as st

st.title("Media-image")

# 서버 이미지
st.image("../data/sponge.jfif", caption="Spongebob SquarePants")

# 웹 이미지
image_url = "http://www.hueree.com/data/file/5_6_1_1/20080701170424-1.jpg"
st.image(image_url, caption="Spongebob SquarePants")
