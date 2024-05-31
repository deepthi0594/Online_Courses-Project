import streamlit as st

st.set_page_config(page_title="Project Description", page_icon="🎓")

st.markdown("# Project Description")

st.write(
    """
    Recent years have seen an increase in interest towards online courses and formations. Hence, studying factors such as course subject, prices, rating, etc. might help us understand what influences customers in choosing an online course. 
    To study those trends, I'll use some data that was scrapped from 2 online academies: 
    - [Udemy](https://www.udemy.com/) 
    - and [edX](https://www.edx.org/)
    """)


st.write(
    """
    ### Goals:
    - Understand current trends/popularity of the courses
    - Compare the 2 online academies
    - Predict the growth in number of students on a 4 year timeframe  
    """)

st.write(
    """Please note that for this project I did not scrape ALL the existing courses offered by Udemy nor edX as I wanted to have datasets matching with 2 older ones.""")

st.write(
    """
    Links:
    - [GitHub](https://github.com/NolwennLeBas/Online_Courses-Project) repository
    - 2020 Kaggle datasets: [Udemy](https://www.kaggle.com/datasets/andrewmvd/udemy-courses), [edX](https://www.kaggle.com/datasets/santoshapatil31/edx-all-courses-3082-courses)
    """)

st.image(['./images/udemy.png','./images/edx.png'], width=300)
