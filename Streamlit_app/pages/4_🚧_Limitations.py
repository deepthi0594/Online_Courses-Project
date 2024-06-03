import streamlit as st
from PIL import Image

st.set_page_config(page_title="Limitations", page_icon="🚧")

st.markdown("# Limitations")

st.write(
    """
    If you've played around with the filters in the prediction model you might have found that the only factors influencing its results where:
    - the previous number of students
    - the number of ratings
    """)

st.write("Sadly, this is why this model is really limited. ")

st.write(
    """
    The subjects are too grouped to be really informative, so what would be interesting would be to create subcategories in each subject based on key words of the course title for example.
    Building the model on this type of subcategories would allow it to better identify patterns about rating, price, academy,... related to specific type of courses instead of merging everything together and trying to predict based on the Subject.
    Furthermore, this type of prediction would be better if the model was built on a year by year dataset has there could be a slowing down in the number of students during the last 2 years for example.
    """)

st.write(
    """
    To have a better understanding of trends about online courses it would be wise to not only increase the amount of data/courses to study for each academy 
    but also push further the analysis by doing some nlp modeling to increase the identification of patterns by the prediction model.
    """)

st.write("#### The End")

image_4=Image.open('graduation_2.jpg', "rb")
st.image(image_4)