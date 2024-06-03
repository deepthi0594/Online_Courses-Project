import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Online Courses - by N.LB 🎓",
    page_icon="✍️",
)

st.write("# Hey there! 👋")

st.sidebar.success("Select a chapter above.")

st.markdown(
    """
    ### Are you curious about online academy and online courses?
    ### Well, here is a small data analytic project about this subject. Enjoy! 😁
    - Nolwenn LB
"""
)

image_1=Image.open('online_education.jpg', "rb")
st.image(image_1)